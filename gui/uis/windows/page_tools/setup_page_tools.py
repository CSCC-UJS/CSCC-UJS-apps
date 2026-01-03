# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import tempfile
from gui.uis.windows.main_window.functions_main_window import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.page_videoplayer.setup_page_videoplayer import SetupPageVideoPlayer

# IMPORT KEYWORD AND SUMMARY MODULES
# ///////////////////////////////////////////////////////////////
from gui.core.keyword_core import KeywordAbstract
from gui.core.summary_core import Summary

# IMPORT SUBTITLEWORKER CORE
# ///////////////////////////////////////////////////////////////
from gui.core.subtitle_core import SubtitleWorker,clean_temp

# IMPORT FUNASR
# ///////////////////////////////////////////////////////////////
from funasr import AutoModel
import os

class SetupPageTools(QObject):
    def __init__(self):
        super().__init__()
        self.video_class=None
        self.ui=None

        self.keyword_num=1
        self.keysentence_num=1

        self.video_not_playing_path=""


        self.generate_subtitle_file=True
    # SETUP PAGE_TOOLS
    # ///////////////////////////////////////////////////////////////
    def setup_page_tools(self):
        # CHECK LOAD UI
        # ///////////////////////////////////////////////////////////////
        if self.ui is None:
            self.ui = UI_MainWindow()
            self.ui.setup_ui(self)
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        # SET THEME 
        # ///////////////////////////////////////////////////////////////
        self.setup_push_buttons_style()
        self.ui.load_pages.line_file.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.toggle_edit.set_stylesheet(
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.toggle_edit.setEnabled(False)
        self.ui.load_pages.btn_file.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.btn_save_sub.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.btn_start_sub.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_sub = PyCircularProgress(
            value = 0,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_sub.setFixedSize(200,200)
        self.ui.load_pages.layout_circular_bar.addWidget(self.circular_progress_sub)

        self.table_sub = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_sub.setColumnCount(3)
        self.table_sub.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  
        self.table_sub.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_sub.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_sub.verticalHeader().setVisible(False)
        self.table_sub.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Columns / Header
        header = self.table_sub.horizontalHeader()
        for idx in range(3):
            if idx == 2:  
                header.setSectionResizeMode(idx, QHeaderView.Stretch)
            else:  
                header.setSectionResizeMode(idx, QHeaderView.Fixed)

        QTimer.singleShot(0, self.set_table_column_widths)

        self.column_index = QTableWidgetItem()
        self.column_index.setTextAlignment(Qt.AlignCenter)
        self.column_index.setText("INDEX")

        self.column_time = QTableWidgetItem()
        self.column_time.setTextAlignment(Qt.AlignCenter)
        self.column_time.setText("TIME")

        self.column_content = QTableWidgetItem()
        self.column_content.setTextAlignment(Qt.AlignCenter)
        self.column_content.setText("CONTENT")

        # Set column
        self.table_sub.setHorizontalHeaderItem(0, self.column_index)
        self.table_sub.setHorizontalHeaderItem(1, self.column_time)
        self.table_sub.setHorizontalHeaderItem(2, self.column_content)

        self.ui.load_pages.layout_subtitle_table.addWidget(self.table_sub)

        self.ui.load_pages.btn_keyword.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.ui.load_pages.btn_summary.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.ui.load_pages.comboBox_keynum.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )


        self.ui.load_pages.comboBox_topK.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )

        self.ui.load_pages.plainTextEdit.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        # SET CONNECTIONS
        # ///////////////////////////////////////////////////////////////
        self.ui.load_pages.btn_file.clicked.connect(self.open_file)
        self.ui.load_pages.btn_save_sub.clicked.connect(self.save_subtitle)
        self.ui.load_pages.btn_start_sub.clicked.connect(self.generate_subtitle_without_video)
        self.ui.load_pages.btn_keyword.clicked.connect(self.start_keyword_worker)
        self.ui.load_pages.btn_summary.clicked.connect(self.start_summary_worker)

        self.ui.load_pages.comboBox_keynum.currentIndexChanged.connect(self.update_btn_keyword)
        self.ui.load_pages.comboBox_topK.currentIndexChanged.connect(self.set_keysentence_num)
# BIND CONNECTIONS
# ///////////////////////////////////////////////////////////////
    def bind_video_class(self,video_settings:SetupPageVideoPlayer):
        self.video_class=video_settings
        self.video_class.subtitle_progress_updated.connect(self.update_circular_progress)
        
        self.video_class.video_path_updated.connect(self.ui.load_pages.line_file.setText)

        self.total_subtext=""
        self.video_class.subtitle_sentence_updated.connect(self.update_subtitle_table)
        
        self.sub_status=0
        self.video_class.sub_generate_status_changed.connect(self.update_sub_generate_status)

    def update_circular_progress(self,progress):
        self.circular_progress_sub.set_value(progress)

    def update_subtitle_table(self,index,start,end,text):
        self.total_subtext=self.total_subtext+text
        row_number = self.table_sub.rowCount()
        self.table_sub.insertRow(row_number)
        self.table_sub.setItem(row_number, 0, QTableWidgetItem(str(index))) # Add index
        time_text = f"{self.video_class.format_time(start)} --> {self.video_class.format_time(end)}"
        self.table_sub.setItem(row_number, 1, QTableWidgetItem(time_text)) # Add time
        self.table_sub.setItem(row_number, 2, QTableWidgetItem(text)) # Add content
        self.table_sub.setRowHeight(row_number, 40)
        self.ui.load_pages.layout_subtitle_table.addWidget(self.table_sub)
    
    def update_sub_generate_status(self,status):
        self.sub_status=status
        if status==0:
            self.ui.load_pages.toggle_edit.setEnabled(False)
            self.ui.load_pages.btn_keyword.setEnabled(False)
            self.ui.load_pages.btn_summary.setEnabled(False)
            self.ui.load_pages.btn_save_sub.setEnabled(False)
            self.ui.load_pages.btn_start_sub.setEnabled(True)
            self.table_sub.setEditTriggers(QAbstractItemView.NoEditTriggers)
        elif status==1:
            self.ui.load_pages.btn_start_sub.setEnabled(False)
        elif status==2:
            self.ui.load_pages.toggle_edit.setEnabled(True)
            self.ui.load_pages.btn_keyword.setEnabled(True)
            self.ui.load_pages.btn_summary.setEnabled(True)
            self.ui.load_pages.btn_save_sub.setEnabled(True)
            self.table_sub.setEditTriggers(QAbstractItemView.AllEditTriggers)
            print(self.total_subtext)

    def update_btn_keyword(self):
        num_key=int(self.ui.load_pages.comboBox_keynum.currentText())
        self.keyword_num=num_key
        self.setup_push_buttons_status(num_key)

    def set_keysentence_num(self):
        self.keysentence_num=int(self.ui.load_pages.comboBox_topK.currentText())

    def setup_push_buttons_status(self,num):
        for btn_num in range(1, num+1):
            btn_attr_name = f"pushButton_{btn_num}"
            if hasattr(self.ui.load_pages, btn_attr_name):
                btn = getattr(self.ui.load_pages, btn_attr_name)
                btn.show()
            else:
                print(f"Warning: Button {btn_attr_name} not found in load_pages!")
        for btn_num in range(num+1, 11):
            btn_attr_name = f"pushButton_{btn_num}"
            if hasattr(self.ui.load_pages, btn_attr_name):
                btn = getattr(self.ui.load_pages, btn_attr_name)
                btn.hide()
            else:
                print(f"Warning: Button {btn_attr_name} not found in load_pages!")


    def setup_push_buttons_style(self):
        btn_style = {
            "radius": 10,
            "color": self.themes["app_color"]["text_foreground"],
            "bg_color": self.themes["app_color"]["dark_one"],
            "bg_color_hover": self.themes["app_color"]["dark_three"],
            "bg_color_pressed": self.themes["app_color"]["dark_four"]
        }
        for btn_num in range(1, 11):
            btn_attr_name = f"pushButton_{btn_num}"

            if hasattr(self.ui.load_pages, btn_attr_name):
                btn = getattr(self.ui.load_pages, btn_attr_name)
                btn.set_style(**btn_style)
                btn.setText("KEYWORD")
                btn.hide()
            else:
                print(f"Warning: Button {btn_attr_name} not found in load_pages!")
        self.ui.load_pages.pushButton_1.show()  
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.ui.load_pages.video_widget,
            "选择播放文件",
            os.path.expanduser("~"),
            "视频文件 (*.mp4 *.avi *.mkv *.mov *.flv *.wmv);;音频文件 (*.mp3 *.wav *.flac *.aac);;所有文件 (*.*)"
        )
        if file_path and os.path.exists(file_path):
            self.video_not_playing_path=file_path
            self.ui.load_pages.line_file.setText(file_path)
            
    def save_subtitle(self):
        if self.sub_status != 2 or self.table_sub.rowCount() == 0:
            QMessageBox.warning(
                self.ui.load_pages.video_widget,
                "保存错误",
                "当前没有可保存的字幕数据！\n请先生成字幕。"
            )
            return
        
        default_path = ""
        if self.video_not_playing_path:
            default_path = os.path.splitext(self.video_not_playing_path)[0] + ".srt"
        save_path, _ = QFileDialog.getSaveFileName(
            self.ui.load_pages.video_widget,
            "保存字幕文件",
            default_path,
            "字幕文件 (*.srt);;所有文件 (*.*)"
        )
        if not save_path:
            return

        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                valid_subtitles = []
                
                for row in range(self.table_sub.rowCount()):
                    index_item = self.table_sub.item(row, 0)
                    time_item = self.table_sub.item(row, 1)
                    content_item = self.table_sub.item(row, 2)
                    if not all([index_item, time_item, content_item]):
                        continue
                    time_line = time_item.text().strip()
                    content = content_item.text().strip()

                    if not content:
                        continue
                    
                    formatted_time = self.format_srt_time_line(time_line)
                    if not self.validate_srt_time(formatted_time):
                        QMessageBox.warning(
                            self.ui.load_pages.video_widget,
                            "格式警告",
                            f"第{row+1}行时间格式无效，已跳过！\n原始时间：{time_line}"
                        )
                        continue
                    
                    valid_subtitles.append({
                        "time": formatted_time,
                        "content": content
                    })
                
                for idx, sub in enumerate(valid_subtitles, 1):
                    f.write(f"{idx}\n")
                    f.write(f"{sub['time']}\n")
                    clean_content = sub['content'].replace('\r\n', '\n').replace('\r', '\n')
                    f.write(f"{clean_content}\n\n")
                f.seek(f.tell() - 2, os.SEEK_SET)
                f.truncate()

            QMessageBox.information(
                self.ui.load_pages.video_widget,
                "保存成功",
                f"字幕文件已成功保存到：\n{save_path}\n共保存 {len(valid_subtitles)} 条字幕"
            )
        except Exception as e:
            QMessageBox.critical(
                self.ui.load_pages.video_widget,
                "保存失败",
                f"字幕文件保存失败！\n错误信息：{str(e)}"
            )

    def format_srt_time_line(self, time_line):
        if "-->" not in time_line:
            return "00:00:00,000 --> 00:00:05,000"  # 无效时间默认值
        
        parts = time_line.split("-->")
        if len(parts) != 2:
            return "00:00:00,000 --> 00:00:05,000"
        
        start_time = parts[0].strip()
        end_time = parts[1].strip()

        start_time = self.normalize_srt_time(start_time)
        end_time = self.normalize_srt_time(end_time)

        return f"{start_time} --> {end_time}"

    def normalize_srt_time(self, time_str):
        time_str = time_str.replace(".", ",")
        
        if "," in time_str:
            hms_part, ms_part = time_str.split(",", 1)
            ms_part = ms_part.ljust(3, "0")[:3]
        else:
            hms_part = time_str
            ms_part = "000"
        time_parts = hms_part.split(":")
        while len(time_parts) < 3:
            time_parts.insert(0, "00")

        time_parts = time_parts[-3:]

        h = time_parts[0].zfill(2)
        m = time_parts[1].zfill(2)
        s = time_parts[2].zfill(2)
        

        return f"{h}:{m}:{s},{ms_part}"

    def validate_srt_time(self, time_line):
        """
        验证时间轴是否符合SRT标准格式
        """
        if "-->" not in time_line:
            return False
        
        start, end = time_line.split("-->")
        start = start.strip()
        end = end.strip()
        
        pattern = r"^\d{2}:\d{2}:\d{2},\d{3}$"
        import re
        if not re.match(pattern, start) or not re.match(pattern, end):
            return False
        
        def time_to_seconds(time_str):
            h, m, s_ms = time_str.split(":")
            s, ms = s_ms.split(",")
            return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000
        
        try:
            start_sec = time_to_seconds(start)
            end_sec = time_to_seconds(end)
            return end_sec > start_sec
        except:
            return False

    def complete_ms(self,time_str):
        if "," not in time_str:
                time_str += ",000"
        else:
            hms, ms = time_str.split(",")
            ms = ms.ljust(3, "0")[:3]  
            time_str = f"{hms},{ms}"
        return time_str

    def set_table_column_widths(self):
            weights = [1, 3, 6]
            total_weight = sum(weights[:2])  
            table_width = self.table_sub.viewport().width() 
            
            col0_width = int(table_width * (weights[0] / (total_weight + weights[2])))
            col1_width = int(table_width * (weights[1] / (total_weight + weights[2])))
            
            self.table_sub.setColumnWidth(0, col0_width)
            self.table_sub.setColumnWidth(1, col1_width)


    

    
# KEYWORD FUNCTIONS
# ///////////////////////////////////////////////////////////////
    # 关键字提取线程
    def start_keyword_worker(self):
        # if not self.temp_srt or not os.path.exists(self.temp_srt):
        #     QMessageBox.warning(
        #         self.ui.load_pages.video_widget,
        #         "参数错误",
        #         "字幕文件不存在，无法提取关键字！\n请先生成或加载字幕。"
        #     )
        #     return
        self.keyword_worker = KeywordAbstract(subtext=self.total_subtext,srt_path=None,topK=self.keyword_num)
        self.keyword_thread = QThread(parent=self)  # 设置父对象，避免内存泄漏
        self.keyword_worker.moveToThread(self.keyword_thread)

        self.keyword_worker.progress.connect(self.on_keyword_progress)
        self.keyword_worker.finished.connect(self.on_keyword_finished)
        self.keyword_thread.started.connect(self.keyword_worker.run)
        self.keyword_thread.finished.connect(self.keyword_thread.deleteLater)

        self.keyword_thread.start()

    def on_keyword_progress(self, msg, progress):
        print(f"关键字提取进度：{progress}% - {msg}")  

    def on_keyword_finished(self, success, msg):
        if success:
            QMessageBox.information(self.ui.load_pages.video_widget, "成功", msg)
            self.show_keywords()
        else:
            QMessageBox.warning(self.ui.load_pages.video_widget, "失败", msg)

        if self.keyword_thread and self.keyword_thread.isRunning():
            self.keyword_thread.quit()
            self.keyword_thread.wait()  
        self.keyword_worker = None
        self.keyword_thread = None
        

    def stop_keyword_worker(self):
        if self.keyword_worker and self.keyword_thread and self.keyword_thread.isRunning():
            self.keyword_worker.stop()
            self.keyword_thread.quit()
            self.keyword_thread.wait()
            self.keyword_worker = None
            self.keyword_thread = None

    def set_keyword_settings(self, keyword_topK: int = 4):
   
        self.keyword_topK = keyword_topK  


    def show_keywords(self):
        print(f"关键字提取结果：{self.keyword_worker.keywords}")
        for index, key in enumerate(self.keyword_worker.keywords):
            btn_attr_name = f"pushButton_{index+1}"
            if hasattr(self.ui.load_pages, btn_attr_name):
                btn = getattr(self.ui.load_pages, btn_attr_name)
                btn.setText(f"{key}")
                btn.show()
            else:
                print(f"Warning: Button {btn_attr_name} not found in load_pages!")


# SUMMARY FUNCTIONS
# ///////////////////////////////////////////////////////////////
    # 摘要提取线程
    def start_summary_worker(self):
        self.summary_worker = Summary(sub_text=self.total_subtext,topK=self.keysentence_num)
        self.summary_thread = QThread(parent=self)  
        self.summary_worker.moveToThread(self.summary_thread)

        self.summary_worker.progress.connect(self.on_summary_progress)
        self.summary_worker.finished.connect(self.on_summary_finished)
        self.summary_thread.started.connect(self.summary_worker.run)
        self.summary_thread.finished.connect(self.summary_thread.deleteLater)

        self.summary_thread.start()
        QMessageBox.information(
            self.ui.load_pages.video_widget,
            "关键词提取",
            "关键词提取已启动，可在后台运行\n进度将在控制台打印"
        )

    def on_summary_progress(self, msg, progress):
        print(f"摘要进度：{progress}% - {msg}")  

    def on_summary_finished(self, success, msg):
        if success:
            QMessageBox.information(self.ui.load_pages.video_widget, "成功", msg)
            self.on_summary_result(self.summary_worker.key_sentences)
        else:
            QMessageBox.warning(self.ui.load_pages.video_widget, "失败", msg)

        # 停止线程
        if self.summary_thread and self.summary_thread.isRunning():
            self.summary_thread.quit()
            self.summary_thread.wait()  
        self.summary_worker = None
        self.summary_thread = None
    def on_summary_result(self, sentences):

        self.ui.load_pages.plainTextEdit.clear()  
    
        # 整理摘要内容
        summary_text = ""

        for idx, item in enumerate(sentences, 1):
            summary_text += f"{idx}. {item['sentence']}\n\n"
    
        self.ui.load_pages.plainTextEdit.setPlainText(summary_text)

    def stop_summary_worker(self):
        if self.summary_worker and self.summary_thread and self.summary_thread.isRunning():
            self.summary_worker.stop()
            self.summary_thread.quit()
            self.summary_thread.wait()
            self.summary_worker = None
            self.summary_thread = None


# SUBTITLE FUNCTIONS WITHOUT VIDEO
# ///////////////////////////////////////////////////////////////
    def generate_subtitle_without_video(self):
        video_dir = os.path.dirname(self.video_not_playing_path)
        video_name = os.path.splitext(os.path.basename(self.video_not_playing_path))[0]

        if self.generate_subtitle_file:
            # 保存到视频同目录
            self.temp_srt = os.path.join(video_dir, f"{video_name}.srt")
        else:
            # 生成临时字幕文件
            temp_fd, temp_path = tempfile.mkstemp(suffix=".srt", prefix="temp_sub_")
            os.close(temp_fd)
            self.temp_srt = temp_path
        self.model = AutoModel(
            model="paraformer-zh",
            vad_model="fsmn-vad",
            punc_model="ct-punc",
            isable_update=True,
            device="cpu",
            model_revision="v2.0.4"
        )
        # 2. 创建字幕生成线程
        self.subtitle_worker = SubtitleWorker(
            model=self.model,
            player_core=None,
            video_path=self.video_not_playing_path,
            srt_path=self.temp_srt,
            whether_play_video=False,
            total_duration=None,
            slice_duration=20,
            short_segment_threshold=3.0
        )
        self.subtitle_thread = QThread()
        self.subtitle_worker.moveToThread(self.subtitle_thread)
        self.subtitle_worker.progress.connect(self.on_subtitle_progress)
        self.subtitle_worker.finished.connect(self.on_subtitle_finished)
        self.subtitle_thread.started.connect(self.subtitle_worker.run)
        self.subtitle_worker.subtitle_updated.connect(self.update_subtitle_table)
        # 启动线程
        self.subtitle_thread.start()
        self.update_sub_generate_status(1)
        

    def on_subtitle_progress(self, msg, progress):
        #字幕生成进度回调
        print(f"字幕生成进度：{progress}% - {msg}")  
        self.subtitle_progress=progress
        self.update_circular_progress(progress)

    def on_subtitle_finished(self, success, msg):
        #字幕生成完成回调
        if success:
            QMessageBox.information(self.ui.load_pages.video_widget, "成功", msg)
        else:
            QMessageBox.warning(self.ui.load_pages.video_widget, "失败", msg)
        self.subtitle_thread.quit()
        self.subtitle_thread.wait()
        self.subtitle_worker = None
        self.subtitle_thread = None
        self.update_sub_generate_status(2)
    
    def stop_subtitle_worker(self):
        if self.subtitle_worker and self.subtitle_thread:
            self.subtitle_worker.stop()
            self.subtitle_thread.quit()
            self.subtitle_thread.wait()
            self.subtitle_worker = None
            self.subtitle_thread = None
        
        if self.temp_srt and not self.generate_subtitle_file and os.path.exists(self.temp_srt):
            clean_temp([self.temp_srt])
        self.temp_srt = None

    



        