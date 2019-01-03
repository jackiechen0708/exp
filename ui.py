# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import os

class Info:
    def __init__(self):
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def education(self):
        return self._education

    @education.setter
    def education(self, education):
        self._education = education

    @property
    def exp1(self):
        return self._exp1

    @exp1.setter
    def exp1(self, exp):
        self._exp1 = exp

    @property
    def exp2(self):
        return self._exp2

    @exp2.setter
    def exp2(self, exp):
        self._exp2 = exp

    @property
    def exp3(self):
        return self._exp3

    @exp3.setter
    def exp3(self, exp):
        self._exp3 = exp


class Ui_MainWindow(object):
    def __init__(self):
        self.info = Info()
        self.flag1 = -1
        self.flag2 = -1
        self.flag3 = -1

        # TODO: load from file
        self.record = []
        if (os.path.exists("record.txt")):
            with open("record.txt") as fp:
                for line in fp.readlines():
                    line = line.replace("\n","")
                    line = line.split()

                    tmp = Info()
                    tmp.age = int (line[0])
                    tmp.gender = line[1]
                    tmp.education = line[2]
                    tmp.exp1 = int(line[3])
                    tmp.exp2 = int(line[4])
                    tmp.exp3 = int(line[5])
                    self.record.append(tmp)
        self.count = [[0, 0], [0, 0], [0, 0]]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 781, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(310, 80, 251, 111))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.page)
        self.checkBox.setGeometry(QtCore.QRect(480, 290, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(310, 50, 251, 111))
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 400, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1) if self.checkBox.checkState() else None)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(290, 200, 72, 15))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.page_3)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 200, 87, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox = QtWidgets.QComboBox(self.page_3)
        self.comboBox.setGeometry(QtCore.QRect(380, 250, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.page_3)
        self.textEdit.setGeometry(QtCore.QRect(370, 140, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(320, 110, 171, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(280, 250, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(300, 150, 72, 15))
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 400, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")

        def jump():
            if len(self.textEdit.toPlainText()) == 0:
                pass
            else:

                self.info.age = int(self.textEdit.toPlainText())
                self.info.gender = self.comboBox_2.currentText()
                self.info.education = self.comboBox.currentText()
                self.stackedWidget.setCurrentIndex(2)

        self.pushButton_8.clicked.connect(jump)
        self.stackedWidget.addWidget(self.page_3)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_7)
        self.textBrowser.setGeometry(QtCore.QRect(200, 70, 411, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_7)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 400, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(3) if self.checkBox.checkState() else None)
        self.stackedWidget.addWidget(self.page_7)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 370, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(370, 60, 91, 16))
        self.label_7.setObjectName("label_7")
        self.qlabel = QtWidgets.QLabel(self.page_2)
        self.qlabel.setGeometry(QtCore.QRect(110, 10, 256, 320))
        self.qlabel.setObjectName("qlabel")
        self.qlabel_2 = QtWidgets.QLabel(self.page_2)
        self.qlabel_2.setGeometry(QtCore.QRect(460, 10, 256, 320))
        self.qlabel_2.setObjectName("qlabel_2")
        if random.random() < 0.5:
            self.qlabel.setPixmap(QtGui.QPixmap(QtGui.QImage("known.png")))
            self.qlabel_2.setPixmap(QtGui.QPixmap(QtGui.QImage("unknown.png")))
            self.flag1 = 1
        else:
            self.qlabel.setPixmap(QtGui.QPixmap(QtGui.QImage("unknown.png")))
            self.qlabel_2.setPixmap(QtGui.QPixmap(QtGui.QImage("known.png")))
            self.flag1 = 0

        def select1():
            self.pushButton.setStyleSheet("background-color: red")
            self.pushButton_2.setStyleSheet("background-color: white")
            self.info.exp1 = self.flag1

        def select2():
            self.pushButton_2.setStyleSheet("background-color: red")
            self.pushButton.setStyleSheet("background-color: white")
            self.info.exp1 = 1 - self.flag1

        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(180, 370, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(select1)
        self.pushButton_2.clicked.connect(select2)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(80, 430, 311, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(450, 430, 311, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 480, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4) if hasattr(self.info,"_exp1") else None)
        self.stackedWidget.addWidget(self.page_2)

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 370, 93, 28))
        self.pushButton_4.setObjectName("pushButton_3")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(370, 60, 91, 16))
        self.label_10.setObjectName("label_10")
        self.qlabel_3 = QtWidgets.QLabel(self.page_4)
        self.qlabel_3.setGeometry(QtCore.QRect(110, 10, 256, 320))
        self.qlabel_3.setObjectName("qlabel_3")
        self.qlabel_4 = QtWidgets.QLabel(self.page_4)
        self.qlabel_4.setGeometry(QtCore.QRect(460, 10, 256, 320))
        self.qlabel_4.setObjectName("qlabel_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 370, 93, 28))
        self.pushButton_3.setObjectName("pushButton_4")

        if random.random() < 0.5:
            self.qlabel_3.setPixmap(QtGui.QPixmap(QtGui.QImage("known.png")))
            self.qlabel_4.setPixmap(QtGui.QPixmap(QtGui.QImage("unknown.png")))
            self.flag2 = 1
        else:
            self.qlabel_3.setPixmap(QtGui.QPixmap(QtGui.QImage("unknown.png")))
            self.qlabel_4.setPixmap(QtGui.QPixmap(QtGui.QImage("known.png")))
            self.flag2 = 0

        def select3():
            self.pushButton_3.setStyleSheet("background-color: red")
            self.pushButton_4.setStyleSheet("background-color: white")
            self.info.exp2 = self.flag2

        def select4():
            self.pushButton_4.setStyleSheet("background-color: red")
            self.pushButton_3.setStyleSheet("background-color: white")
            self.info.exp2 = 1 - self.flag2

        self.pushButton_3.clicked.connect(select3)
        self.pushButton_4.clicked.connect(select4)
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(80, 430, 311, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(450, 430, 311, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_11.setGeometry(QtCore.QRect(620, 480, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5) if hasattr(self.info,"_exp2") else None)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 370, 93, 28))
        self.pushButton_6.setObjectName("pushButton_5")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(370, 60, 91, 16))
        self.label_13.setObjectName("label_13")
        self.qlabel_5 = QtWidgets.QLabel(self.page_5)
        self.qlabel_5.setGeometry(QtCore.QRect(110, 10, 256, 320))
        self.qlabel_5.setObjectName("qlabel_5")
        self.qlabel_6 = QtWidgets.QLabel(self.page_5)
        self.qlabel_6.setGeometry(QtCore.QRect(460, 10, 256, 320))
        self.qlabel_6.setObjectName("qlabel_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 370, 93, 28))
        self.pushButton_5.setObjectName("pushButton_6")

        if random.random() < 0.5:
            self.qlabel_5.setPixmap(QtGui.QPixmap(QtGui.QImage("known.png")))
            self.qlabel_6.setPixmap(QtGui.QPixmap(QtGui.QImage("unknown.png")))
            self.flag3 = 1
        else:
            self.qlabel_5.setPixmap(QtGui.QPixmap(QtGui.QImage("unknown.png")))
            self.qlabel_6.setPixmap(QtGui.QPixmap(QtGui.QImage("known.png")))
            self.flag3 = 0

        def select5():
            self.pushButton_5.setStyleSheet("background-color: red")
            self.pushButton_6.setStyleSheet("background-color: white")
            self.info.exp3 = self.flag3

        def select6():
            self.pushButton_6.setStyleSheet("background-color: red")
            self.pushButton_5.setStyleSheet("background-color: white")
            self.info.exp3 = 1 - self.flag3

        self.pushButton_5.clicked.connect(select5)
        self.pushButton_6.clicked.connect(select6)

        self.label_16 = QtWidgets.QLabel(self.page_5)
        self.label_16.setGeometry(QtCore.QRect(90, 430, 311, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(460, 430, 311, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_12.setGeometry(QtCore.QRect(620, 480, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")

        def summary():
            try:
                if hasattr(self.info, "_exp3"):
                    self.record.append(self.info)

                    for record in self.record:
                        if record.exp1:
                            self.count[0][0] += 1
                        else:
                            self.count[0][1] += 1
                        if record.exp2:
                            self.count[1][0] += 1
                        else:
                            self.count[1][1] += 1
                        if record.exp3:
                            self.count[2][0] += 1
                        else:
                            self.count[2][1] += 1
                    print(self.count)
                    for i in range(len(self.count)):
                        for j in range(len(self.count[0])):
                            print("debug", i, j, self.count[i][j])
                            self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.count[i][j])))
                    self.tableWidget.setItem(len(self.count), 0,
                                             QtWidgets.QTableWidgetItem(str(sum([i[0] for i in self.count]))))
                    self.tableWidget.setItem(len(self.count), 1,
                                             QtWidgets.QTableWidgetItem(str(sum([i[1] for i in self.count]))))
                    self.stackedWidget.setCurrentIndex(6)
            except Exception as e:
                print(e)

        self.pushButton_12.clicked.connect(summary)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.tableWidget = QtWidgets.QTableWidget(self.page_6)
        self.tableWidget.setGeometry(QtCore.QRect(240, 140, 331, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)


        self.label_14 = QtWidgets.QLabel(self.page_6)
        self.label_14.setGeometry(QtCore.QRect(370, 90, 72, 15))
        self.label_14.setObjectName("label_14")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_13.setGeometry(QtCore.QRect(560, 420, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")

        def save():
            # TODO:save
            with open("record.txt","w") as fp:
                for i in self.record:
                    fp.write(str(i.age) + " " + str(i.gender) +" " + str(i.education) + " " + str(i.exp1) +" " + str(i.exp2) +" " + str(i.exp3)+"\n")
            exit(0)
        self.pushButton_13.clicked.connect(save)
        self.stackedWidget.addWidget(self.page_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Click \"Agree\" To Accept Experiment"))
        self.checkBox.setText(_translate("MainWindow", "Agree"))
        self.label_2.setText(_translate("MainWindow", "I have read all the consent."))
        self.pushButton_7.setText(_translate("MainWindow", "Next"))
        self.label_3.setText(_translate("MainWindow", "Gender"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox.setItemText(0, _translate("MainWindow", "College"))
        self.comboBox.setItemText(1, _translate("MainWindow", "High School"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Middle School"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Personal Information"))
        self.label_5.setText(_translate("MainWindow", "Education"))
        self.label_6.setText(_translate("MainWindow", "Age"))
        self.pushButton_8.setText(_translate("MainWindow", "Next"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Consider the following problem carefully, then write down your decision. On the table are two urns, labeled A and B, containing red and blue marbles, and you have to draw a marble from one of the urns without looking. If you get a blue marble, you will be entered into a £30 lottery draw. Urn A contains 50 red marbles and 50 blue marbles. Urn B contains 100 marbles in an unknown color ratio, from 100 red marbles and 0 blue marbles to 0 red marbles and 100 blue marbles. The mixture of red and blue marbles in Urn B has been decided by writing the numbers 0, 1, 2, . . ., 100 on separate slips of paper, shuffling the slips thoroughly, and then drawing one of them at random. The number chosen was used to determine the number of blue marbles to be put into Urn B, but you do not know the number. Every possible mixture of red and blue marbles in Urn B is equally likely. You have to decide whether you prefer to draw a marble at random from Urn A or Urn B. What you hope is to draw a blue marble and be entered for the £30 lottery draw. Consider very carefully from which urn you prefer to draw the marble, then write down your decision below. You will draw a marble from your chosen urn straight afterwards. I prefer to draw a marble from Urn A/Urn B</p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Next"))
        self.pushButton_2.setText(_translate("MainWindow", "urn B"))
        self.label_7.setText(_translate("MainWindow", "2 Marbles"))
        self.pushButton.setText(_translate("MainWindow", "urn A"))
        self.label_8.setText(_translate("MainWindow", "I prefer to draw a marble from Urn A"))
        self.label_9.setText(_translate("MainWindow", "I prefer to draw a marble from Urn B"))
        self.pushButton_10.setText(_translate("MainWindow", "Next"))
        self.pushButton_3.setText(_translate("MainWindow", "urn A"))
        self.label_10.setText(_translate("MainWindow", "10 Marbles"))
        self.pushButton_4.setText(_translate("MainWindow", "urn B"))
        self.label_11.setText(_translate("MainWindow", "I prefer to draw a marble from Urn A"))
        self.label_12.setText(_translate("MainWindow", "I prefer to draw a marble from Urn B"))
        self.pushButton_11.setText(_translate("MainWindow", "Next"))
        self.pushButton_5.setText(_translate("MainWindow", "urn A"))
        self.label_13.setText(_translate("MainWindow", "100 Marbles"))
        self.pushButton_6.setText(_translate("MainWindow", "urn B"))
        self.label_16.setText(_translate("MainWindow", "I prefer to draw a marble from Urn A"))
        self.label_17.setText(_translate("MainWindow", "I prefer to draw a marble from Urn B"))
        self.pushButton_12.setText(_translate("MainWindow", "Next"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Known risk"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ambiguous"))
        self.label_14.setText(_translate("MainWindow", "Result"))
        self.pushButton_13.setText(_translate("MainWindow", "Finish"))
