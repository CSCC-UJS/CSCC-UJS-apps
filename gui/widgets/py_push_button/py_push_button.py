# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''

# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
        self, 
        parent=None,
        text="",  
        radius=8, 
        color="#FFFFFF", 
        bg_color="#282828",  
        bg_color_hover="#383838", 
        bg_color_pressed="#181818" 
    ):
        super().__init__()

        # 保存样式参数
        self._radius = radius
        self._color = color
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed

        # SET PARAMETRES
        self.setText(text)
        if parent is not None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # 初始化样式
        self.update_style()

    def update_style(self):
        """更新按钮样式"""
        custom_style = style.format(
            _color=self._color,
            _radius=self._radius,
            _bg_color=self._bg_color,
            _bg_color_hover=self._bg_color_hover,
            _bg_color_pressed=self._bg_color_pressed
        )
        self.setStyleSheet(custom_style)

    # 设置文本颜色
    def set_text_color(self, color):
        self._color = color
        self.update_style()

    # 设置圆角半径
    def set_radius(self, radius):
        self._radius = radius
        self.update_style()

    # 设置默认背景色
    def set_bg_color(self, color):
        self._bg_color = color
        self.update_style()

    # 设置悬浮背景色
    def set_bg_hover_color(self, color):
        self._bg_color_hover = color
        self.update_style()

    # 设置按下背景色
    def set_bg_pressed_color(self, color):
        self._bg_color_pressed = color
        self.update_style()

    # 批量修改样式
    def set_style(
        self, 
        radius=None, 
        color=None, 
        bg_color=None, 
        bg_color_hover=None, 
        bg_color_pressed=None
    ):
        """
        批量修改样式属性
        :param radius: 圆角半径
        :param color: 文本颜色
        :param bg_color: 默认背景色
        :param bg_color_hover: 悬浮背景色
        :param bg_color_pressed: 按下背景色
        """
        if radius is not None:
            self._radius = radius
        if color is not None:
            self._color = color
        if bg_color is not None:
            self._bg_color = bg_color
        if bg_color_hover is not None:
            self._bg_color_hover = bg_color_hover
        if bg_color_pressed is not None:
            self._bg_color_pressed = bg_color_pressed
        
        self.update_style()

    # 获取当前样式参数
    def get_style_params(self):
        """返回当前所有样式参数"""
        return {
            'radius': self._radius,
            'color': self._color,
            'bg_color': self._bg_color,
            'bg_color_hover': self._bg_color_hover,
            'bg_color_pressed': self._bg_color_pressed
        }

# # IMPORT QT CORE
# # ///////////////////////////////////////////////////////////////
# from qt_core import *

# # IMPORT THEME COLORS
# # ///////////////////////////////////////////////////////////////
# from gui.core.json_themes import Themes

# # STYLE
# # ///////////////////////////////////////////////////////////////
# style = '''
# QPushButton {{
# 	border: none;
#     padding-left: 10px;
#     padding-right: 5px;
#     color: {_color};
# 	border-radius: {_radius};	
# 	background-color: {_bg_color};
# }}
# QPushButton:hover {{
# 	background-color: {_bg_color_hover};
# }}
# QPushButton:pressed {{	
# 	background-color: {_bg_color_pressed};
# }}
# '''

# # PY PUSH BUTTON
# # ///////////////////////////////////////////////////////////////
# class PyPushButton(QPushButton):
#     def __init__(
#         self, 
#         parent=None,
#         text="",  
#         radius=8, 
#         color="#FFFFFF", 
#         bg_color="#282828",  
#         bg_color_hover="#383838", 
#         bg_color_pressed="#181818" 
#     ):
#         super().__init__()

#         # SET PARAMETRES
#         self.setText(text)
#         if parent != None:
#             self.setParent(parent)
#         self.setCursor(Qt.PointingHandCursor)

#         # SET STYLESHEET
#         custom_style = style.format(
#             _color = color,
#             _radius = radius,
#             _bg_color = bg_color,
#             _bg_color_hover = bg_color_hover,
#             _bg_color_pressed = bg_color_pressed
#         )
#         self.setStyleSheet(custom_style)

        