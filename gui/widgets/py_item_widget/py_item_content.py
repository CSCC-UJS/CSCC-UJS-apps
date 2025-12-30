# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

class VideoItemContent(QWidget):
    def __init__(self, cover_path, title, author, views, duration, parent=None):
        super().__init__(parent)
        self.setFixedHeight(80)
        self.setMinimumWidth(300)

        # 封面标签
        self.cover_label = QLabel()
        self.cover_label.setFixedSize(120, 70)
        self.cover_label.setStyleSheet("border-radius: 4px; background-color: #f0f0f0;")
        self.cover_label.setAlignment(Qt.AlignCenter)
        if cover_path:
            pixmap = QPixmap(cover_path)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(120, 70, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.cover_label.setPixmap(pixmap)
            else:
                self.cover_label.setText("暂无封面")

        # 信息布局
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(10, 0, 0, 0)
        info_layout.setSpacing(2)

        # 标题（限制2行+省略号）
        self.title_label = QLabel(title or "无标题")
        self.title_label.setStyleSheet("font-size: 14px; color: #333;")
        self.title_label.setWordWrap(True)

        # 作者/播放量/时长
        info_text = f"{author or '未知作者'} • {views or '0次播放'} • {duration or '00:00'}"
        self.info_label = QLabel(info_text)
        self.info_label.setStyleSheet("font-size: 12px; color: #999;")

        info_layout.addWidget(self.title_label)
        info_layout.addWidget(self.info_label)
        info_layout.addStretch()

        # 主布局
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.addWidget(self.cover_label)
        main_layout.addLayout(info_layout)
        main_layout.addStretch()