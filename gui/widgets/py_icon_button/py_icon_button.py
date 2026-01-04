# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# PY TITLE BUTTON
# ///////////////////////////////////////////////////////////////
class PyIconButton(QPushButton):
    def __init__(
        self,
        parent = None,
        icon_path = None,
        app_parent = None,
        tooltip_text = "",
        btn_id = None,
        width = 40,          # 适配UI中设置的40x40最小尺寸
        height = 40,
        radius = 8,
        bg_color = "#343b48",
        bg_color_hover = "#3c4454",
        bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        dark_one = "#1b1e23",
        text_foreground = "#8a95aa",
        context_color = "#568af2",
        top_margin = 40,
        is_active = False
    ):
        super().__init__(parent)
        
        # SET DEFAULT PARAMETERS - 适配UI文件中直接实例化的场景
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)
        if btn_id:
            self.setObjectName(btn_id)
        # 清除默认文本（UI中设置为空文本）
        self.setText("")

        # PROPERTIES
        self._bg_color = bg_color
        self._bg_color_hover = bg_color_hover
        self._bg_color_pressed = bg_color_pressed        
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._context_color = context_color
        self._top_margin = top_margin
        self._is_active = is_active
        
        # Set Parameters
        self._set_bg_color = bg_color
        self._set_icon_path = icon_path
        self._set_icon_color = icon_color
        self._set_border_radius = radius
        
        # Parent
        self._parent = parent if parent else self
        self._app_parent = app_parent if app_parent else self.parentWidget()

        # TOOLTIP - 兼容无父组件的情况
        self._tooltip_text = tooltip_text
        self._tooltip = None
        if self._app_parent and tooltip_text:
            self._tooltip = _ToolTip(
                self._app_parent,
                tooltip_text,
                dark_one,
                text_foreground
            )
            self._tooltip.hide()

    # SET ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def set_active(self, is_active):
        self._is_active = is_active
        self.repaint()

    # RETURN IF IS ACTIVE MENU
    # ///////////////////////////////////////////////////////////////
    def is_active(self):
        return self._is_active

    # PAINT EVENT
    # painting the button and the icon
    # ///////////////////////////////////////////////////////////////
    def paintEvent(self, event):
        # PAINTER
        paint = QPainter(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # 绘制背景
        if self._is_active:
            brush = QBrush(QColor(self._context_color))
        else:
            brush = QBrush(QColor(self._set_bg_color))

        # 创建圆角矩形路径（防止样式冲突）
        path = QPainterPath()
        rect = QRect(0, 0, self.width(), self.height())
        path.addRoundedRect(rect, self._set_border_radius, self._set_border_radius)
        
        paint.setPen(Qt.NoPen)
        paint.setBrush(brush)
        paint.drawPath(path)

        # 绘制图标（兼容无图标路径的情况）
        if self._set_icon_path:
            self.icon_paint(paint, self._set_icon_path, rect)

        # END PAINTER
        paint.end()

    # CHANGE STYLES
    # Functions with custom styles
    # ///////////////////////////////////////////////////////////////
    def change_style(self, event):
        if event == QEvent.Enter:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
        elif event == QEvent.Leave:
            self._set_bg_color = self._bg_color
            self._set_icon_color = self._icon_color
        elif event == QEvent.MouseButtonPress:            
            self._set_bg_color = self._bg_color_pressed
            self._set_icon_color = self._icon_color_pressed
        elif event == QEvent.MouseButtonRelease:
            self._set_bg_color = self._bg_color_hover
            self._set_icon_color = self._icon_color_hover
        self.repaint()

    # MOUSE OVER
    # Event triggered when the mouse is over the BTN
    # ///////////////////////////////////////////////////////////////
    def enterEvent(self, event):
        self.change_style(QEvent.Enter)
        if self._tooltip:
            self.move_tooltip()
            self._tooltip.show()

    # MOUSE LEAVE
    # Event fired when the mouse leaves the BTN
    # ///////////////////////////////////////////////////////////////
    def leaveEvent(self, event):
        self.change_style(QEvent.Leave)
        if self._tooltip:
            self._tooltip.hide()

    # MOUSE PRESS
    # Event triggered when the left button is pressed
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonPress)
            self.setFocus()
            self.clicked.emit()

    # MOUSE RELEASED
    # Event triggered after the mouse button is released
    # ///////////////////////////////////////////////////////////////
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.change_style(QEvent.MouseButtonRelease)
            self.released.emit()

    # DRAW ICON WITH COLORS
    # ///////////////////////////////////////////////////////////////
    def icon_paint(self, qp, image, rect):
        try:
            icon = QPixmap(image)
            if icon.isNull():
                return
            
            painter = QPainter(icon)
            painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
            
            if self._is_active:
                painter.fillRect(icon.rect(), QColor(self._icon_color_active))
            else:
                painter.fillRect(icon.rect(), QColor(self._set_icon_color))
            
            # 居中绘制图标
            x = (rect.width() - icon.width()) // 2
            y = (rect.height() - icon.height()) // 2
            qp.drawPixmap(x, y, icon)        
            painter.end()
        except Exception:
            # 兼容图标加载失败的情况
            pass

    # SET ICON
    # ///////////////////////////////////////////////////////////////
    def set_icon(self, icon_path):
        self._set_icon_path = icon_path
        self.repaint()

    # MOVE TOOLTIP
    # ///////////////////////////////////////////////////////////////
    def move_tooltip(self):
        if not self._tooltip or not self._parent:
            return
            
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSITION
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2)
        pos_y = pos.y() - self._top_margin

        # SET POSITION TO WIDGET
        self._tooltip.move(pos_x, pos_y)

    # ========== 新增样式修改函数 ==========
    # 修改背景色（普通/悬浮/按下状态）
    # ///////////////////////////////////////////////////////////////
    def set_background_colors(self, normal=None, hover=None, pressed=None):
        """
        修改按钮背景色
        :param normal: 普通状态背景色 (str, 如 "#343b48")
        :param hover: 悬浮状态背景色 (str)
        :param pressed: 按下状态背景色 (str)
        """
        if normal:
            self._bg_color = normal
            # 如果当前不是悬浮/按下状态，立即更新显示的背景色
            if self._set_bg_color in (self._bg_color, self._bg_color_hover, self._bg_color_pressed):
                self._set_bg_color = normal
        if hover:
            self._bg_color_hover = hover
        if pressed:
            self._bg_color_pressed = pressed
        self.repaint()

    # 修改图标颜色（普通/悬浮/按下/激活状态）
    # ///////////////////////////////////////////////////////////////
    def set_icon_colors(self, normal=None, hover=None, pressed=None, active=None):
        """
        修改图标颜色
        :param normal: 普通状态图标色 (str)
        :param hover: 悬浮状态图标色 (str)
        :param pressed: 按下状态图标色 (str)
        :param active: 激活状态图标色 (str)
        """
        if normal:
            self._icon_color = normal
            # 如果当前不是悬浮/按下状态，立即更新显示的图标色
            if self._set_icon_color in (self._icon_color, self._icon_color_hover, self._icon_color_pressed):
                self._set_icon_color = normal
        if hover:
            self._icon_color_hover = hover
        if pressed:
            self._icon_color_pressed = pressed
        if active:
            self._icon_color_active = active
        self.repaint()

    # 修改按钮圆角
    # ///////////////////////////////////////////////////////////////
    def set_border_radius(self, radius):
        """
        修改按钮圆角半径
        :param radius: 圆角半径 (int)
        """
        self._set_border_radius = radius
        self.repaint()

    # 修改按钮尺寸
    # ///////////////////////////////////////////////////////////////
    def set_button_size(self, width, height):
        """
        修改按钮固定尺寸
        :param width: 宽度 (int)
        :param height: 高度 (int)
        """
        self.setFixedSize(width, height)
        self.repaint()

    # 修改激活状态的上下文颜色
    # ///////////////////////////////////////////////////////////////
    def set_context_color(self, color):
        """
        修改激活状态的背景色
        :param color: 上下文颜色 (str)
        """
        self._context_color = color
        if self._is_active:
            self.repaint()

    # 修改tooltip相关样式
    # ///////////////////////////////////////////////////////////////
    def update_tooltip(self, new_text=None, dark_one=None, text_foreground=None):
        """
        更新tooltip文本或样式
        :param new_text: 新的tooltip文本 (str)
        :param dark_one: tooltip背景色 (str)
        :param text_foreground: tooltip文字色 (str)
        """
        if not self._tooltip:
            return
        
        # 更新文本
        if new_text:
            self._tooltip_text = new_text
            self._tooltip.setText(new_text)
            self._tooltip.adjustSize()
        
        # 更新样式
        if dark_one or text_foreground:
            current_dark = self._tooltip.style_tooltip.split("{_dark_one}")[0].split(":")[-1].strip() if not dark_one else dark_one
            current_text = self._tooltip.style_tooltip.split("{_text_foreground}")[0].split(":")[-1].strip() if not text_foreground else text_foreground
            
            style = self._tooltip.style_tooltip.format(
                _dark_one = dark_one or current_dark,
                _text_foreground = text_foreground or current_text
            )
            self._tooltip.setStyleSheet(style)

# TOOLTIP
# ///////////////////////////////////////////////////////////////
class _ToolTip(QLabel):
    # TOOLTIP / LABEL StyleSheet
    style_tooltip = """ 
    QLabel {{		
        background-color: {_dark_one};	
        color: {_text_foreground};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
        font: 800 9pt "Noto Sans, Microsoft YaHei, SimSun, Arial, sans-serif";
    }}
    """
    def __init__(
        self,
        parent, 
        tooltip,
        dark_one,
        text_foreground
    ):
        super().__init__(parent)

        # LABEL SETUP
        style = self.style_tooltip.format(
            _dark_one = dark_one,
            _text_foreground = text_foreground
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setText(tooltip)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)


# # IMPORT QT CORE
# # ///////////////////////////////////////////////////////////////
# from qt_core import *

# # PY TITLE BUTTON
# # ///////////////////////////////////////////////////////////////
# class PyIconButton(QPushButton):
#     def __init__(
#         self,
#         icon_path = None,
#         parent = None,
#         app_parent = None,
#         tooltip_text = "",
#         btn_id = None,
#         width = 30,
#         height = 30,
#         radius = 8,
#         bg_color = "#343b48",
#         bg_color_hover = "#3c4454",
#         bg_color_pressed = "#2c313c",
#         icon_color = "#c3ccdf",
#         icon_color_hover = "#dce1ec",
#         icon_color_pressed = "#edf0f5",
#         icon_color_active = "#f5f6f9",
#         dark_one = "#1b1e23",
#         text_foreground = "#8a95aa",
#         context_color = "#568af2",
#         top_margin = 40,
#         is_active = False
#     ):
#         super().__init__()
        
#         # SET DEFAULT PARAMETERS
#         self.setFixedSize(width, height)
#         self.setCursor(Qt.PointingHandCursor)
#         self.setObjectName(btn_id)

#         # PROPERTIES
#         self._bg_color = bg_color
#         self._bg_color_hover = bg_color_hover
#         self._bg_color_pressed = bg_color_pressed        
#         self._icon_color = icon_color
#         self._icon_color_hover = icon_color_hover
#         self._icon_color_pressed = icon_color_pressed
#         self._icon_color_active = icon_color_active
#         self._context_color = context_color
#         self._top_margin = top_margin
#         self._is_active = is_active
#         # Set Parameters
#         self._set_bg_color = bg_color
#         self._set_icon_path = icon_path
#         self._set_icon_color = icon_color
#         self._set_border_radius = radius
#         # Parent
#         self._parent = parent
#         self._app_parent = app_parent

#         # TOOLTIP
#         self._tooltip_text = tooltip_text
#         self._tooltip = _ToolTip(
#             app_parent,
#             tooltip_text,
#             dark_one,
#             text_foreground
#         )
#         self._tooltip.hide()

#     # SET ACTIVE MENU
#     # ///////////////////////////////////////////////////////////////
#     def set_active(self, is_active):
#         self._is_active = is_active
#         self.repaint()

#     # RETURN IF IS ACTIVE MENU
#     # ///////////////////////////////////////////////////////////////
#     def is_active(self):
#         return self._is_active

#     # PAINT EVENT
#     # painting the button and the icon
#     # ///////////////////////////////////////////////////////////////
#     def paintEvent(self, event):
#         # PAINTER
#         paint = QPainter()
#         paint.begin(self)
#         paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        
#         if self._is_active:
#             # BRUSH
#             brush = QBrush(QColor(self._context_color))
#         else:
#             # BRUSH
#             brush = QBrush(QColor(self._set_bg_color))

#         # CREATE RECTANGLE
#         rect = QRect(0, 0, self.width(), self.height())
#         paint.setPen(Qt.NoPen)
#         paint.setBrush(brush)
#         paint.drawRoundedRect(
#             rect, 
#             self._set_border_radius, 
#             self._set_border_radius
#         )

#         # DRAW ICONS
#         self.icon_paint(paint, self._set_icon_path, rect)

#         # END PAINTER
#         paint.end()

#     # CHANGE STYLES
#     # Functions with custom styles
#     # ///////////////////////////////////////////////////////////////
#     def change_style(self, event):
#         if event == QEvent.Enter:
#             self._set_bg_color = self._bg_color_hover
#             self._set_icon_color = self._icon_color_hover
#             self.repaint()         
#         elif event == QEvent.Leave:
#             self._set_bg_color = self._bg_color
#             self._set_icon_color = self._icon_color
#             self.repaint()
#         elif event == QEvent.MouseButtonPress:            
#             self._set_bg_color = self._bg_color_pressed
#             self._set_icon_color = self._icon_color_pressed
#             self.repaint()
#         elif event == QEvent.MouseButtonRelease:
#             self._set_bg_color = self._bg_color_hover
#             self._set_icon_color = self._icon_color_hover
#             self.repaint()

#     # MOUSE OVER
#     # Event triggered when the mouse is over the BTN
#     # ///////////////////////////////////////////////////////////////
#     def enterEvent(self, event):
#         self.change_style(QEvent.Enter)
#         self.move_tooltip()
#         self._tooltip.show()

#     # MOUSE LEAVE
#     # Event fired when the mouse leaves the BTN
#     # ///////////////////////////////////////////////////////////////
#     def leaveEvent(self, event):
#         self.change_style(QEvent.Leave)
#         self.move_tooltip()
#         self._tooltip.hide()

#     # MOUSE PRESS
#     # Event triggered when the left button is pressed
#     # ///////////////////////////////////////////////////////////////
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.change_style(QEvent.MouseButtonPress)
#             # SET FOCUS
#             self.setFocus()
#             # EMIT SIGNAL
#             return self.clicked.emit()

#     # MOUSE RELEASED
#     # Event triggered after the mouse button is released
#     # ///////////////////////////////////////////////////////////////
#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.change_style(QEvent.MouseButtonRelease)
#             # EMIT SIGNAL
#             return self.released.emit()

#     # DRAW ICON WITH COLORS
#     # ///////////////////////////////////////////////////////////////
#     def icon_paint(self, qp, image, rect):
#         icon = QPixmap(image)
#         painter = QPainter(icon)
#         painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
#         if self._is_active:
#             painter.fillRect(icon.rect(), self._icon_color_active)
#         else:
#             painter.fillRect(icon.rect(), self._set_icon_color)
#         qp.drawPixmap(
#             (rect.width() - icon.width()) / 2, 
#             (rect.height() - icon.height()) / 2,
#             icon
#         )        
#         painter.end()

#     # SET ICON
#     # ///////////////////////////////////////////////////////////////
#     def set_icon(self, icon_path):
#         self._set_icon_path = icon_path
#         self.repaint()

#     # MOVE TOOLTIP
#     # ///////////////////////////////////////////////////////////////
#     def move_tooltip(self):
#         # GET MAIN WINDOW PARENT
#         gp = self.mapToGlobal(QPoint(0, 0))

#         # SET WIDGET TO GET POSTION
#         # Return absolute position of widget inside app
#         pos = self._parent.mapFromGlobal(gp)

#         # FORMAT POSITION
#         # Adjust tooltip position with offset
#         pos_x = (pos.x() - (self._tooltip.width() // 2)) + (self.width() // 2)
#         pos_y = pos.y() - self._top_margin

#         # SET POSITION TO WIDGET
#         # Move tooltip position
#         self._tooltip.move(pos_x, pos_y)

# # TOOLTIP
# # ///////////////////////////////////////////////////////////////
# class _ToolTip(QLabel):
#     # TOOLTIP / LABEL StyleSheet
#     style_tooltip = """ 
#     QLabel {{		
#         background-color: {_dark_one};	
#         color: {_text_foreground};
#         padding-left: 10px;
#         padding-right: 10px;
#         border-radius: 17px;
#         border: 0px solid transparent;
#         font: 800 9pt "Segoe UI";
#     }}
#     """
#     def __init__(
#         self,
#         parent, 
#         tooltip,
#         dark_one,
#         text_foreground
#     ):
#         QLabel.__init__(self)

#         # LABEL SETUP
#         style = self.style_tooltip.format(
#             _dark_one = dark_one,
#             _text_foreground = text_foreground
#         )
#         self.setObjectName(u"label_tooltip")
#         self.setStyleSheet(style)
#         self.setMinimumHeight(34)
#         self.setParent(parent)
#         self.setText(tooltip)
#         self.adjustSize()

#         # SET DROP SHADOW
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(30)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(0, 0, 0, 80))
#         self.setGraphicsEffect(self.shadow)
