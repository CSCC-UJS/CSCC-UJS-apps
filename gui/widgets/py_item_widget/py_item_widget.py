# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT ITEM CONTENT
# ///////////////////////////////////////////////////////////////
from .py_item_content import VideoItemContent


# PY ITEM WIDGET
# ///////////////////////////////////////////////////////////////
class PyItemWidget(QListWidgetItem):
    def __init__(
        self, 
        cover_path, title, author, views, duration,
        radius=8, color="#333333", bg_color="#ffffff",
        bg_hover_color="#f5f5f5", bg_selected_color="#e8f0fe",
        border_color="#eee", context_color="#00ABE8"
    ):
        super().__init__()
        # 存储视频信息
        self.cover_path = cover_path
        self.title = title
        self.author = author
        self.views = views
        self.duration = duration

        # 创建内容组件
        self.content_widget = VideoItemContent(cover_path, title, author, views, duration)
        # 设置Item尺寸
        self.setSizeHint(self.content_widget.sizeHint())

        # 样式参数（仅存储，实际样式给QListWidget设置）
        self.style_params = {
            "radius": radius,
            "color": color,
            "bg_color": bg_color,
            "bg_hover_color": bg_hover_color,
            "bg_selected_color": bg_selected_color,
            "border_color": border_color,
            "context_color": context_color
        }