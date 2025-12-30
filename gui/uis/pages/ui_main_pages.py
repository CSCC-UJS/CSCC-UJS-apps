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
from gui.widgets.py_icon_button.py_icon_button import PyIconButton
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_slider.py_slider import PySlider

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(780, 555)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_home)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_home)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.Shape.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Shadow.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.Shape.NoFrame)
        self.logo.setFrameShadow(QFrame.Shadow.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pages.addWidget(self.page_home)
        self.page_tools = QWidget()
        self.page_tools.setObjectName(u"page_tools")
        self.page_2_layout = QVBoxLayout(self.page_tools)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_tools)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 233, 265))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_tools)
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

        self.volume_btn = PyIconButton(self.page_videoplayer)
        self.volume_btn.setObjectName(u"volume_btn")
        self.volume_btn.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.volume_btn)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 11)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.pages.addWidget(self.page_videoplayer)
        self.page_tool = QWidget()
        self.page_tool.setObjectName(u"page_tool")
        self.verticalLayout_5 = QVBoxLayout(self.page_tool)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_tool)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_11 = PyPushButton(self.page_tool)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 0, 1, 1)

        self.pushButton_4 = PyPushButton(self.page_tool)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_10 = PyPushButton(self.page_tool)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 1, 4, 1, 1)

        self.pushButton_6 = PyPushButton(self.page_tool)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_15 = PyPushButton(self.page_tool)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)

        self.pushButton_12 = PyPushButton(self.page_tool)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 2, 1, 1, 1)

        self.pushButton_5 = PyPushButton(self.page_tool)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_14 = PyPushButton(self.page_tool)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)

        self.pushButton_8 = PyPushButton(self.page_tool)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.pushButton_9 = PyPushButton(self.page_tool)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 0, 4, 1, 1)

        self.pushButton_1 = PyPushButton(self.page_tool)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_7 = PyPushButton(self.page_tool)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_13 = PyPushButton(self.page_tool)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 2, 2, 1, 1)

        self.pushButton_2 = PyPushButton(self.page_tool)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = PyPushButton(self.page_tool)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.label_3 = QLabel(self.page_tool)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt \"JetBrains Mono\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_3)

        self.plainTextEdit = QPlainTextEdit(self.page_tool)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.pages.addWidget(self.page_tool)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.prev_btn.setText("")
        self.stop_btn.setText("")
        self.next_btn.setText("")
        self.progress_label.setText(QCoreApplication.translate("MainPages", u"00:00", None))
        self.volume_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainPages", u"\u5173\u952e\u8bcd\u63d0\u53d6", None))
        self.pushButton_11.setText("")
        self.pushButton_4.setText("")
        self.pushButton_10.setText("")
        self.pushButton_6.setText("")
        self.pushButton_15.setText("")
        self.pushButton_12.setText("")
        self.pushButton_5.setText("")
        self.pushButton_14.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.pushButton_1.setText("")
        self.pushButton_7.setText("")
        self.pushButton_13.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("MainPages", u"\u6587\u672c\u6458\u8981", None))
    # retranslateUi

