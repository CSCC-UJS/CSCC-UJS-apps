import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
from PySide6.QtCore import QObject, Signal
from importlib import reload
import swapsub

class summary(QObject):
    progress = Signal(str, int)
    finished = Signal(bool, str)

    def __init__(self, srt_path, txt_path, topK):
        """初始化"""
        super().__init__()
        self.srt_path = srt_path
        self.isrunning = True
        self.topK = topK
        self.txt_path = txt_path

        # 存储提取的关键字
        self.sentences = []

    def swap(self):
        """文本类型转换"""
        sub = swapsub.load(self.srt_path)  
        swapsub.convert(sub,self.txt_path)

    def abstract_sum(self):
        try:
            self.progress.emit("正在生成摘要...", 30)
            text = codecs.open(self.txt_path, 'r', 'utf-8').read()
            tr4w = TextRank4Keyword()
        
            self.progress.emit("正在生成摘要...", 50)
            tr4w.analyze(text=text, lower = True, window=2)

            self.progress.emit("正在生成摘要...", 70)
            tr4s = TextRank4Sentence()
            tr4s.analyze(text=text, lower = True, source = 'all_filters')

            self.progress.emit("正在生成摘要...", 90)
            self.sentence = tr4s.get_key_sentences(num = self.topK)
        except Exception as e:
            self.finished.emit(False, f"生成摘要失败: {str(e)}")
            raise

    def run(self):
        # 初始化
        self.__init__()

        # 文本类型转换
        self.swap()

        # 生成摘要
        self.abstract_sum()

    def stop(self):
        self.isrunning = False