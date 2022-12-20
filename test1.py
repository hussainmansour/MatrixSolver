from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setGeometry(QRect(0, 0, 800, 600))
        self.MainFrame.setStyleSheet(u"background-color: rgb(46, 52, 54);\n""color: \"white\";")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.MainFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 40, 371, 81))
        font = QFont()
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: \"white\";")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.MainFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 180, 371, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.MainFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 290, 371, 61))
        self.label_4.setFont(font1)
        self.comboBox = QComboBox(self.MainFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(520, 400, 211, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.MainFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 390, 371, 61))
        self.label_5.setFont(font1)
        self.comboBox_2 = QComboBox(self.MainFrame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(580, 190, 151, 41))
        self.comboBox_2.setFont(font2)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_3 = QComboBox(self.MainFrame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(580, 300, 151, 41))
        self.comboBox_3.setFont(font2)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_6 = QPushButton(self.MainFrame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(590, 500, 181, 71))
        self.pushButton_6.setFont(font1)
        self.pushButton_8 = QPushButton(self.MainFrame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 510, 171, 51))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.pushButton_6.raise_()
        self.pushButton_8.raise_()
        self.label_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Matrix Solver", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter number of equations:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Enter the percision:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gauss Elimination", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gauss Jordan", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"LU Decomposition", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Jacobi Iterative Method", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Gauss Seidel", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Choose the operation:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"9", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_3.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_3.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_3.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_3.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_3.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_3.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Proceed", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Scaling", None))
    # retranslateUi
