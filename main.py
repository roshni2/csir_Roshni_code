import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QTableWidgetItem, QMessageBox, QProgressBar, \
    QSplashScreen

from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
import pandas as pd
import time
import random
import string


class SplashScreen(QSplashScreen):
    def __int__(self):
        super(QSplashScreen, self).__int__()
        loadUi("splash.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        pixmap = QPixmap("splash baground image.jpeg")
        self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)
            



class Page1(QDialog):
    def __init__(self):
        super(Page1, self).__init__()
        loadUi(r"homepage.ui", self)
        self.dataca_btn.clicked.connect(self.go_To_Secondpage)
        self.data_btn.clicked.connect(self.go_To_Thirdpage)
        self.test_btn.clicked.connect(self.go_To_Fourthpage)

    def go_To_Secondpage(self):
        page_2 = Page2()
        widget.addWidget(page_2)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def go_To_Thirdpage(self):
        page_3 = Page3()
        widget.addWidget(page_3)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def go_To_Fourthpage(self):
        page_4 = Page4()
        widget.addWidget(page_4)
        widget.setCurrentIndex(widget.currentIndex() + 3)


class Page2(QDialog):
    def __init__(self):
        super(Page2, self).__init__()
        loadUi(r"filepage2.ui", self)
        self.home_btn.clicked.connect(self.back_to_Firstpage_2)
        self.data_btn.clicked.connect(self.gotothirdpage_2)
        self.test_btn.clicked.connect(self.gotofourthpage_2)
        self.Acq_btn_2.clicked.connect(self.dataHead)
        self.browse_btn.clicked.connect(self.openfile)
        self.type_box.currentIndexChanged.connect(self.selectionbox1)
        self.Acq_btn.clicked.connect(self.show_popup)
        self.progress_bar = QProgressBar()
        self.progress_bar.setGeometry(300, 240, 200, 25)

    def openfile(self):
        '''
        try:
            path = QFileDialog.getOpenFileName(self, 'Open', os.getenv('HOME'), 'CSV(*.csv)')
            self.all_data = pd.read_csv(path[0])
        except:
            print(path)
        '''
        path = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Roshni\\pythonProject\\Test.csv', 'csv file (*.csv)')
        self.file_name.setText(path[0])
        self.file_input.setText(path[0])
        self.all_data = pd.read_csv((path[0]))

    def dataHead(self):
        numColomn = self.spinBox.value()
        if numColomn == 0:
            NumRows = len(self.all_data.index)
        else:
            NumRows = numColomn
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(NumRows)
        self.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def selectionbox1(self, i):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, 'Test_Sample', 'Calibration_Sample', 'Reference_Sample')
        if not os.path.exists(final_directory):
            new_folder = os.makedirs(final_directory)
            self.Type_box.currentText(self, new_folder)
        else:
            self.Type_box.currentText(self, final_directory)

    def back_to_Firstpage_2(self):
        page_1 = Page1()
        widget.addWidget(page_1)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotothirdpage_2(self):
        page_3 = Page3()
        widget.addWidget(page_3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotofourthpage_2(self):
        page_4 = Page4()
        widget.addWidget(page_4)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def show_popup(self):
        self.message = QMessageBox()
        self.message.setWindowTitle('Message- from server ')
        self.message.setText('Id :- Acquired')
        self.message.setIcon(QMessageBox.Question)
        self.message.standardButton(QMessageBox.Ok)
        for i in range(101):
            time.sleep(0.1)
            self.pbar.setValue(i)


class Page3(QDialog):
    def __init__(self):
        super(Page3, self).__init__()
        loadUi(r"3page.ui", self)
        self.dataca_btn.clicked.connect(self.gotoSecondpage_3)
        self.home_btn.clicked.connect(self.gotofirstpage_3)
        self.test_btn.clicked.connect(self.gotofourthpage_3)
        self.calibration_btn.clicked.connect(self.calibrate_data)

    def gotoSecondpage_3(self):
        page_2 = Page2()
        widget.addWidget(page_2)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotofirstpage_3(self):
        page_1 = Page1()
        widget.addWidget(page_1)
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def gotofourthpage_3(self):
        page_4 = Page4()
        widget.addWidget(page_4)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def calibrate_data(self):
        print("calculate data from serial port")
        Page4()


class Page4(QDialog):
    def __init__(self):
        super(Page4, self).__init__()
        loadUi(r"4page.ui", self)
        self.dataca_btn.clicked.connect(self.gotoSecondpage_4)
        self.data_btn.clicked.connect(self.gotothirdpage_4)
        self.home_btn.clicked.connect(self.gotofirstpage_4)

    def gotoSecondpage_4(self):
        page_2 = Page2()
        widget.addWidget(page_2)
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def gotothirdpage_4(self):
        page_3 = Page3()
        widget.addWidget(page_3)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def gotofirstpage_4(self):
        page_1 = Page1()
        widget.addWidget(page_1)
        widget.setCurrentIndex(widget.currentIndex() - 3)


app = QApplication(sys.argv)

splash = SplashScreen()
splash.move(300, 100)
splash.setFixedWidth(544)
splash.setFixedHeight(550)
splash.show()
splash.progress()

mainScreen = Page1()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainScreen)
widget.setFixedWidth(640)
widget.setFixedHeight(740)
widget.show()
app.exec_()
