# import os,re
# import sys
# import time
# import tempfile
# from PySide6.QtCore import QObject, Signal
# from datetime import timedelta
# import whisper
# from opencc import OpenCC
# import subprocess
# from tqdm import tqdm
# from gui.core.api_utils.asr import ASRClient
# # 字幕生成
# # 音频切片，可以正常识别音频并输出分片字幕
# def clean_temp(files):
#     for file in files:
#         if os.path.exists(file):
#             try:
#                 os.remove(file)
#             except Exception as e:
#                 print(f"警告：无法删除临时文件 {file}: {e}")

# class SubtitleWorker(QObject):
#     progress = Signal(str, int)
#     finished = Signal(bool, str)
#     subtitle_updated = Signal(float,float,str)  

#     def __init__(self,asr_client, video_path, srt_path,  total_duration, slice_duration=10, short_segment_threshold=2.0):
#         super().__init__()
#         self.asr_client=asr_client
#         self.video_path = video_path
#         self.srt_path = srt_path,
#         self.slice_duration = slice_duration  # 切片时长
#         self.short_segment_threshold = short_segment_threshold  # 阈值
#         self.is_running = True
#         self.converter = OpenCC('t2s')  
#         self.model = None  
#         self.subtitle_index = 1  
#         self.temp_files = []  
#         self.short_segments_cache = []  
#         self.total_duration=total_duration

#     def preload_model(self):
#         # """预加载Whisper模型（避免实时识别时卡顿）"""
#         # self.progress.emit("正在加载识别模型...", 5)
#         # self.model = whisper.load_model(self.model_size)
#         # self.progress.emit("模型加载完成", 10)
#         """预加载API"""
#         self.progress.emit("正在加载识别模型...", 5)
#     def extract_audio_slice(self, start_time, duration, output_file):
#         cmd = [
#             'ffmpeg',
#             '-y',  # 覆盖已存在的文件
#             '-ss', f'{start_time:.2f}',  # 起始时间
#             '-i', self.video_path,  # 输入视频文件
#             '-t', f'{duration:.2f}',  # 提取时长
#             '-vn',  # 禁用视频流
#             '-acodec', 'pcm_s16le',  # 音频编码
#             '-ar', '16000',  # 采样率
#             '-ac', '1',  # 单声道
#             '-f', 'wav',  # 输出格式
#             '-hide_banner',  # 隐藏banner信息
#             '-loglevel', 'error',  # 仅输出错误信息
#             output_file  # 输出文件路径
#         ]

#         try:
#             subprocess.run(
#                 cmd,
#                 check=True,
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE,
#                 encoding='utf-8'
#             )
#         except subprocess.CalledProcessError as e:
#             print(f"音频提取失败：{e.stderr}")
#             raise Exception(f"ffmpeg提取音频失败：{e.stderr}")

#         if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
#             raise Exception(f"音频切片文件生成失败：{output_file}")


#     def merge_short_segments(self):
#         if not self.short_segments_cache:
#             return
        
#         merged_start = self.short_segments_cache[0]["start"]
#         merged_end = self.short_segments_cache[-1]["end"]
#         merged_text = "".join([seg["text"] for seg in self.short_segments_cache])
        
#         start_str = self.format_srt_time(merged_start)
#         end_str = self.format_srt_time(merged_end)
        
#         with open(self.srt_path, "a", encoding="utf-8") as f:
#             f.write(f"{self.subtitle_index}\n")
#             f.write(f"{start_str} --> {end_str}\n")
#             f.write(f"{merged_text}\n\n")
        
#         self.subtitle_updated.emit(merged_start,merged_end,merged_text)
#         self.subtitle_index += 1
        
#         self.short_segments_cache = []

#     def run(self):
#         try:
#             self.preload_model()

#             if not self.total_duration or self.total_duration <= 0:
#                 raise Exception("无法获取视频时长")

#             with open(self.srt_path, "w", encoding="utf-8") as f:
#                 f.write("")

#             current_time = 0
#             self.progress.emit("开始实时生成字幕...", 10)
            
#             # 计算总切片数
#             total_slices = int(self.total_duration / self.slice_duration) + 1
            
#             # 使用tqdm显示进度条（同时指定file和position避免重复）
#             with tqdm(total=total_slices, desc="字幕生成", unit="切片", ncols=100, file=sys.stdout, position=0) as pbar:
#                 while current_time < self.total_duration and self.is_running:
#                     # 计算当前进度
#                     progress_percent = int(10 + (current_time / self.total_duration) * 90)
#                     self.progress.emit(f"正在识别 {current_time:.1f} - {current_time + self.slice_duration:.1f} 秒...", progress_percent)

#                     # 创建临时音频切片文件
#                     temp_fd, temp_audio = tempfile.mkstemp(suffix=".wav")
#                     os.close(temp_fd)  # 关闭文件描述符
#                     self.temp_files.append(temp_audio)

#                     # 提取当前时间段的音频切片
#                     self.extract_audio_slice(current_time, self.slice_duration, temp_audio)

#                     # 检查切片文件是否有效
#                     if not os.path.exists(temp_audio) or os.path.getsize(temp_audio) == 0:
#                         current_time += self.slice_duration
#                         continue

#                     #识别切片音频
#                     # result = self.model.transcribe(
#                     #     temp_audio,
#                     #     language="zh",
#                     #     verbose=None,  # 使用None完全禁用输出
#                     #     fp16=False,
#                     #     no_speech_threshold=0.1
#                     # )
#                     res = self.asr_client.transcribe(
#                         file_path=temp_audio,
#                         model="TeleAI/TeleSpeechASR"
#                     )
#                     #之前写死强制以slice_duration为字幕起止时间间隔
#                     # 解析识别结果并处理短片段合并
#                     if result["segments"]:
#                         for seg in result["segments"]:
#                             # 修正字幕时间（基于切片起始时间）
#                             seg_start = current_time + seg["start"]
#                             seg_end = current_time + seg["end"]
#                             seg_duration = seg_end - seg_start
#                             # 繁转简
#                             subtitle_text = self.converter.convert(seg["text"].strip())

#                             # 判断是否为短片段
#                             if seg_duration < self.short_segment_threshold:
#                                 # 加入缓存
#                                 self.short_segments_cache.append({
#                                     "start": seg_start,
#                                     "end": seg_end,
#                                     "text": subtitle_text
#                                 })
#                             else:
#                                 # 先合并缓存中的短片段
#                                 self.merge_short_segments()
#                                 # 直接写入长片段
#                                 start_str = self.format_srt_time(seg_start)
#                                 end_str = self.format_srt_time(seg_end)
#                                 with open(self.srt_path, "a", encoding="utf-8") as f:
#                                     f.write(f"{self.subtitle_index}\n")
#                                     f.write(f"{start_str} --> {end_str}\n")
#                                     f.write(f"{subtitle_text}\n\n")
#                                 self.subtitle_updated.emit(seg_start,seg_end,subtitle_text)
#                                 self.subtitle_index += 1

#                     # 切片结束时，合并剩余的短片段
#                     self.merge_short_segments()
#                     # 推进时间轴
#                     current_time += self.slice_duration
#                     time.sleep(0.1)
                        
#                     # 更新进度条
#                     pbar.update(1)
#                     pbar.set_postfix_str(f"时间: {current_time:.1f}s")

#                 # 最终合并所有剩余的短片段
#                 self.merge_short_segments()

#                 if self.is_running:
#                     self.progress.emit("实时字幕生成完成！", 100)
#                     self.finished.emit(True, f"实时字幕已保存：{os.path.basename(self.srt_path)}")
#                 else:
#                     self.finished.emit(False, "用户终止了实时字幕生成")

#         except Exception as e:
#             self.finished.emit(False, f"实时字幕生成失败：{str(e)}")
#         finally:
#             clean_temp(self.temp_files)

#     def format_srt_time(self, seconds):
#         """将秒数转换为SRT标准时间格式（00:00:00,000）"""
#         td = timedelta(seconds=seconds)
#         hours, remainder = divmod(td.seconds, 3600)
#         minutes, secs = divmod(remainder, 60)
#         milliseconds = td.microseconds // 1000
#         return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

#     def stop(self):
#         self.is_running = False


import os,re
import sys
import time
import tempfile
from PySide6.QtCore import QObject, Signal
from datetime import timedelta
import whisper
from opencc import OpenCC
import subprocess
from tqdm import tqdm
from funasr import AutoModel

# 字幕生成
# 音频不切片
def clean_temp(files):

    for file in files:
        if os.path.exists(file):
            try:
                os.remove(file)
            except Exception as e:
                print(f"警告：无法删除临时文件 {file}: {e}")


class SubtitleWorker(QObject):
    progress = Signal(str, int)
    finished = Signal(bool, str)

    def __init__(self,model, video_path, srt_path):
        super().__init__()
        self.video_path = video_path
        self.srt_path = srt_path
        self.is_running = True
        self.converter=OpenCC('t2s')
        self.model=model
    def run(self):
        audio_temp = "temp_audio.wav"
        try:
            self.progress.emit("正在提取音频...", 20)
            # 提取音频
            os.system(f'ffmpeg -i "{self.video_path}" -vn -acodec pcm_s16le -ar 16000 -ac 1 "{audio_temp}"')
            # 检测音频临时文件是否生成，且有数据写入
            if not self.is_running or not os.path.exists(audio_temp) or os.path.getsize(audio_temp) == 0:
                raise Exception("音频提取失败或用户取消操作")

            self.progress.emit(f"正在使用 funasr 模型识别...", 40)

            self.audio_to_subtitle(self.model,audio_temp,self.srt_path)
            if not self.is_running:
                raise Exception("用户取消了生成")

            self.progress.emit("正在解析并保存字幕...", 80)
        
            # 提示字幕生成完成
            self.progress.emit("字幕生成完成！", 100)
            self.finished.emit(True, f"字幕已保存为SRT文件：{os.path.basename(self.srt_path)}")

        except Exception as e:
            self.finished.emit(False, f"字幕生成失败：{str(e)}")
        finally:
            clean_temp([audio_temp])

    def format_time(self,seconds):
        """将秒数格式化为 SRT 字幕时间格式: 00:00:00,000"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        ms = int((seconds - int(seconds)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"

    def split_text_by_punctuation(self,text, split_chars=None):
        """按标点拆分文本，适配时间戳分段"""
        if split_chars is None:
            split_chars = r'，。！？；：、.?!;:'
        parts = re.split(f'([{split_chars}])', text)
        merged_parts = []
        temp = ""
        for part in parts:
            if part:
                temp += part
                if part in split_chars:
                    merged_parts.append(temp.strip())
                    temp = ""
        if temp:
            merged_parts.append(temp.strip())
        return merged_parts

    # ==================== 复用模型生成字幕 ====================
    def audio_to_subtitle(self,preloaded_model, audio_path, output_srt_path=None):

        # 设置默认输出路径
        if output_srt_path is None:
            base_name = os.path.splitext(audio_path)[0]
            output_srt_path = f"{base_name}.srt"
        
        # 复用模型进行推理（无需重新加载）
        print(f"\n正在处理音频: {audio_path}")
        res = preloaded_model.generate(
            input=audio_path,
            batch_size_s=30,
            merge_vad=True,
            use_itn=True,
            add_pause=True,
            predict_timestamp=True
        )
        
        srt_content = []
        index = 1
        try:
            full_text = res[0].get("text", "").strip()
            timestamps_ms = res[0].get("timestamp", [])
            
            if not full_text or not timestamps_ms:
                raise ValueError("未获取到有效文本或时间戳")
            
            # 拆分文本 + 匹配时间戳
            text_segments = self.split_text_by_punctuation(full_text)
            # 适配文本和时间戳数量
            if len(text_segments) > len(timestamps_ms):
                text_segments = text_segments[:len(timestamps_ms)]
            elif len(text_segments) < len(timestamps_ms):
                ts_per_segment = len(timestamps_ms) // len(text_segments)
                remainder = len(timestamps_ms) % len(text_segments)
                new_timestamps = []
                current = 0
                for i in range(len(text_segments)):
                    count = ts_per_segment + (1 if i < remainder else 0)
                    count = min(count, len(timestamps_ms) - current)
                    start_ms = timestamps_ms[current][0]
                    end_ms = timestamps_ms[current + count - 1][1]
                    new_timestamps.append([start_ms, end_ms])
                    current += count
                timestamps_ms = new_timestamps
            
            # 生成字幕片段
            for i in range(min(len(text_segments), len(timestamps_ms))):
                start_ms, end_ms = timestamps_ms[i]
                start_time = start_ms / 1000.0
                end_time = end_ms / 1000.0
                text = text_segments[i]
                
                if not text or start_time >= end_time:
                    continue
                
                start_str = self.format_time(start_time)
                end_str = self.format_time(end_time)
                srt_content.extend([str(index), f"{start_str} --> {end_str}", text.strip(), ""])
                index += 1
            
            if index == 1:
                raise ValueError("未生成有效字幕片段")
        
        except Exception as e:
            print(f"⚠️ 解析失败: {e}，启用兜底方案")
            full_text = res[0].get("text", "").strip()
            if full_text:
                srt_content = ["1", "00:00:00,000 --> 00:30:00,000", full_text, ""]
        
        # 写入文件
        with open(output_srt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(srt_content))
        print(f"✅ 字幕生成完成: {output_srt_path}")
        print(f"📝 共生成 {max(index-1, 1)} 条字幕")

    def stop(self):
        self.is_running = False