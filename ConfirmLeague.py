# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfirmLeague.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PlayerSignup import Ui_PlayerSignup

class Ui_ConfirmLeague(object):
    def openPlayerSignup(self, ConfirmLeague, L):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PlayerSignup()
        self.ui.setupUi(self.window, L)
        ConfirmLeague.hide()
        self.window.show()
        
    def back_main(self, ConfirmLeague, L):
        L.show()
        ConfirmLeague.hide()

    def setupUi(self, ConfirmLeague, L):
        ConfirmLeague.setObjectName("ConfirmLeague")
        ConfirmLeague.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ConfirmLeague)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 170, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.YesBut = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openPlayerSignup(ConfirmLeague,L))
        self.YesBut.setGeometry(QtCore.QRect(390, 200, 75, 23))
        self.YesBut.setObjectName("YesBut")
        self.NoBut = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: ConfirmLeague.close())
        self.NoBut.setGeometry(QtCore.QRect(290, 200, 75, 23))
        self.NoBut.setObjectName("NoBut")
        ConfirmLeague.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConfirmLeague)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ConfirmLeague.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConfirmLeague)
        self.statusbar.setObjectName("statusbar")
        ConfirmLeague.setStatusBar(self.statusbar)
        self.retranslateUi(ConfirmLeague)
        QtCore.QMetaObject.connectSlotsByName(ConfirmLeague)

    def retranslateUi(self, ConfirmLeague):
        _translate = QtCore.QCoreApplication.translate
        ConfirmLeague.setWindowTitle(_translate("ConfirmLeague", "ConfirmLeague"))
        self.label.setText(_translate("ConfirmLeague", "League Name"))
        self.label_2.setText(_translate("ConfirmLeague", "Is this the correct league?"))
        self.YesBut.setText(_translate("ConfirmLeague", "Yes"))
        self.NoBut.setText(_translate("ConfirmLeague", "No"))
        self.label.adjustSize()
        self.label_2.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfirmLeague = QtWidgets.QMainWindow()
    ui = Ui_ConfirmLeague()
    ui.setupUi(ConfirmLeague)
    ConfirmLeague.show()
    sys.exit(app.exec_())
