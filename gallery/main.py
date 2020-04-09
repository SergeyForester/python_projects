# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gallery.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import threading

from PyQt5 import QtCore, QtGui, QtWidgets

import data
import db


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1083, 804)
        MainWindow.setStyleSheet("background-color:white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagesL = QtWidgets.QVBoxLayout(self.centralwidget)
        self.imagesL.setGeometry(QtCore.QRect(60, 140, 961, 621))
        self.imagesL.setObjectName("listView")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1083, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        showThread = threading.Thread(target=self.show_images).start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Gallery"))

    def show_images(self):
        print(len(db.get_images()))

        if len(db.get_images()) < 40:
            self.setup_db()

        files = db.get_images()

        for x in files[:40]:
            print(x)
            print(type(x))

            button = QtWidgets.QPushButton()
            button.setFixedSize(400, 300)

            icon = QtGui.QIcon(x['title'])

            button.setIcon(icon)
            button.setIconSize(button.size())

            self.imagesL.addWidget(button)

    def setup_db(self):
        images = data.get_images()
        for image in images:
            db.add_image(image)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
