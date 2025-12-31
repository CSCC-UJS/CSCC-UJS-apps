import os,sys
import re
script_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["PATH"] = script_dir + os.pathsep + os.environ["PATH"]
import mpv
import time

class MPVPlayerCore:
    def __init__(self):
        self.mpv_player = mpv.MPV(
            vo='gpu',  
            input_default_bindings=True,
            input_vo_keyboard=True,
            osc=True, 
            # SUBTITLE OPTIONS
            sid='auto',
            sub_auto='fuzzy',
            sub_font_size=24,
            sub_color='#FFFFFF',
            sub_border_color='#000000',
            sub_border_size=2
        )

        self.is_playing = False
        self.current_file = None

        self.set_volume(80)

        self.injected_subtitle_ids = []
        self.temp_sub_track_id=None

        self.duration_loaded = False

        @self.mpv_player.event_callback('file-loaded')
        def on_file_loaded(event):
            self.duration_loaded = True

        self.progress_update_callback=None

        @self.mpv_player.property_observer('time-pos')
        def time_pos_observer(_name, value):
            #进度监听回调
            if self.progress_update_callback and value is not None:
                self.progress_update_callback(value, self.get_duration())


    def bind_to_window(self, win_id):
        #将MPV绑定到指定窗口
        self.mpv_player.wid = str(int(win_id))

    def load_video(self, file_path):
        #加载并播放指定视频文件
        self.stop()
        self.current_file = file_path
        self.duration_loaded= False
        self.mpv_player.play(file_path)
        self.is_playing = True


    def toggle_play_pause(self):
        #切换播放/暂停状态
        if not self.current_file:
            raise ValueError("未加载视频文件")
        
        if self.is_playing:
            self.mpv_player.pause=True
            self.is_playing = False
        else:
            self.mpv_player.pause=False
            self.is_playing = True


    def stop(self):
        #停止播放并重置状态
        if self.current_file:
            self.mpv_player.stop()
            self.is_playing = False
            self.current_file = None
            if self.temp_sub_track_id is not None:
                self.mpv_player.command('sub-remove', self.temp_sub_track_id)
                self.temp_sub_track_id = None
    def set_volume(self, value):
        if 0 <= value <= 100:
            self.mpv_player.volume = value

    def get_volume(self):
        return self.mpv_player.volume

    def get_duration(self, timeout=5.0, interval=0.1):
        #获取总时长
        start = time.time()
        while time.time() - start < timeout:
            if self.duration_loaded:
                try:
                    return self.mpv_player.duration or 0
                except AttributeError:
                    return 0
            time.sleep(interval)
        return 0
    
    def set_position(self, seconds):
        if 0 <= seconds <= self.get_duration():
            self.mpv_player.seek(seconds, reference='absolute')

    def get_position(self):
        try:
            return self.mpv_player.time_pos or 0
        except:
            return 0

    def set_progress_callback(self, callback):
        #进度更新回调
        self.progress_update_callback = callback

    def set_subtitle_file(self,subtitle_path):
        #设置字幕文件路径
        if os.path.exists(subtitle_path):
            self.mpv_player.sub_file=subtitle_path
        else:
            raise FileNotFoundError(f"字幕文件不存在：{subtitle_path}")
        
# 临时字幕注入
# ///////////////////////////////////////////////////////////////    
# mpv命令参数有问题，无法实时注入字幕
    def inject_mpv_subtitle(self, subtitle_text):


        if not isinstance(subtitle_text, str):
            print(f"字幕文本类型错误，要求字符串，实际为：{type(subtitle_text)} | 内容：{subtitle_text}")
            return
    
        subtitle_text = subtitle_text.strip()
        if not subtitle_text or not self.mpv_player:
            return

        try:
            # 2. 解析字幕时间和内容（适配 srt 格式）
            time_pattern = r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})"
            match = re.search(time_pattern, subtitle_text)
            if not match:
                print(f"字幕格式解析失败，未匹配到时间轴 | 内容：{subtitle_text}")
                return

            # 转换 SRT 时间为秒数
            start_time = self._srt_time_to_seconds(match.group(1))
            end_time = self._srt_time_to_seconds(match.group(2))
            content = re.sub(time_pattern, "", subtitle_text).strip()
        
            if not content or start_time >= end_time:
                print(f"字幕内容为空或时间轴无效 | 开始：{start_time} 结束：{end_time} 内容：{content}")
                return

            sub_content = f"{start_time:.3f} --> {end_time:.3f}\n{content}"
        
            self.mpv_player.command(
                "sub-add", 
                sub_content, 
                "select,temporary"
            )
        
            # 记录注入的字幕轨道ID
            self.injected_subtitle_ids.append(self.mpv_player.sub)

        except Exception as e:
            print(f"字幕注入失败：{type(e).__name__} - {e} | 字幕内容：{subtitle_text[:100]}")

    def _srt_time_to_seconds(self, srt_time):
        #转换 SRT 时间格式
        try:
            hours, minutes, seconds = srt_time.split(":")
            seconds, milliseconds = seconds.split(",")
            total_seconds = (
            int(hours) * 3600
            + int(minutes) * 60
            + int(seconds)
            + int(milliseconds) / 1000
            )
            return total_seconds
        except:
            return 0.0

    def fast_forward(self):
        if not self.current_file:
            raise ValueError("未加载视频文件，无法快进")
    
        total_duration = self.get_duration()
        current_pos = self.get_position()
    
        increment = total_duration * 0.01
        if increment <= 0: 
            return
    
        new_pos = min(current_pos + increment, total_duration)
    

        self.set_position(new_pos)

    def fast_rewind(self):
        if not self.current_file:
            raise ValueError("未加载视频文件，无法快退")
    
        total_duration = self.get_duration()
        current_pos = self.get_position()
    
        increment = total_duration * 0.01
        if increment <= 0:
            return
    
        new_pos = max(current_pos - increment, 0)
        self.set_position(new_pos)

    def cleanup(self):
        self.stop()
        self.mpv_player.terminate()

    def __del__(self):
        self.cleanup()