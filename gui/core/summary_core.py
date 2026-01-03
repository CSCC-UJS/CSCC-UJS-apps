from typing import List, Dict, Any
from textrank4zh import TextRank4Sentence
from PySide6.QtCore import QObject, Signal

class Summary(QObject):
    """
    字幕文件摘要生成类
    用于将字幕文件转换为文本并生成关键句子摘要
    """
    progress = Signal(str, int)  # 进度信号：(提示文本, 进度百分比)
    finished = Signal(bool, str)  # 完成信号：(是否成功, 结果/错误信息)

    def __init__(self, sub_text: str, topK: int):
        """
        初始化摘要生成器

        :param sub_text: 字幕文本内容
        :param topK: 要提取的关键句子数量
        """
        super().__init__()
        self.subtitle_text = sub_text
        self.topK = topK
        self.is_running = True
        
        # 存储文本摘要
        self.key_sentences: List[Dict[str, Any]] = [] 

    # def swap(self) -> None:
    #     """将字幕文件转换为文本文件"""
    #     if not self.is_running:
    #         raise RuntimeError("任务已被终止")
            
    #     self.progress.emit("正在转换字幕文件...", 10)
    #     try:
    #         sub = load(self.srt_path)
    #         convert(sub, self.txt_path)
    #         self.progress.emit("字幕转换完成", 20)
    #     except Exception as e:
    #         self.finished.emit(False, f"字幕转换失败: {str(e)}")
    #         raise

    def abstract_sum(self) -> List[Dict[str, Any]]:
        """生成文本摘要，提取关键句子"""
        if not self.is_running:
            raise RuntimeError("任务已被终止")
            
        try:
            # self.progress.emit("正在读取文本文件...", 30)
            # # 安全读取文件
            # with codecs.open(self.txt_path, 'r', 'utf-8') as f:
            #     text = f.read()

            # if not text.strip():
            #     raise ValueError("转换后的文本文件为空")

            self.progress.emit("正在提取文本摘要...", 50)
            tr4s = TextRank4Sentence()
            tr4s.analyze(text=self.subtitle_text, lower=True, source='all_filters')

            self.progress.emit("正在提取文本摘要...", 70)
            self.key_sentences = tr4s.get_key_sentences(num=self.topK)
            
            self.progress.emit("摘要生成完成", 90)
            return self.key_sentences
            
        except Exception as e:
            self.finished.emit(False, f"生成摘要失败: {str(e)}")
            raise

    def run(self) -> None:
        """执行摘要生成流程"""
        self.is_running = True
        try:
            self.progress.emit("开始处理...", 0)
            
            #self.swap()
            
            self.abstract_sum()
            
            if self.is_running:
                self.finished.emit(True, "摘要生成成功！")
                self.progress.emit("任务完成", 100)
                
        except Exception as e:
            if self.is_running:
                self.finished.emit(False, f"任务执行失败: {str(e)}")
        finally:
            self.is_running = False

    def stop(self) -> None:
        """停止当前运行的任务"""
        self.is_running = False
        self.progress.emit("任务已终止", 0)
        self.finished.emit(False, "任务被用户终止")





