# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("self.MainWindow")
        self.MainWindow.resize(900, 552)



        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWindow.sizePolicy().hasHeightForWidth())
        self.MainWindow.setSizePolicy(sizePolicy)
        self.MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color:white;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tablesListView = QtWidgets.QListWidget(self.centralwidget)
        self.tablesListView.setFixedWidth(160)
        self.tablesListView.setStyleSheet("width:80px;")
        self.tablesListView.setObjectName("tablesListView")
        self.gridLayout.addWidget(self.tablesListView, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.path_db = QtWidgets.QLineEdit(self.centralwidget)
        self.path_db.setEnabled(False)
        self.path_db.setObjectName("path_db")
        self.horizontalLayout.addWidget(self.path_db)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableViewerTableView = QtWidgets.QTableView(self.centralwidget)
        self.tableViewerTableView.setEnabled(True)
        self.tableViewerTableView.setStyleSheet("width:350px;\n"
"height:200px;")
        self.tableViewerTableView.setObjectName("tableViewerTableView")
        self.verticalLayout.addWidget(self.tableViewerTableView)
        self.gridLayout.addLayout(self.verticalLayout, 3, 4, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addRowPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.addRowPushButton.setObjectName("addRowPushButton")
        self.horizontalLayout_2.addWidget(self.addRowPushButton)
        self.deleteRowPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteRowPushButton.setObjectName("deleteRowPushButton")
        self.horizontalLayout_2.addWidget(self.deleteRowPushButton)
        self.saveDbPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveDbPushButton.setObjectName("saveDbPushButton")
        self.horizontalLayout_2.addWidget(self.saveDbPushButton)
        self.openDbPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openDbPushButton.setObjectName("openDbPushButton")
        self.horizontalLayout_2.addWidget(self.openDbPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 4, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(self.MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.open = QtWidgets.QAction(self.MainWindow)
        self.open.setObjectName("open")
        self.actionadd_row = QtWidgets.QAction(self.MainWindow)
        self.actionadd_row.setObjectName("actionadd_row")
        self.actiondel_row = QtWidgets.QAction(self.MainWindow)
        self.actiondel_row.setObjectName("actiondel_row")
        self.actionsave = QtWidgets.QAction(self.MainWindow)
        self.actionsave.setObjectName("actionsave")

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("self.MainWindow", "self.MainWindow"))
        self.label_2.setText(_translate("self.MainWindow", "Tables"))
        self.label.setText(_translate("self.MainWindow", "Path to db:"))
        self.addRowPushButton.setText(_translate("self.MainWindow", "Add row in db"))
        self.deleteRowPushButton.setText(_translate("self.MainWindow", "Delete row in db"))
        self.saveDbPushButton.setText(_translate("self.MainWindow", "Save"))
        self.openDbPushButton.setText(_translate("self.MainWindow", "Open"))
        self.toolBar.setWindowTitle(_translate("self.MainWindow", "toolBar"))
        self.open.setText(_translate("self.MainWindow", "Открыть бд"))
        self.actionadd_row.setText(_translate("self.MainWindow", "add_row"))
        self.actiondel_row.setText(_translate("self.MainWindow", "del_row"))
        self.actionsave.setText(_translate("self.MainWindow", "save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.Qself.MainWindow()
    ui = Ui_self.MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
