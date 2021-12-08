# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LeagueView2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from AdminLogin import Ui_AdminLogin

from CodeShare import Ui_CodeShare
from CreateTeam import Ui_CreateTeam
from JoinTeam import Ui_TeamJoiner


class Ui_LeagueView(object):
    def openCodeViewer(self, L):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CodeShare()
        self.ui.setupUi(self.window)
        self.window.show()
    def openAdminLogin(self, L):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminLogin()
        self.ui.setupUi(self.window)
        self.window.show()
    def openTeamJoiner(self, L):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_TeamJoiner()
        self.ui.setupUi(self.window)
        self.window.show()
    def openCreateTeam(self, L):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CreateTeam()
        self.ui.setupUi(self.window)
        self.window.show()
    def back_main(self, L, LeagueView):
        L.show()
        LeagueView.hide()


    def setupUi(self,LeagueView,L):
        self.league_name = "" #get the league name from the confirm league window

        LeagueView.setObjectName("LeagueView")
        LeagueView.resize(610, 713)
        font = QtGui.QFont()
        font.setPointSize(13)
        LeagueView.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LeagueView)
        self.centralwidget.setObjectName("centralwidget")
        self.LeagueName_label = QtWidgets.QLabel(self.centralwidget)
        self.LeagueName_label.setGeometry(QtCore.QRect(210, 60, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.LeagueName_label.setFont(font)
        self.LeagueName_label.setObjectName("label")
        self.LeagueName_label.setText(self.league_name)

        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(90, 150, 461, 461))
        self.Tabs.setObjectName("Tabs")
        self.Welcome = QtWidgets.QWidget()
        self.Welcome.setObjectName("Welcome")
        self.label_4 = QtWidgets.QLabel(self.Welcome)
        self.label_4.setGeometry(QtCore.QRect(150, 80, 201, 91))
        self.label_4.setObjectName("label_4")
        self.Tabs.addTab(self.Welcome, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(90, 70, 251, 321))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(9)

        df = pd.read_excel('Data1.xlsx', 'ViewTeams')
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row[0], col_index, tableItem)

        self.tableWidget.setColumnWidth(1, 125)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(150, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Tabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(60, 0, 331, 411))
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.Tabs.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 80, 351, 321))
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(9)
        ab = pd.read_excel('Data1.xlsx', 'ViewStandings')
        if ab.size == 0:
            return

        ab.fillna('', inplace=True)
        self.tableWidget_2.setRowCount(ab.shape[0])
        self.tableWidget_2.setColumnCount(ab.shape[1])
        self.tableWidget_2.setHorizontalHeaderLabels(ab.columns)

        # returns pandas array object
        for row in ab.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget_2.setItem(row[0], col_index, tableItem)
        self.tableWidget_2.setColumnWidth(1, 50)
        self.tableWidget_2.setColumnWidth(2, 50)
        self.tableWidget_2.setColumnWidth(3, 50)

        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Tabs.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.ScheduleMaker = QtWidgets.QCalendarWidget(self.tab_4)
        self.ScheduleMaker.setGeometry(QtCore.QRect(20, 30, 411, 301))
        self.ScheduleMaker.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.ScheduleMaker.setObjectName("ScheduleMaker")
        self.Tabs.addTab(self.tab_4, "")
        LeagueView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LeagueView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setObjectName("menubar")
        self.menuJoin_a_Team = QtWidgets.QMenu(self.menubar)
        self.menuJoin_a_Team.setObjectName("menuJoin_a_Team")
        self.menuInvite_Players_to_League = QtWidgets.QMenu(self.menubar)
        self.menuInvite_Players_to_League.setObjectName("menuInvite_Players_to_League")
        self.menuLogout = QtWidgets.QMenu(self.menubar)
        self.menuLogout.setObjectName("menuLogout")
        LeagueView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LeagueView)
        self.statusbar.setObjectName("statusbar")
        LeagueView.setStatusBar(self.statusbar)
        self.actionCreate_a_Team = QtWidgets.QAction(LeagueView)
        self.actionCreate_a_Team.setObjectName("actionCreate_a_Team")
        self.actionCreate_a_Team.triggered.connect(self.openCreateTeam)
        self.actionJoin_a_Team = QtWidgets.QAction(LeagueView)
        self.actionJoin_a_Team.setObjectName("actionJoin_a_Team")
        self.actionJoin_a_Team.triggered.connect(self.openTeamJoiner)
        self.actionAdmin_Login = QtWidgets.QAction(LeagueView)
        self.actionAdmin_Login.setObjectName("actionAdmin_Login")
        self.actionAdmin_Login.triggered.connect(self.openAdminLogin)
        self.actionInvite_Players_to_League = QtWidgets.QAction("actionInvite_Players_to_League")
        self.actionInvite_Players_to_League.triggered.connect(self.openCodeViewer)
        self.actionInvite_Players_to_League.setObjectName("actionInvite_Players_to_League")
        self.actionConfirm_Logout = QtWidgets.QAction(LeagueView, triggered = lambda: self.back_main(L,LeagueView))
        self.actionConfirm_Logout.setObjectName("actionConfirm_Logout")
        # self.actionConfirm_Logout.triggered.connect()
        self.menuJoin_a_Team.addAction(self.actionCreate_a_Team)
        self.menuJoin_a_Team.addAction(self.actionJoin_a_Team)
        self.menuJoin_a_Team.addAction(self.actionInvite_Players_to_League)
        self.menuInvite_Players_to_League.addAction(self.actionAdmin_Login)
        self.menuLogout.addAction(self.actionConfirm_Logout)
        self.menubar.addAction(self.menuJoin_a_Team.menuAction())
        self.menubar.addAction(self.menuInvite_Players_to_League.menuAction())
        self.menubar.addAction(self.menuLogout.menuAction())

        self.retranslateUi(LeagueView)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LeagueView)

    def retranslateUi(self, LeagueView):
        _translate = QtCore.QCoreApplication.translate
        LeagueView.setWindowTitle(_translate("LeagueView", "MainWindow"))
        self.LeagueName_label.setText(_translate("LeagueView", "League Name"))
        self.label_4.setText(_translate("LeagueView", "Welcome Information"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Welcome), _translate("LeagueView", "Welcome"))
        self.label_3.setText(_translate("LeagueView", "Team List"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), _translate("LeagueView", "Teams"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("LeagueView", "Rule 1 "))
        item = self.listWidget.item(1)
        item.setText(_translate("LeagueView", "Rule 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("LeagueView", "Rule 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("LeagueView", "Rule 4"))
        item = self.listWidget.item(4)
        item.setText(_translate("LeagueView", "Rule 5"))
        item = self.listWidget.item(5)
        item.setText(_translate("LeagueView", "New Item"))
        item = self.listWidget.item(6)
        item.setText(_translate("LeagueView", "New Item"))
        item = self.listWidget.item(7)
        item.setText(_translate("LeagueView", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_2), _translate("LeagueView", "Rulebook"))
        self.label_2.setText(_translate("LeagueView", "Standings"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), _translate("LeagueView", "Standings"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_4), _translate("LeagueView", "Schedule"))
        self.menuJoin_a_Team.setTitle(_translate("LeagueView", "Team Actions"))
        self.menuInvite_Players_to_League.setTitle(_translate("LeagueView", "Admin"))
        self.menuLogout.setTitle(_translate("LeagueView", "Logout"))
        self.actionCreate_a_Team.setText(_translate("LeagueView", "Create a Team"))
        self.actionJoin_a_Team.setText(_translate("LeagueView", "Join a Team"))
        self.actionAdmin_Login.setText(_translate("LeagueView", "Admin Login"))
        self.actionInvite_Players_to_League.setText(_translate("LeagueView", "Invite Players to League"))
        self.actionConfirm_Logout.setText(_translate("LeagueView", "Confirm Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LeagueView = QtWidgets.QMainWindow()
    ui = Ui_LeagueView()
    ui.setupUi(LeagueView)
    LeagueView.show()
    sys.exit(app.exec_())
