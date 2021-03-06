# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from openpyxl import load_workbook
from pandas.core import series
import numpy as np


class Ui_CreateTeam(object):
    def createTeam(self):
        fname = "Data1.xlsx"
        data = pd.read_excel(fname,"ViewTeams") #read the excel file
        new_data = [[self.TeamName.text(), 1]] #Fetching new record from the frontend (right now I am just set up a record)
        df2 = pd.DataFrame(new_data, columns=['Team Name', 'Player Count'])# Convert this new record to dataframe
        data = data.append(df2,ignore_index=True)#append to the data we got from the excel
        book = load_workbook(fname)
        writer = pd.ExcelWriter(fname,engine = 'openpyxl')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)#trying to set up not overwrite the excel
        data.to_excel(writer,sheet_name="ViewTeams",index=False)#push the data to the excel
        writer.save()

    def setupUi(self, CreateTeam):
        CreateTeam.setObjectName("CreateTeam")
        CreateTeam.resize(493, 233)
        self.centralwidget = QtWidgets.QWidget(CreateTeam)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.TeamName = QtWidgets.QLineEdit(self.centralwidget)
        self.TeamName.setGeometry(QtCore.QRect(210, 90, 113, 20))
        self.TeamName.setObjectName("TeamName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.FreeAgent = QtWidgets.QCheckBox(self.centralwidget)
        self.FreeAgent.setGeometry(QtCore.QRect(140, 120, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FreeAgent.setFont(font)
        self.FreeAgent.setObjectName("FreeAgent")
        self.Confirm = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: [self.createTeam(), CreateTeam.hide()])
        self.Confirm.setGeometry(QtCore.QRect(250, 150, 75, 23))
        self.Confirm.setObjectName("Confirm")
        self.Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.Cancel.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.Cancel.setObjectName("Cancel")
        CreateTeam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateTeam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 21))
        self.menubar.setObjectName("menubar")
        CreateTeam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CreateTeam)
        self.statusbar.setObjectName("statusbar")
        CreateTeam.setStatusBar(self.statusbar)

        self.retranslateUi(CreateTeam)
        QtCore.QMetaObject.connectSlotsByName(CreateTeam)

    def retranslateUi(self, CreateTeam):
        _translate = QtCore.QCoreApplication.translate
        CreateTeam.setWindowTitle(_translate("CreateTeam", "MainWindow"))
        self.label.setText(_translate("CreateTeam", "Create a Team"))
        self.label_2.setText(_translate("CreateTeam", "Team Name:"))
        self.FreeAgent.setText(_translate("CreateTeam", "Accepting Free Agents"))
        self.Confirm.setText(_translate("CreateTeam", "Confirm"))
        self.Cancel.setText(_translate("CreateTeam", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateTeam = QtWidgets.QMainWindow()
    ui = Ui_CreateTeam()
    ui.setupUi(CreateTeam)
    CreateTeam.show()
    sys.exit(app.exec_())
