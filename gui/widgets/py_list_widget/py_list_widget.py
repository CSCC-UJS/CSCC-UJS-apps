# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from . style import *

# IMPORT ITEM WIDGET
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_item_widget.py_item_widget import PyItemWidget

# PY LIST WIDGET
# ///////////////////////////////////////////////////////////////
class PyListWidget(QListWidget):
    def __init__(
        self, 
        radius=8,
        color="#DADBDE",
        bg_color= "#e6e7e9",
        item_bg_color="#b0b2b6",
        item_bg_hover_color="#f5f5f5",
        item_bg_selected_color="#e8f0fe",
        border_color="#ebecef",
        scroll_bar_bg_color="#f5f5f5",
        scroll_bar_btn_color="#e9eaeb",
        context_color="#BABEC0"
    ):
        super().__init__()

        # 1. 基础配置
        self.setFrameShape(QListWidget.NoFrame)
        self.setSelectionMode(QListWidget.SingleSelection)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSpacing(10)  # 条目间距
        
        # 2. 启用拖动排序
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QListWidget.InternalMove)  # 仅内部拖动

        # 3. 样式参数
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._item_bg_color = item_bg_color
        self._item_bg_hover_color = item_bg_hover_color
        self._item_bg_selected_color = item_bg_selected_color
        self._border_color = border_color
        self._scroll_bar_bg_color = scroll_bar_bg_color
        self._scroll_bar_btn_color = scroll_bar_btn_color
        self._context_color = context_color

        # SET STYLESHEET
        self.set_stylesheet(
            radius=self._radius,
            color=self._color,
            bg_color=self._bg_color,
            item_bg_color=self._item_bg_color,
            item_bg_hover_color=self._item_bg_hover_color,
            item_bg_selected_color=self._item_bg_selected_color,
            border_color=self._border_color,
            scroll_bar_bg_color=self._scroll_bar_bg_color,
            scroll_bar_btn_color=self._scroll_bar_btn_color,
            context_color=self._context_color
        )
    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        color,
        bg_color,
        item_bg_color,
        item_bg_hover_color,
        item_bg_selected_color,
        border_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style_list.format(
            _radius = radius,          
            _color = color,
            _bg_color = bg_color,
            _item_bg_color = item_bg_color,
            _item_bg_hover_color = item_bg_hover_color,
            _item_bg_selected_color = item_bg_selected_color,
            _border_color = border_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)


    # 添加单个视频条目
    def add_video_item(self, cover_path, title, author, views, duration):
        item = PyItemWidget(
            cover_path=cover_path,
            title=title,
            author=author,
            views=views,
            duration=duration,
            radius=self._radius,
            color=self._color,
            bg_color=self._item_bg_color,
            bg_hover_color=self._item_bg_hover_color,
            bg_selected_color=self._item_bg_selected_color,
            border_color=self._border_color,
            context_color=self._context_color
        )
        self.addItem(item)
        self.setItemWidget(item, item.content_widget)


















