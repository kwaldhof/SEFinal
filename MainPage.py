# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tester.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from LeagueCreator import Ui_CreateLeague
from LeagueFinder import Ui_LeagueFinder



class Ui_Leagues(object):
    def openLeagueCreator(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateLeague()
        self.ui.setupUi(self.window)
        self.window.show()

    def openLeagueFinder(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LeagueFinder()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, L):
        L.setObjectName("L")
        L.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(L)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFixedSize(800, 600)
        windowwidth = self.centralwidget.width()
        windowheight = self.centralwidget.height()
        self.LeagueMaker = QtWidgets.QPushButton(self.centralwidget,  clicked = lambda: self.openLeagueCreator())
        self.LeagueMaker.setGeometry(QtCore.QRect(int(windowwidth/2)-(windowwidth*0.2/2), 180, int(windowwidth*0.2), int(windowheight*0.06)))
        # self.LeagueMaker.setSizePolicy()
        self.LeagueMaker.setObjectName("LeagueMaker")
        self.LeagueViewer = QtWidgets.QPushButton(self.centralwidget)
        self.LeagueViewer.setGeometry(QtCore.QRect(340, 360, 101, 31))
        self.LeagueViewer.setFixedSize(120,20)
        self.LeagueViewer.setObjectName("LeagueViewer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 110, 101, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        # button
        self.LeagueJoiner = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openLeagueFinder())
        self.LeagueJoiner.setGeometry(QtCore.QRect(340, 270, 101, 31))
        self.LeagueJoiner.setFixedSize(120,20)
        self.LeagueJoiner.setObjectName("LeagueJoiner")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        L.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(L)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        L.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(L)
        self.statusbar.setObjectName("statusbar")
        L.setStatusBar(self.statusbar)

        self.retranslateUi(L)
        QtCore.QMetaObject.connectSlotsByName(L)

    def retranslateUi(self, L):
        _translate = QtCore.QCoreApplication.translate
        L.setWindowTitle(_translate("L", "MainWindow"))
        self.LeagueMaker.setText(_translate("L", "Create a League"))
        self.LeagueViewer.setText(_translate("L", "View a League"))
        self.LeagueJoiner.setText(_translate("L", "Join a League"))
        self.label_2.setText(_translate("L", "IM Made EZ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    L = QtWidgets.QMainWindow()
    ui = Ui_Leagues()
    ui.setupUi(L)
    L.show()
    sys.exit(app.exec_())
