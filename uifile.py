# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdfwizard.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 141, 551))
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color:rgb(47, 149, 239)\n"
"}\n"
"QLabel{\n"
"background-color:white;\n"
"color:blue;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"height:22px;\n"
"border:none;\n"
"padding-left:5px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: #F5FAFE;\n"
"color:#2F95EF;\n"
"font-weight:bold\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Script MT Bold"])
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label.setMargin(10)
        self.label.setIndent(0)

        self.verticalLayout.addWidget(self.label)

        self.create_button = QPushButton(self.widget)
        self.create_button.setObjectName(u"create_button")
        font1 = QFont()
        font1.setPointSize(12)
        self.create_button.setFont(font1)
        self.create_button.setCheckable(True)
        self.create_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.create_button)

        self.mainconvert_button = QPushButton(self.widget)
        self.mainconvert_button.setObjectName(u"mainconvert_button")
        self.mainconvert_button.setFont(font1)
        self.mainconvert_button.setCheckable(True)
        self.mainconvert_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.mainconvert_button)

        self.extract_button = QPushButton(self.widget)
        self.extract_button.setObjectName(u"extract_button")
        self.extract_button.setFont(font1)
        self.extract_button.setCheckable(True)
        self.extract_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.extract_button)

        self.split_button = QPushButton(self.widget)
        self.split_button.setObjectName(u"split_button")
        self.split_button.setFont(font1)
        self.split_button.setCheckable(True)
        self.split_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.split_button)

        self.insert_button = QPushButton(self.widget)
        self.insert_button.setObjectName(u"insert_button")
        self.insert_button.setFont(font1)
        self.insert_button.setCheckable(True)
        self.insert_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.insert_button)

        self.merge_button = QPushButton(self.widget)
        self.merge_button.setObjectName(u"merge_button")
        self.merge_button.setFont(font1)
        self.merge_button.setCheckable(True)
        self.merge_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.merge_button)

        self.protect_button = QPushButton(self.widget)
        self.protect_button.setObjectName(u"protect_button")
        self.protect_button.setFont(font1)
        self.protect_button.setCheckable(True)
        self.protect_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.protect_button)

        self.watermark_button = QPushButton(self.widget)
        self.watermark_button.setObjectName(u"watermark_button")
        self.watermark_button.setFont(font1)
        self.watermark_button.setCheckable(True)
        self.watermark_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.watermark_button)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pushButton_9)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(160, 80, 591, 481))
        self.stackedWidget.setStyleSheet(u"background-color:rgb(243, 241, 228)rgb(241, 240, 255)")
        self.create_page = QWidget()
        self.create_page.setObjectName(u"create_page")
        self.label_2 = QLabel(self.create_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 40, 241, 141))
        self.stackedWidget.addWidget(self.create_page)
        self.widget_3 = QWidget()
        self.widget_3.setObjectName(u"widget_3")
        self.stackedWidget.addWidget(self.widget_3)
        self.split_page = QWidget()
        self.split_page.setObjectName(u"split_page")
        self.label_8 = QLabel(self.split_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 180, 91, 16))
        self.stackedWidget.addWidget(self.split_page)
        self.convert_page = QWidget()
        self.convert_page.setObjectName(u"convert_page")
        self.widget_2 = QWidget(self.convert_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 30, 501, 51))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout.addWidget(self.label_5)

        self.convert_from_combobox = QComboBox(self.widget_2)
        self.convert_from_combobox.addItem("")
        self.convert_from_combobox.addItem("")
        self.convert_from_combobox.addItem("")
        self.convert_from_combobox.addItem("")
        self.convert_from_combobox.setObjectName(u"convert_from_combobox")
        self.convert_from_combobox.setFont(font1)

        self.horizontalLayout.addWidget(self.convert_from_combobox)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.convert_to_combobox = QComboBox(self.widget_2)
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.addItem("")
        self.convert_to_combobox.setObjectName(u"convert_to_combobox")
        self.convert_to_combobox.setFont(font1)
        self.convert_to_combobox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.convert_to_combobox)

        self.widget_4 = QWidget(self.convert_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(20, 100, 501, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.selectFile_line = QLineEdit(self.widget_4)
        self.selectFile_line.setObjectName(u"selectFile_line")

        self.horizontalLayout_2.addWidget(self.selectFile_line)

        self.selectFile_button = QPushButton(self.widget_4)
        self.selectFile_button.setObjectName(u"selectFile_button")
        self.selectFile_button.setFont(font1)
        self.selectFile_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.selectFile_button)

        self.selectFolder_line = QLineEdit(self.widget_4)
        self.selectFolder_line.setObjectName(u"selectFolder_line")

        self.horizontalLayout_2.addWidget(self.selectFolder_line)

        self.selectFolder_button = QPushButton(self.widget_4)
        self.selectFolder_button.setObjectName(u"selectFolder_button")
        self.selectFolder_button.setFont(font1)
        self.selectFolder_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.selectFolder_button)

        self.widget_5 = QWidget(self.convert_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(20, 200, 501, 42))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_3 = QLineEdit(self.widget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.selectoutFolder_button = QPushButton(self.widget_5)
        self.selectoutFolder_button.setObjectName(u"selectoutFolder_button")
        self.selectoutFolder_button.setFont(font1)
        self.selectoutFolder_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.selectoutFolder_button)

        self.convert_button = QPushButton(self.convert_page)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setGeometry(QRect(410, 373, 121, 81))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.convert_button.setFont(font3)
        self.convert_button.setStyleSheet(u"background-color:rgb(5, 80, 255);\n"
"color:white;\n"
"border-radius:25px;\n"
"")
        self.convert_button.setCheckable(True)
        self.stackedWidget.addWidget(self.convert_page)
        self.merge_page = QWidget()
        self.merge_page.setObjectName(u"merge_page")
        self.label_6 = QLabel(self.merge_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 150, 181, 16))
        self.stackedWidget.addWidget(self.merge_page)
        self.extract_page = QWidget()
        self.extract_page.setObjectName(u"extract_page")
        self.label_3 = QLabel(self.extract_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 100, 231, 16))
        self.stackedWidget.addWidget(self.extract_page)
        self.watermark_page = QWidget()
        self.watermark_page.setObjectName(u"watermark_page")
        self.label_9 = QLabel(self.watermark_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 160, 261, 16))
        self.stackedWidget.addWidget(self.watermark_page)
        self.protect_page = QWidget()
        self.protect_page.setObjectName(u"protect_page")
        self.label_7 = QLabel(self.protect_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 150, 201, 16))
        self.stackedWidget.addWidget(self.protect_page)
        self.insert_page = QWidget()
        self.insert_page.setObjectName(u"insert_page")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(False)
        self.insert_page.setFont(font4)
        self.label_4 = QLabel(self.insert_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 130, 241, 16))
        self.stackedWidget.addWidget(self.insert_page)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(160, 10, 591, 51))
        font5 = QFont()
        font5.setFamilies([u"Vidya"])
        font5.setPointSize(22)
        font5.setBold(True)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"background-color:rgb(226, 234, 255);\n"
"color:rgb(1, 8, 22);")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setIndent(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_9.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.mainconvert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.extract_button.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.split_button.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.insert_button.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.merge_button.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.protect_button.setText(QCoreApplication.translate("MainWindow", u"Protect", None))
        self.watermark_button.setText(QCoreApplication.translate("MainWindow", u"Watermark", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Create Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"split page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Convert from", None))
        self.convert_from_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Doc/Docx", None))
        self.convert_from_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Image", None))
        self.convert_from_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pdf", None))
        self.convert_from_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Txt", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.convert_to_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Pdf", None))
        self.convert_to_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Image (.jpg)", None))
        self.convert_to_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Image (.jpeg)", None))
        self.convert_to_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Image (.png)", None))
        self.convert_to_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Image (.bmp)", None))
        self.convert_to_combobox.setItemText(5, QCoreApplication.translate("MainWindow", u"Image (.tif)", None))
        self.convert_to_combobox.setItemText(6, QCoreApplication.translate("MainWindow", u"Image (.tiff)", None))

        self.selectFile_button.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.selectFolder_button.setText(QCoreApplication.translate("MainWindow", u"Select Folder", None))
        self.selectoutFolder_button.setText(QCoreApplication.translate("MainWindow", u"Select Output Folder", None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"merge page", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Extract Page", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"watermark page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"protect page", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Insert Page", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Welcome To Pdf Wizard", None))
    # retranslateUi

