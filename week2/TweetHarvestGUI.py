from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    #widget form size, tab widget, text label of Twitter API Scraper and Search Input
    def __init__(self, Form):
        Form.setObjectName("Form")
        Form.resize(1019,698)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85,98,112,255), stop:1 rgba(255,107,107,255));")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(390, 19, 611, 661))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.tabWidget.setObjectName("tabWidget")
        # self.tabWidget.addTab(self.tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(60, 30, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgba(255,255,255,220);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(255,255,255,220);")
        self.label_2.setObjectName("label_2")
        
    # calendar in widget tab of Super Task
    def calendar(self):
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setGeometry(QtCore.QRect(60, 50, 491, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("color:rbg(48,44,47)")
        self.calendarWidget.setObjectName("calendarWidget")
        
    # spin box of tweet count limit in widget tab of Super Task
    def spinbox(self):
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(230, 350, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(1000000)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color:rgb(210,214,213);\n"
"border-radius:10px;")
        self.spinBox.setObjectName("spinBox")
    
    # text label of tweet count limit
    def textLabel_tweetcountlimit(self):
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(70, 350, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
    # create api scrap task button
    def button_create_api_scrap_task(self):
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 440, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(143,142,140);\n"
"border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
    
    # text label of warn note
    def textlabel_note(self):
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(110, 20, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(239,73,59);")
        self.label_4.setObjectName("label_4")
        
    # clear analyze data button
    def button_clear_analyze_data(self):
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 580, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(143,142,140);\n"
"border-radius:10px;")
        self.pushButton_3.setObjectName("pushButton_3")
        
    # text label of analyzed data sentiment
    def textLabel_analyzeddatasentiment(self):
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
    # Stacked bar chart of analyzed data sentiment
    def display_Stacked_bar_chart(self):
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(10, 60, 581, 271))
        self.graphicsView.setObjectName("graphicsView")
        
    # text label of top word Result Preview
    def textLabel_topwordResultPreview(self):
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 340, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
    # horizontal bar chart of top word Result Preview
    def display_top_word_Result_Preview(self):
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 380, 411, 231))
        self.graphicsView_3.setObjectName("graphicsView_3")
        
    # text label of Conduct Overall Sentiment Analysis
    def textLabel_ConductOverallSentimentAnalysis(self):
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
    # Donut chart of Conduct Overall Sentiment Analysis
    def display_Overall_Sentiment_Analysis(self):
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 40, 581, 321))
        self.graphicsView_2.setObjectName("graphicsView_2")
        
    # text label of System Overview
    def textLabel_SystemOverview(self):
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
    # text label of Total Document/Tweet Count
    def textLabel_TweetCount(self):
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(50, 430, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        
    # display output of Total Document/Tweet Count
    def textOutput_TweetCount(self):
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setGeometry(QtCore.QRect(40, 470, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:rgb(210,214,213);")
        self.textBrowser.setObjectName("textBrowser")
        
    # text label of Newest Twitter Create At Date
    def textLabel_NewestTwitterDate(self):
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(340, 430, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
    # display output of Newest Twitter Create At Date
    def textOutput_NewestTwitterDate(self):
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(290, 470, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color:rgb(210,214,213);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        
    # text label of Last Time Update/Scraping
    def textLabel_LastTimeScraping(self):
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(70, 530, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
    # display output of Last Time Update/Scraping
    def textOutput_LastTimeScraping(self):
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 570, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color:rgb(210,214,213);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        
    # text label of Current Time
    def textLabel_CurrentTime(self):
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(410, 530, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
    # display output of Current Time
    def textOutput_CurrentTime(self):
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(310, 570, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("background-color:rgb(210,214,213);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        
    # Search label
    def Search_input(self, Form):
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 130, 321, 181))
        self.textEdit.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;\n"
"")
        self.textEdit.setObjectName("textEdit")
    
    # Progressbar display  
    def Progress_bar(self, Form):
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(30, 320, 361, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        
    # Cancel Button
    def button_cancel(self, Form):
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 360, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(210,214,213);\n"
"border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        self.pushButton.clicked.connect(self.textEdit.clear) # type: ignore
        self.pushButton.clicked.connect(self.progressBar.reset) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    
        
    # Group box of type selection
    def GroupBox_type(self,Form):
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 410, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color:rgba(255,255,255,220);\n"
"background-color:rgba(255,255,255,0);")
        self.groupBox.setObjectName("groupBox")
        
    # Radio button of Word
    # def RadioButton_word(self):
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 40, 95, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color:rgba(255,255,255,0);")
        self.radioButton_2.setObjectName("radioButton_2")
        
    # Radio button of Hashtag
    # def RadioButton_hashtag(self):
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color:rgba(255,255,255,0);")
        self.radioButton.setObjectName("radioButton")
        
    # setting the text for various labels, buttons, and other UI elements in a form called "Form"
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Tweet Count Limit :"))
        self.pushButton_2.setText(_translate("Form", "Create API Scrap Task"))
        self.label_4.setText(_translate("Form", "You can not scrap tweet that is created more than a week"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Super Task"))
        self.pushButton_3.setText(_translate("Form", "Clear Analyze Data"))
        self.label_5.setText(_translate("Form", "Analyzed Data Sentiment"))
        self.label_6.setText(_translate("Form", "Top word Result Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Analyze Date"))
        self.label_7.setText(_translate("Form", "Conduct Overall Sentiment Analysis"))
        self.label_8.setText(_translate("Form", "System Overview"))
        self.label_9.setText(_translate("Form", "Total Document/Tweet Count"))
        self.label_10.setText(_translate("Form", "Newest Twitter Create At Date"))
        self.label_11.setText(_translate("Form", "Last Time Update/Scraping"))
        self.label_12.setText(_translate("Form", "Current Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Analyze Overall Sentiment"))
        self.label.setText(_translate("Form", "Twitter API Scraper"))
        self.label_2.setText(_translate("Form", "Search Input"))
        self.pushButton.setText(_translate("Form", "Cancel"))
        self.groupBox.setTitle(_translate("Form", "Type Selection"))
        self.radioButton_2.setText(_translate("Form", "Word"))
        self.radioButton.setText(_translate("Form", "Hashtag"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    ui.calendar()
    ui.spinbox()
    ui.textLabel_tweetcountlimit()
    ui.button_create_api_scrap_task()
    ui.textlabel_note()
    ui.button_clear_analyze_data()
    ui.textLabel_analyzeddatasentiment()
    ui.display_Stacked_bar_chart()
    ui.textLabel_topwordResultPreview()
    ui.display_top_word_Result_Preview()
    ui.textLabel_ConductOverallSentimentAnalysis()
    ui.display_Overall_Sentiment_Analysis()
    ui.textLabel_SystemOverview()
    ui.textLabel_TweetCount()
    ui.textOutput_TweetCount()
    ui.textLabel_NewestTwitterDate()
    ui.textOutput_NewestTwitterDate()
    ui.textLabel_LastTimeScraping()
    ui.textOutput_LastTimeScraping()
    ui.textLabel_CurrentTime()
    ui.textOutput_CurrentTime()
    ui.Search_input(Form)
    ui.Progress_bar(Form)
    ui.button_cancel(Form)
    ui.GroupBox_type(Form)
    # ui.RadioButton_word()
    # ui.RadioButton_hashtag()
    ui.retranslateUi(Form)
    
    Form.show()
    sys.exit(app.exec_())