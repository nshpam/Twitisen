# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 12pt \"Sans Serif Collection\";\n"
"background-color: rgb(23, 31, 53);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choiceMenu_frame = QtWidgets.QFrame(self.centralwidget)
        self.choiceMenu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choiceMenu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choiceMenu_frame.setObjectName("choiceMenu_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.choiceMenu_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TweetHarvestframe = QtWidgets.QFrame(self.choiceMenu_frame)
        self.TweetHarvestframe.setStyleSheet("")
        self.TweetHarvestframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TweetHarvestframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TweetHarvestframe.setObjectName("TweetHarvestframe")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.TweetHarvestframe)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.TweetHarvestframe)
        self.label_8.setMinimumSize(QtCore.QSize(30, 30))
        self.label_8.setMaximumSize(QtCore.QSize(30, 30))
        self.label_8.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/icons/icon/twitter.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label = QtWidgets.QLabel(self.TweetHarvestframe)
        self.label.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(28, 150, 232);")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout.addWidget(self.TweetHarvestframe)
        self.Buttonframe = QtWidgets.QFrame(self.choiceMenu_frame)
        self.Buttonframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Buttonframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Buttonframe.setObjectName("Buttonframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Buttonframe)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_dataSentiment = QtWidgets.QPushButton(self.Buttonframe)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_dataSentiment.setFont(font)
        self.pushButton_dataSentiment.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);\n"
"")
        self.pushButton_dataSentiment.setObjectName("pushButton_dataSentiment")
        self.verticalLayout_3.addWidget(self.pushButton_dataSentiment)
        self.pushButton_topWord = QtWidgets.QPushButton(self.Buttonframe)
        self.pushButton_topWord.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);")
        self.pushButton_topWord.setObjectName("pushButton_topWord")
        self.verticalLayout_3.addWidget(self.pushButton_topWord)
        self.pushButton_overallSent = QtWidgets.QPushButton(self.Buttonframe)
        self.pushButton_overallSent.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);")
        self.pushButton_overallSent.setObjectName("pushButton_overallSent")
        self.verticalLayout_3.addWidget(self.pushButton_overallSent)
        self.pushButton_location = QtWidgets.QPushButton(self.Buttonframe)
        self.pushButton_location.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);")
        self.pushButton_location.setObjectName("pushButton_location")
        self.verticalLayout_3.addWidget(self.pushButton_location)
        self.pushButton_scraperSetting = QtWidgets.QPushButton(self.Buttonframe)
        self.pushButton_scraperSetting.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);")
        self.pushButton_scraperSetting.setObjectName("pushButton_scraperSetting")
        self.verticalLayout_3.addWidget(self.pushButton_scraperSetting)
        self.pushButton_searchTerms = QtWidgets.QPushButton(self.Buttonframe)
        self.pushButton_searchTerms.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);")
        self.pushButton_searchTerms.setObjectName("pushButton_searchTerms")
        self.verticalLayout_3.addWidget(self.pushButton_searchTerms)
        self.verticalLayout.addWidget(self.Buttonframe)
        self.frame_6 = QtWidgets.QFrame(self.choiceMenu_frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.choiceMenu_frame)
        self.mainBody = QtWidgets.QFrame(self.centralwidget)
        self.mainBody.setStyleSheet("background-color: rgb(13, 15, 33);\n"
"color: rgb(255, 255, 255);")
        self.mainBody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainBody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Bar_frame = QtWidgets.QFrame(self.mainBody)
        self.Bar_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Bar_frame.setStyleSheet("background-color: rgb(23, 31, 53);\n"
"border-radius: 5px;")
        self.Bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bar_frame.setObjectName("Bar_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Bar_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_frame = QtWidgets.QFrame(self.Bar_frame)
        self.menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.menu_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_menu = QtWidgets.QPushButton(self.menu_frame)
        self.pushButton_menu.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"")
        self.pushButton_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_menu.setIcon(icon)
        self.pushButton_menu.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.horizontalLayout_3.addWidget(self.pushButton_menu)
        self.label_2 = QtWidgets.QLabel(self.menu_frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.menu_frame, 0, QtCore.Qt.AlignLeft)
        self.Dashbord_frame = QtWidgets.QFrame(self.Bar_frame)
        self.Dashbord_frame.setStyleSheet("")
        self.Dashbord_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Dashbord_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Dashbord_frame.setObjectName("Dashbord_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Dashbord_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.Dashbord_frame)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.Dashbord_frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Icon_frame = QtWidgets.QFrame(self.Bar_frame)
        self.Icon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Icon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Icon_frame.setObjectName("Icon_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Icon_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_short = QtWidgets.QPushButton(self.Icon_frame)
        self.pushButton_short.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"")
        self.pushButton_short.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_short.setIcon(icon1)
        self.pushButton_short.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_short.setObjectName("pushButton_short")
        self.horizontalLayout_4.addWidget(self.pushButton_short)
        self.pushButton_padding = QtWidgets.QPushButton(self.Icon_frame)
        self.pushButton_padding.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"")
        self.pushButton_padding.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon/expand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_padding.setIcon(icon2)
        self.pushButton_padding.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_padding.setObjectName("pushButton_padding")
        self.horizontalLayout_4.addWidget(self.pushButton_padding)
        self.pushButton_exit = QtWidgets.QPushButton(self.Icon_frame)
        self.pushButton_exit.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"")
        self.pushButton_exit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icon/closed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon3)
        self.pushButton_exit.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_4.addWidget(self.pushButton_exit)
        self.horizontalLayout_2.addWidget(self.Icon_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.Bar_frame, 0, QtCore.Qt.AlignTop)
        self.output_frame = QtWidgets.QFrame(self.mainBody)
        self.output_frame.setStyleSheet("border-radius: 5px;")
        self.output_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.output_frame.setObjectName("output_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.output_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.output_frame)
        self.stackedWidget.setStyleSheet("background-color: rgb(23, 31, 53);\n"
"border-radius: 5px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.data_sentiment = QtWidgets.QWidget()
        self.data_sentiment.setObjectName("data_sentiment")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.data_sentiment)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.data_sentiment)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.frame_12, 0, QtCore.Qt.AlignTop)
        self.frame_13 = QtWidgets.QFrame(self.data_sentiment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet("background-color: rgb(19, 27, 47);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7.addWidget(self.frame_13)
        self.stackedWidget.addWidget(self.data_sentiment)
        self.top_word = QtWidgets.QWidget()
        self.top_word.setObjectName("top_word")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.top_word)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_15 = QtWidgets.QFrame(self.top_word)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_15)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.frame_14 = QtWidgets.QFrame(self.top_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet("background-color: rgb(19, 27, 47);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_10.addWidget(self.frame_14)
        self.stackedWidget.addWidget(self.top_word)
        self.overall_sentiment = QtWidgets.QWidget()
        self.overall_sentiment.setObjectName("overall_sentiment")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.overall_sentiment)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_17 = QtWidgets.QFrame(self.overall_sentiment)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.frame_17)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_11.addWidget(self.label_6, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_12.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.overall_sentiment)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setStyleSheet("background-color: rgb(19, 27, 47);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_12.addWidget(self.frame_16)
        self.stackedWidget.addWidget(self.overall_sentiment)
        self.location = QtWidgets.QWidget()
        self.location.setObjectName("location")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.location)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_19 = QtWidgets.QFrame(self.location)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.frame_19)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_14.addWidget(self.frame_19)
        self.frame_18 = QtWidgets.QFrame(self.location)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setStyleSheet("background-color: rgb(19, 27, 47);")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_14.addWidget(self.frame_18)
        self.stackedWidget.addWidget(self.location)
        self.scraper_setting = QtWidgets.QWidget()
        self.scraper_setting.setStyleSheet("QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"/* HORIZONTAL SCROLLBAR */\n"
"/* HORIZONTAL SCROLLBAR */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    height: 14px;\n"
"    margin: 0 15px 0 15px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"/* HANDLE BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(80, 80, 122);\n"
"    min-width: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN LEFT - SCROLLBAR */\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    width: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN RIGHT - SCROLLBAR */\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    width: 15px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"    background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"")
        self.scraper_setting.setObjectName("scraper_setting")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scraper_setting)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scraper_setting)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 826, 639))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.inputWord_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.inputWord_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputWord_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputWord_frame.setObjectName("inputWord_frame")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.inputWord_frame)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_7 = QtWidgets.QFrame(self.inputWord_frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setStyleSheet("background-color: rgb(13, 15, 30);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.verticalLayout_16.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.inputWord_frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_8)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spinBox = QtWidgets.QSpinBox(self.frame_8)
        self.spinBox.setStyleSheet("background-color: rgb(13, 15, 30);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.spinBox.setMaximum(999999999)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_8.addWidget(self.spinBox)
        self.verticalLayout_16.addWidget(self.frame_8)
        self.verticalLayout_15.addWidget(self.inputWord_frame)
        self.dateRequest_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.dateRequest_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dateRequest_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dateRequest_frame.setObjectName("dateRequest_frame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.dateRequest_frame)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.dateRequest_frame)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_17.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.dateRequest_frame)
        self.label_12.setStyleSheet("color: rgb(217, 62, 49);")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_17.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dateRequest_frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 862, 507))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.scrollAreaWidgetContents_2)
        self.calendarWidget.setStyleSheet("color: rgb(46, 117, 158);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgb(18, 24, 47);\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_18.addWidget(self.calendarWidget)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_17.addWidget(self.scrollArea_2)
        self.verticalLayout_15.addWidget(self.dateRequest_frame)
        self.btnScrap_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.btnScrap_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btnScrap_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnScrap_frame.setObjectName("btnScrap_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.btnScrap_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.progressBar = QtWidgets.QProgressBar(self.btnScrap_frame)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.pushButton_Scrap = QtWidgets.QPushButton(self.btnScrap_frame)
        self.pushButton_Scrap.setStyleSheet("background-color: rgb(22, 126, 231);\n"
"border-radius: 20px;\n"
"")
        self.pushButton_Scrap.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Scrap.setCheckable(False)
        self.pushButton_Scrap.setAutoDefault(False)
        self.pushButton_Scrap.setDefault(False)
        self.pushButton_Scrap.setObjectName("pushButton_Scrap")
        self.horizontalLayout_9.addWidget(self.pushButton_Scrap)
        self.verticalLayout_15.addWidget(self.btnScrap_frame)
        self.ETL_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.ETL_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ETL_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ETL_frame.setObjectName("ETL_frame")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.ETL_frame)
        self.verticalLayout_19.setContentsMargins(0, 11, 11, 11)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_13 = QtWidgets.QLabel(self.ETL_frame)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_19.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_ETL = QtWidgets.QPushButton(self.ETL_frame)
        self.pushButton_ETL.setStyleSheet("background-color: rgb(22, 126, 231);\n"
"border-radius: 20px;\n"
"")
        self.pushButton_ETL.setObjectName("pushButton_ETL")
        self.verticalLayout_19.addWidget(self.pushButton_ETL)
        self.verticalLayout_15.addWidget(self.ETL_frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame)
        self.stackedWidget.addWidget(self.scraper_setting)
        self.serachTerms = QtWidgets.QWidget()
        self.serachTerms.setObjectName("serachTerms")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.serachTerms)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.availableSearchTerm_frame = QtWidgets.QFrame(self.serachTerms)
        self.availableSearchTerm_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.availableSearchTerm_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.availableSearchTerm_frame.setObjectName("availableSearchTerm_frame")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.availableSearchTerm_frame)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_14 = QtWidgets.QLabel(self.availableSearchTerm_frame)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_20.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        self.listWidget = QtWidgets.QListWidget(self.availableSearchTerm_frame)
        self.listWidget.setStyleSheet("background-color: rgb(19, 27, 47);\n"
"color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_20.addWidget(self.listWidget)
        self.pushButton_selectAll = QtWidgets.QPushButton(self.availableSearchTerm_frame)
        self.pushButton_selectAll.setStyleSheet("background-color: rgb(22, 126, 231);\n"
"border-radius: 20px;\n"
"")
        self.pushButton_selectAll.setObjectName("pushButton_selectAll")
        self.verticalLayout_20.addWidget(self.pushButton_selectAll)
        self.pushButton_deselectAll = QtWidgets.QPushButton(self.availableSearchTerm_frame)
        self.pushButton_deselectAll.setStyleSheet("background-color: rgb(22, 126, 231);\n"
"border-radius: 20px;\n"
"")
        self.pushButton_deselectAll.setObjectName("pushButton_deselectAll")
        self.verticalLayout_20.addWidget(self.pushButton_deselectAll)
        self.pushButton_delete = QtWidgets.QPushButton(self.availableSearchTerm_frame)
        self.pushButton_delete.setStyleSheet("background-color: rgb(22, 126, 231);\n"
"border-radius: 20px;\n"
"")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_20.addWidget(self.pushButton_delete)
        self.horizontalLayout_10.addWidget(self.availableSearchTerm_frame)
        self.detailSearchTerm_frame = QtWidgets.QFrame(self.serachTerms)
        self.detailSearchTerm_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailSearchTerm_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detailSearchTerm_frame.setObjectName("detailSearchTerm_frame")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.detailSearchTerm_frame)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_15 = QtWidgets.QLabel(self.detailSearchTerm_frame)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_21.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.listWidget_2 = QtWidgets.QListWidget(self.detailSearchTerm_frame)
        self.listWidget_2.setStyleSheet("background-color: rgb(19, 27, 47);\n"
"color: rgb(255, 255, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_21.addWidget(self.listWidget_2)
        self.horizontalLayout_10.addWidget(self.detailSearchTerm_frame)
        self.stackedWidget.addWidget(self.serachTerms)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.output_frame)
        self.horizontalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tweet Harvest"))
        self.pushButton_dataSentiment.setText(_translate("MainWindow", "Data Sentiment"))
        self.pushButton_topWord.setText(_translate("MainWindow", "Top Words"))
        self.pushButton_overallSent.setText(_translate("MainWindow", "Overall Sentiment"))
        self.pushButton_location.setText(_translate("MainWindow", "Location"))
        self.pushButton_scraperSetting.setText(_translate("MainWindow", "Scraping settings"))
        self.pushButton_searchTerms.setText(_translate("MainWindow", "Search Terms"))
        self.label_2.setText(_translate("MainWindow", "MENU"))
        self.label_3.setText(_translate("MainWindow", "DASHBORD"))
        self.label_4.setText(_translate("MainWindow", "Sentiment analysis of the data"))
        self.label_5.setText(_translate("MainWindow", "Top 10 Words Results Preview"))
        self.label_6.setText(_translate("MainWindow", "Overall Sentiment Analysis"))
        self.label_7.setText(_translate("MainWindow", "The geographical distribution of tweets"))
        self.label_9.setText(_translate("MainWindow", "Word/Hashtag : "))
        self.label_10.setText(_translate("MainWindow", "Tweet Count Limit : "))
        self.label_11.setText(_translate("MainWindow", "Tweet Created At Date Request"))
        self.label_12.setText(_translate("MainWindow", "You cannot scrape tweets that were created more than a week ago."))
        self.pushButton_Scrap.setText(_translate("MainWindow", "Create API Scrap Task"))
        self.label_13.setText(_translate("MainWindow", "Data Processing"))
        self.pushButton_ETL.setText(_translate("MainWindow", "Analyze Tweets"))
        self.label_14.setText(_translate("MainWindow", "Available Search Term"))
        self.pushButton_selectAll.setText(_translate("MainWindow", "Select All Search Term"))
        self.pushButton_deselectAll.setText(_translate("MainWindow", "Deselect All Search Term"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.label_15.setText(_translate("MainWindow", "Details Search Term"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
