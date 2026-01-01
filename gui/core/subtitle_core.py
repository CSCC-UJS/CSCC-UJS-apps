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

    def __init__(self, video_path, srt_path):
        super().__init__()
        self.video_path = video_path
        self.srt_path = srt_path
        self.is_running = True
        self.converter=OpenCC('t2s')

        self.model = AutoModel(
            model="paraformer-zh",
            vad_model="fsmn-vad",
            punc_model="ct-punc",
            disable_update=True,
            device="cpu",
            model_revision="v2.0.4"  # 锁定稳定版本，避免时间戳格式波动
        )

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

            result = self.model.generate(
                input=audio_temp,
                batch_size=16,
                return_timestamps=True,
                timestamp_type="word",
                word_level=True
                )
            if not self.is_running:
                raise Exception("用户取消了生成")

            self.progress.emit("正在解析并保存字幕...", 80)
            # 生成SRT内容
            srt_content = []
            srt_index = 1  # SRT序号从1开始

            for seg_idx, segment in enumerate(result):
                full_text = segment.get("text", "").strip()
                word_timestamp_list = segment.get("timestamp", [])
                if not full_text or not word_timestamp_list:
                    continue

                # 拆分文本为词列表
                text_parts = re.findall(r"([^，。！？；：\s]+|[，。！？；：])", full_text)
                word_list = [part for part in text_parts if part.strip()]

                # 对齐词和时间戳长度
                min_length = min(len(word_list), len(word_timestamp_list))
                word_list = word_list[:min_length]
                word_timestamp_list = word_timestamp_list[:min_length]

                # 按句子合并生成SRT条目
                current_sentence = []
                current_start_ms = None
                
                for word, ts_item in zip(word_list, word_timestamp_list):
                    start_ms, end_ms = self.get_word_timestamps(ts_item)
                    
                    if current_start_ms is None:
                        current_start_ms = start_ms
                    
                    current_sentence.append(word)
                    
                    # 遇到句末标点，生成SRT条目
                    if word in ["。", "！", "？", "；"]:
                        # 转换时间格式
                        start_srt = self.ms_to_srt_time(current_start_ms)
                        end_srt = self.ms_to_srt_time(end_ms)
                        # 拼接句子文本
                        sentence_text = "".join(current_sentence)
                        # 添加SRT条目
                        srt_content.append(f"{srt_index}")
                        srt_content.append(f"{start_srt} --> {end_srt}")
                        srt_content.append(sentence_text)
                        srt_content.append("")  # 空行分隔条目
                        # 更新序号和缓存
                        srt_index += 1
                        current_sentence = []
                        current_start_ms = None
                
                # 处理最后一句（无句末标点）
                if current_sentence:
                    start_ms = current_start_ms if current_start_ms else 0
                    last_start_ms, last_end_ms = self.get_word_timestamps(word_timestamp_list[-1])
                    start_srt = self.ms_to_srt_time(start_ms)
                    end_srt = self.ms_to_srt_time(last_end_ms)
                    sentence_text = "".join(current_sentence)
                    # 添加最后一句的SRT条目
                    srt_content.append(f"{srt_index}")
                    srt_content.append(f"{start_srt} --> {end_srt}")
                    srt_content.append(sentence_text)
                    srt_content.append("")
                    srt_index += 1

            # 保存SRT文件
            with open(self.srt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(srt_content))
            # 提示字幕生成完成
            self.progress.emit("字幕生成完成！", 100)
            self.finished.emit(True, f"字幕已保存为SRT文件：{os.path.basename(self.srt_path)}")

        except Exception as e:
            self.finished.emit(False, f"字幕生成失败：{str(e)}")
        finally:
            clean_temp([audio_temp])

    def get_word_timestamps(self,timestamp_item):
        if isinstance(timestamp_item, (list, tuple)):
            if len(timestamp_item) == 2 and isinstance(timestamp_item[1], (list, tuple)):
                return [int(timestamp_item[1][0]), int(timestamp_item[1][1])]
            elif len(timestamp_item) >= 2:
                return [int(timestamp_item[0]), int(timestamp_item[1])]
        return [0, 100]

    # 辅助函数：转换毫秒到SRT时间格式 (00:00:00,000)
    def ms_to_srt_time(self,ms):
        seconds = ms // 1000
        minutes = seconds // 60
        hours = minutes // 60
        remaining_seconds = seconds % 60
        remaining_minutes = minutes % 60
        remaining_ms = ms % 1000
        return f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d},{remaining_ms:03d}"

    def stop(self):
        self.is_running = False