# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
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



class SetupPageSettings(QObject):
    settings_update=Signal(bool,int,str,str)
    def __init__(self):
        super().__init__()
        self.whether_generate_subtitles=False
        self.font_size=24
        self.sub_place="Bottom"
        self.sub_colour="#FFFFFF"
    # SETUP PAGE_VIDEOPLAYER
    # ///////////////////////////////////////////////////////////////
    def setup_page_settings(self):
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
        # SUBTITLE SETTINGS STYLES
        self.ui.load_pages.comboBox_sub_model.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.toggle_save_subtitles.set_stylesheet(
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.comboBox_font_size.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.comboBox_sub_place.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.ui.load_pages.btn_sub_colour.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.btn_apply_setting.set_style(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.ui.load_pages.btn_sub_colour.clicked.connect(self.open_color_dialog)
        self.ui.load_pages.btn_apply_setting.clicked.connect(self.apply_settings)

    def apply_settings(self):
        self.whether_generate_subtitles=self.ui.load_pages.toggle_save_subtitles.isChecked()
        self.font_size=int(self.ui.load_pages.comboBox_font_size.currentText())
        self.sub_place=self.ui.load_pages.comboBox_sub_place.currentText()
        self.settings_update.emit(self.whether_generate_subtitles,self.font_size,self.sub_place,self.sub_colour)

    def open_color_dialog(self):
        color_dialog = QColorDialog()
        color_dialog.setWindowTitle("选择字幕颜色")
        color_dialog.setModal(True)
        
        color_dialog.setOption(QColorDialog.NoButtons, False)
        
        custom_dialog_colors = {
            "light_bg": "#2B2D31",       # 主背景：深灰
            "medium_bg": "#36393F",      # 中背景：略浅深灰（层级区分）
            "dark_bg": "#1E1F22",        # 深背景：点击态
            "border_color": "#42464D",   # 边框色：浅灰（弱化但统一）
            "text_color": "#B9BBBE",     # 文字色：浅灰（高可读性）
            "highlight_color": "#4C76D1",# 高亮色：柔和蓝（点缀）
            "white": "#E5E9F0"           # 浅灰白（按钮/选中态）
        }
        
        color_dialog_stylesheet = f"""
            /* ========== 1. 根对话框全容器覆盖（解决纯黑核心问题） ========== */
            QColorDialog,
            QColorDialog * {{  /* 强制覆盖所有子控件 */
                background-color: {custom_dialog_colors["light_bg"]};
                color: {custom_dialog_colors["text_color"]};
                border-color: {custom_dialog_colors["border_color"]};
            }}
            
            /* 对话框主容器 */
            QColorDialog {{
                border-radius: 12px;
                border: 2px solid {custom_dialog_colors["border_color"]};
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                        stop:0 {custom_dialog_colors["light_bg"]},
                                        stop:1 {custom_dialog_colors["medium_bg"]});
            }}
            
            /* 对话框标题栏 */
            QColorDialog::title {{
                background-color: {custom_dialog_colors["medium_bg"]};
                padding: 10px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                color: {custom_dialog_colors["white"]};
                font-size: 14px;
                font-weight: bold;
                border-bottom: 1px solid {custom_dialog_colors["border_color"]};
            }}
            
            /* ========== 2. 核心修复：颜色面板底层容器（解决纯黑关键） ========== */
            QColorDialog QWidget[class="QColorDialogOptionsWidget"],
            QColorDialog QWidget[objectName*="ColorPanel"],
            QColorDialog QStackedWidget,
            QColorDialog QFrame {{
                background-color: {custom_dialog_colors["medium_bg"]} !important;  /* 强制覆盖 */
                border-radius: 8px;
                padding: 8px;
                margin: 8px;
                border: 1px solid {custom_dialog_colors["border_color"]};
            }}
            
            /* ========== 3. 其他控件样式（保留原有设计） ========== */
            /* 按钮样式 */
            QPushButton {{
                background-color: {custom_dialog_colors["medium_bg"]};
                color: {custom_dialog_colors["text_color"]};
                border-radius: 8px;
                padding: 8px 18px;
                border: 1px solid {custom_dialog_colors["border_color"]};
            }}
            QPushButton:hover {{
                background-color: {QColor(custom_dialog_colors["medium_bg"]).lighter(110).name()};
                border-color: {QColor(custom_dialog_colors["highlight_color"]).lighter(110).name()};
            }}
            QPushButton:pressed {{
                background-color: {custom_dialog_colors["dark_bg"]};
            }}
            QPushButton:default {{
                background-color: {custom_dialog_colors["highlight_color"]};
                color: {custom_dialog_colors["white"]};
                border: none;
            }}
            
            /* 输入框样式 */
            QLineEdit {{
                background-color: {custom_dialog_colors["dark_bg"]};
                color: {custom_dialog_colors["white"]};
                border: 1px solid {custom_dialog_colors["border_color"]};
                border-radius: 6px;
                padding: 6px 10px;
            }}
            QLineEdit:focus {{
                border-color: {custom_dialog_colors["highlight_color"]};
                outline: none;
                background-color: {QColor(custom_dialog_colors["dark_bg"]).lighter(105).name()};
            }}
            
            /* 下拉框样式 */
            QComboBox {{
                background-color: {custom_dialog_colors["dark_bg"]};
                color: {custom_dialog_colors["text_color"]};
                border-radius: 6px;
                padding: 6px 10px;
                border: 1px solid {custom_dialog_colors["border_color"]};
            }}
            QComboBox::drop-down {{
                border: none;
                padding-right: 8px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 6px solid {custom_dialog_colors["text_color"]};
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {custom_dialog_colors["medium_bg"]};
                color: {custom_dialog_colors["text_color"]};
                border-radius: 6px;
                selection-background-color: {custom_dialog_colors["highlight_color"]};
                selection-color: {custom_dialog_colors["white"]};
                padding: 4px;
                border: 1px solid {custom_dialog_colors["border_color"]};
            }}
            
            /* 滑块样式 */
            QSlider::groove:horizontal {{
                background-color: {custom_dialog_colors["medium_bg"]};
                height: 8px;
                border-radius: 4px;
                border: 1px solid {custom_dialog_colors["border_color"]};
            }}
            QSlider::handle:horizontal {{
                background-color: {custom_dialog_colors["highlight_color"]};
                width: 18px;
                height: 18px;
                margin: -5px 0;
                border-radius: 9px;
                border: 2px solid {custom_dialog_colors["light_bg"]};
            }}
            QSlider::sub-page:horizontal {{
                background-color: {custom_dialog_colors["highlight_color"]};
                border-radius: 4px;
            }}
            
            /* 颜色预览框 */
            QFrame[objectName*="ColorPreview"] {{
                border: 2px solid {custom_dialog_colors["border_color"]};
                border-radius: 6px;
                background-color: {custom_dialog_colors["white"]};
            }}
            
            /* 颜色网格按钮 */
            QColorPicker {{
                border-radius: 4px;
                margin: 1px;
                border: 1px solid {custom_dialog_colors["border_color"]};
                background-color: transparent !important;
            }}
            QColorPicker:hover {{
                border: 2px solid {custom_dialog_colors["highlight_color"]};
                margin: 0px;
            }}
            
            /* 标签样式 */
            QLabel {{
                color: {custom_dialog_colors["text_color"]};
                font-size: 13px;
                padding: 4px;
            }}
            
            /* 分组框样式 */
            QGroupBox {{
                border: 1px solid {custom_dialog_colors["border_color"]};
                border-radius: 8px;
                margin-top: 8px;
                padding-top: 10px;
                color: {custom_dialog_colors["text_color"]};
                font-weight: medium;
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 8px 0 8px;
                color: {QColor(custom_dialog_colors["text_color"]).lighter(110).name()};
            }}
        """
        color_dialog.setStyleSheet(color_dialog_stylesheet)
        
        color_dialog.setAttribute(Qt.WA_StyledBackground, True)
        color_dialog.update()
        
        if color_dialog.exec_():  
            selected_color = color_dialog.selectedColor()
        if selected_color.isValid(): 
            self.update_color_button_style(selected_color)
            self.sub_colour=selected_color.name()
    def update_color_button_style(self, color):
        self.ui.load_pages.btn_sub_colour.set_bg_color(color.name())
        self.ui.load_pages.btn_sub_colour.set_bg_hover_color(color.lighter(120).name())
        self.ui.load_pages.btn_sub_colour.set_bg_pressed_color(color.darker(120).name())