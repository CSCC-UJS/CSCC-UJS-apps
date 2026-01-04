# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

from gui.widgets.py_combobox.py_combobox import PyComboBox
from gui.widgets.py_icon_button.py_icon_button import PyIconButton
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit
from gui.widgets.py_plain_text_edit.py_plain_text_edit import PyPlainTextEdit
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_slider.py_slider import PySlider
from gui.widgets.py_toggle.py_toggle import PyToggle

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(895, 697)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"font-size: 14pt")
        self.horizontalLayout_21 = QHBoxLayout(self.page_home)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_home)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(400, 300))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.Shape.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Shadow.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(400, 240))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignTop)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.horizontalLayout_21.addWidget(self.welcome_base)

        self.pages.addWidget(self.page_home)
        self.page_videoplayer = QWidget()
        self.page_videoplayer.setObjectName(u"page_videoplayer")
        self.page_videoplayer.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.page_videoplayer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.video_widget = QWidget(self.page_videoplayer)
        self.video_widget.setObjectName(u"video_widget")
        self.video_widget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 500 15pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.video_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_3.addWidget(self.video_widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prev_btn = PyIconButton(self.page_videoplayer)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setMinimumSize(QSize(40, 40))
        self.prev_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.prev_btn)

        self.stop_btn = PyIconButton(self.page_videoplayer)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(40, 40))
        self.stop_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.stop_btn)

        self.next_btn = PyIconButton(self.page_videoplayer)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(40, 40))
        self.next_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.next_btn)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.progressbar = PySlider(self.page_videoplayer)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.progressbar)

        self.progress_label = QLabel(self.page_videoplayer)
        self.progress_label.setObjectName(u"progress_label")
        self.progress_label.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.progress_label)

        self.comboBox_speed = PyComboBox(self.page_videoplayer)
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.setObjectName(u"comboBox_speed")
        self.comboBox_speed.setMinimumSize(QSize(50, 40))
        font = QFont()
        font.setPointSize(14)
        self.comboBox_speed.setFont(font)

        self.horizontalLayout_2.addWidget(self.comboBox_speed)

        self.volume_btn = PyIconButton(self.page_videoplayer)
        self.volume_btn.setObjectName(u"volume_btn")
        self.volume_btn.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.volume_btn)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(3, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 11)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.pages.addWidget(self.page_videoplayer)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_2 = QVBoxLayout(self.page_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.groupBox_5 = QGroupBox(self.page_settings)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid rgb(130, 130, 130);\n"
"    padding-top: 10px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    padding-bottom: 8px;\n"
"	font: 14pt \"JetBrains Mono\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(250, 30))
        self.label_21.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_21)

        self.comboBox_sub_model = PyComboBox(self.groupBox_5)
        self.comboBox_sub_model.addItem("")
        self.comboBox_sub_model.addItem("")
        self.comboBox_sub_model.setObjectName(u"comboBox_sub_model")
        self.comboBox_sub_model.setMinimumSize(QSize(0, 30))
        self.comboBox_sub_model.setFont(font)

        self.horizontalLayout_5.addWidget(self.comboBox_sub_model)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_23)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(250, 30))
        self.label_22.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_22)

        self.toggle_save_subtitles = PyToggle(self.groupBox_5)
        self.toggle_save_subtitles.setObjectName(u"toggle_save_subtitles")

        self.horizontalLayout_6.addWidget(self.toggle_save_subtitles)

        self.horizontalSpacer_24 = QSpacerItem(200, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_24)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(250, 30))
        self.label_24.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_24)

        self.comboBox_sub_place = PyComboBox(self.groupBox_5)
        self.comboBox_sub_place.addItem("")
        self.comboBox_sub_place.addItem("")
        self.comboBox_sub_place.setObjectName(u"comboBox_sub_place")
        self.comboBox_sub_place.setMinimumSize(QSize(100, 30))
        self.comboBox_sub_place.setFont(font)

        self.horizontalLayout_7.addWidget(self.comboBox_sub_place)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_26)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(250, 30))
        self.label_25.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_25)

        self.btn_sub_colour = PyPushButton(self.groupBox_5)
        self.btn_sub_colour.setObjectName(u"btn_sub_colour")
        self.btn_sub_colour.setMinimumSize(QSize(100, 40))

        self.horizontalLayout_8.addWidget(self.btn_sub_colour)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_27)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(250, 30))
        self.label_26.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_26)

        self.comboBox_font_size = PyComboBox(self.groupBox_5)
        self.comboBox_font_size.addItem("")
        self.comboBox_font_size.addItem("")
        self.comboBox_font_size.addItem("")
        self.comboBox_font_size.addItem("")
        self.comboBox_font_size.addItem("")
        self.comboBox_font_size.addItem("")
        self.comboBox_font_size.setObjectName(u"comboBox_font_size")
        self.comboBox_font_size.setMinimumSize(QSize(0, 30))
        self.comboBox_font_size.setFont(font)

        self.horizontalLayout_11.addWidget(self.comboBox_font_size)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_28)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer)

        self.btn_apply_setting = PyPushButton(self.groupBox_5)
        self.btn_apply_setting.setObjectName(u"btn_apply_setting")
        self.btn_apply_setting.setMinimumSize(QSize(100, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_apply_setting.setFont(font1)

        self.horizontalLayout_17.addWidget(self.btn_apply_setting)


        self.verticalLayout.addLayout(self.horizontalLayout_17)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.verticalLayout_9.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pages.addWidget(self.page_settings)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        self.verticalLayout_13 = QVBoxLayout(self.page_tools)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_7 = QLabel(self.page_tools)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_7)

        self.line_file = PyLineEdit(self.page_tools)
        self.line_file.setObjectName(u"line_file")
        self.line_file.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_15.addWidget(self.line_file)

        self.btn_file = PyPushButton(self.page_tools)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setMinimumSize(QSize(150, 30))
        self.btn_file.setFont(font1)

        self.horizontalLayout_15.addWidget(self.btn_file)

        self.horizontalLayout_15.setStretch(1, 6)

        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_start_sub = PyPushButton(self.page_tools)
        self.btn_start_sub.setObjectName(u"btn_start_sub")
        self.btn_start_sub.setMinimumSize(QSize(0, 30))

        self.verticalLayout_8.addWidget(self.btn_start_sub)

        self.btn_save_sub = PyPushButton(self.page_tools)
        self.btn_save_sub.setObjectName(u"btn_save_sub")
        self.btn_save_sub.setMinimumSize(QSize(0, 30))

        self.verticalLayout_8.addWidget(self.btn_save_sub)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.page_tools)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.toggle_edit = PyToggle(self.page_tools)
        self.toggle_edit.setObjectName(u"toggle_edit")

        self.horizontalLayout_10.addWidget(self.toggle_edit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.layout_circular_bar = QVBoxLayout()
        self.layout_circular_bar.setObjectName(u"layout_circular_bar")

        self.verticalLayout_8.addLayout(self.layout_circular_bar)

        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 3)

        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_3 = QLabel(self.page_tools)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_3)

        self.layout_subtitle_table = QVBoxLayout()
        self.layout_subtitle_table.setObjectName(u"layout_subtitle_table")

        self.verticalLayout_11.addLayout(self.layout_subtitle_table)

        self.verticalLayout_11.setStretch(1, 4)

        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 4)

        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.page_tools)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.page_tools)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_15)

        self.comboBox_keynum = PyComboBox(self.page_tools)
        self.comboBox_keynum.addItem("")
        self.comboBox_keynum.addItem("")
        self.comboBox_keynum.addItem("")
        self.comboBox_keynum.addItem("")
        self.comboBox_keynum.setObjectName(u"comboBox_keynum")
        self.comboBox_keynum.setMinimumSize(QSize(150, 30))
        self.comboBox_keynum.setFont(font1)

        self.horizontalLayout_20.addWidget(self.comboBox_keynum)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_20)

        self.btn_keyword = PyPushButton(self.page_tools)
        self.btn_keyword.setObjectName(u"btn_keyword")
        self.btn_keyword.setMinimumSize(QSize(150, 30))
        self.btn_keyword.setFont(font1)

        self.horizontalLayout_12.addWidget(self.btn_keyword)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_3 = PyPushButton(self.page_tools)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 40))
        self.pushButton_3.setMaximumSize(QSize(100, 40))
        self.pushButton_3.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_7 = PyPushButton(self.page_tools)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(100, 40))
        self.pushButton_7.setMaximumSize(QSize(100, 40))
        self.pushButton_7.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_8 = PyPushButton(self.page_tools)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(100, 40))
        self.pushButton_8.setMaximumSize(QSize(100, 40))
        self.pushButton_8.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.pushButton_4 = PyPushButton(self.page_tools)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 40))
        self.pushButton_4.setMaximumSize(QSize(100, 40))
        self.pushButton_4.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_10 = PyPushButton(self.page_tools)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(100, 40))
        self.pushButton_10.setMaximumSize(QSize(100, 40))
        self.pushButton_10.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_10, 1, 4, 1, 1)

        self.pushButton_2 = PyPushButton(self.page_tools)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 40))
        self.pushButton_2.setMaximumSize(QSize(100, 40))
        self.pushButton_2.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_9 = PyPushButton(self.page_tools)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 40))
        self.pushButton_9.setMaximumSize(QSize(100, 40))
        self.pushButton_9.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_5 = PyPushButton(self.page_tools)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 40))
        self.pushButton_5.setMaximumSize(QSize(100, 40))
        self.pushButton_5.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.pushButton_1 = PyPushButton(self.page_tools)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(100, 40))
        self.pushButton_1.setMaximumSize(QSize(100, 40))
        self.pushButton_1.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_6 = PyPushButton(self.page_tools)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(100, 40))
        self.pushButton_6.setMaximumSize(QSize(100, 40))
        self.pushButton_6.setStyleSheet(u"font: 14pt \"JetBrains Mono\";")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_13)


        self.verticalLayout_5.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.page_tools)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_11 = QLabel(self.page_tools)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.label_11)

        self.comboBox_topK = PyComboBox(self.page_tools)
        self.comboBox_topK.addItem("")
        self.comboBox_topK.addItem("")
        self.comboBox_topK.addItem("")
        self.comboBox_topK.addItem("")
        self.comboBox_topK.addItem("")
        self.comboBox_topK.setObjectName(u"comboBox_topK")
        self.comboBox_topK.setMinimumSize(QSize(150, 30))
        self.comboBox_topK.setFont(font1)

        self.horizontalLayout_19.addWidget(self.comboBox_topK)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_19)

        self.btn_summary = PyPushButton(self.page_tools)
        self.btn_summary.setObjectName(u"btn_summary")
        self.btn_summary.setMinimumSize(QSize(150, 30))
        self.btn_summary.setFont(font1)

        self.horizontalLayout_14.addWidget(self.btn_summary)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.plainTextEdit = PyPlainTextEdit(self.page_tools)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_12.addWidget(self.plainTextEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_12)


        self.verticalLayout_13.addLayout(self.verticalLayout_5)

        self.pages.addWidget(self.page_tools)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"CSCC-UJS-Apps", None))
        self.prev_btn.setText("")
        self.stop_btn.setText("")
        self.next_btn.setText("")
        self.progress_label.setText(QCoreApplication.translate("MainPages", u"00:00", None))
        self.comboBox_speed.setItemText(0, QCoreApplication.translate("MainPages", u"\u500d\u901f\uff1a0.5x", None))
        self.comboBox_speed.setItemText(1, QCoreApplication.translate("MainPages", u"\u500d\u901f\uff1a0.75x", None))
        self.comboBox_speed.setItemText(2, QCoreApplication.translate("MainPages", u"\u500d\u901f\uff1a1x", None))
        self.comboBox_speed.setItemText(3, QCoreApplication.translate("MainPages", u"\u500d\u901f\uff1a1.25x", None))
        self.comboBox_speed.setItemText(4, QCoreApplication.translate("MainPages", u"\u500d\u901f\uff1a1.5x", None))
        self.comboBox_speed.setItemText(5, QCoreApplication.translate("MainPages", u"\u500d\u901f\uff1a2x", None))

        self.volume_btn.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainPages", u"\u5b57\u5e55\u8bbe\u7f6e", None))
        self.label_21.setText(QCoreApplication.translate("MainPages", u"\u5b57\u5e55\u751f\u6210\u6a21\u578b    ", None))
        self.comboBox_sub_model.setItemText(0, QCoreApplication.translate("MainPages", u"funasr(\u63a8\u8350\uff09", None))
        self.comboBox_sub_model.setItemText(1, QCoreApplication.translate("MainPages", u"funasr(\u8f83\u6162\uff09", None))

        self.label_22.setText(QCoreApplication.translate("MainPages", u"\u662f\u5426\u751f\u6210\u5b57\u5e55\u6587\u4ef6", None))
        self.toggle_save_subtitles.setText("")
        self.label_24.setText(QCoreApplication.translate("MainPages", u"\u5b57\u5e55\u663e\u793a\u4f4d\u7f6e    ", None))
        self.comboBox_sub_place.setItemText(0, QCoreApplication.translate("MainPages", u"\u5e95\u90e8", None))
        self.comboBox_sub_place.setItemText(1, QCoreApplication.translate("MainPages", u"\u9876\u90e8", None))

        self.label_25.setText(QCoreApplication.translate("MainPages", u"\u5b57\u5e55\u989c\u8272       ", None))
        self.btn_sub_colour.setText("")
        self.label_26.setText(QCoreApplication.translate("MainPages", u"\u5b57\u5e55\u5b57\u4f53\u5927\u5c0f    ", None))
        self.comboBox_font_size.setItemText(0, QCoreApplication.translate("MainPages", u"10", None))
        self.comboBox_font_size.setItemText(1, QCoreApplication.translate("MainPages", u"12", None))
        self.comboBox_font_size.setItemText(2, QCoreApplication.translate("MainPages", u"14", None))
        self.comboBox_font_size.setItemText(3, QCoreApplication.translate("MainPages", u"16", None))
        self.comboBox_font_size.setItemText(4, QCoreApplication.translate("MainPages", u"18", None))
        self.comboBox_font_size.setItemText(5, QCoreApplication.translate("MainPages", u"20", None))

        self.btn_apply_setting.setText(QCoreApplication.translate("MainPages", u"\u5e94\u7528\u8bbe\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"\u89c6\u9891\u6587\u4ef6\u8def\u5f84", None))
        self.line_file.setText(QCoreApplication.translate("MainPages", u"\u5f53\u524d\u6587\u4ef6\u8def\u5f84", None))
        self.btn_file.setText(QCoreApplication.translate("MainPages", u"\u6d4f\u89c8...", None))
        self.btn_start_sub.setText(QCoreApplication.translate("MainPages", u"\u751f\u6210\u5b57\u5e55", None))
        self.btn_save_sub.setText(QCoreApplication.translate("MainPages", u"\u5bfc\u51fa\u5b57\u5e55", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"\u542f\u7528\u7f16\u8f91", None))
        self.toggle_edit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u5b57\u5e55\u8f93\u51fa", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"\u5173\u952e\u8bcd\u63d0\u53d6", None))
        self.label_15.setText(QCoreApplication.translate("MainPages", u"\u5173\u952e\u8bcd\u4e2a\u6570", None))
        self.comboBox_keynum.setItemText(0, QCoreApplication.translate("MainPages", u"1", None))
        self.comboBox_keynum.setItemText(1, QCoreApplication.translate("MainPages", u"2", None))
        self.comboBox_keynum.setItemText(2, QCoreApplication.translate("MainPages", u"3", None))
        self.comboBox_keynum.setItemText(3, QCoreApplication.translate("MainPages", u"4", None))

        self.btn_keyword.setText(QCoreApplication.translate("MainPages", u"\u63d0\u53d6\u5173\u952e\u8bcd", None))
        self.pushButton_3.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_4.setText("")
        self.pushButton_10.setText("")
        self.pushButton_2.setText("")
        self.pushButton_9.setText("")
        self.pushButton_5.setText("")
        self.pushButton_1.setText("")
        self.pushButton_6.setText("")
        self.label_10.setText(QCoreApplication.translate("MainPages", u"\u6587\u672c\u6458\u8981", None))
        self.label_11.setText(QCoreApplication.translate("MainPages", u"\u6982\u62ec\u7cbe\u5ea6", None))
        self.comboBox_topK.setItemText(0, QCoreApplication.translate("MainPages", u"1", None))
        self.comboBox_topK.setItemText(1, QCoreApplication.translate("MainPages", u"2", None))
        self.comboBox_topK.setItemText(2, QCoreApplication.translate("MainPages", u"4", None))
        self.comboBox_topK.setItemText(3, QCoreApplication.translate("MainPages", u"8", None))
        self.comboBox_topK.setItemText(4, QCoreApplication.translate("MainPages", u"16", None))

        self.btn_summary.setText(QCoreApplication.translate("MainPages", u"\u63d0\u53d6\u6458\u8981", None))
    # retranslateUi
