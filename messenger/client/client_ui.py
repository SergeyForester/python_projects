# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ClientUI(object):
    def setupUi(self, ClientUI):
        ClientUI.setObjectName("ClientUI")
        ClientUI.resize(995, 757)
        ClientUI.setStyleSheet("background-color: rgb(41, 41, 41);")
        self.widget_2 = QtWidgets.QWidget(ClientUI)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 971, 41))
        self.widget_2.setStyleSheet("background-color: rgb(63, 63, 63);")
        self.widget_2.setObjectName("widget_2")
        self.appNameLabel = QtWidgets.QLabel(self.widget_2)
        self.appNameLabel.setGeometry(QtCore.QRect(10, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.appNameLabel.setObjectName("appNameLabel")
        self.greetingsLabel = QtWidgets.QLabel(self.widget_2)
        self.greetingsLabel.setGeometry(QtCore.QRect(120, 0, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.greetingsLabel.setFont(font)
        self.greetingsLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.greetingsLabel.setObjectName("greetingsLabel")
        self.contactsListWidget = QtWidgets.QListWidget(ClientUI)
        self.contactsListWidget.setGeometry(QtCore.QRect(10, 100, 241, 631))
        self.contactsListWidget.setStyleSheet("color: rgb(255, 255, 255); font-size:22px;")
        self.contactsListWidget.setObjectName("contactsListWidget")
        self.greetingsLabel_2 = QtWidgets.QLabel(ClientUI)
        self.greetingsLabel_2.setGeometry(QtCore.QRect(20, 70, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.greetingsLabel_2.setFont(font)
        self.greetingsLabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.greetingsLabel_2.setObjectName("greetingsLabel_2")
        self.messageTextEdit = QtWidgets.QTextEdit(ClientUI)
        self.messageTextEdit.setStyleSheet("color: white; font-size:17px;")
        self.messageTextEdit.setGeometry(QtCore.QRect(270, 670, 621, 61))
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.sendMessageBtn = QtWidgets.QPushButton(ClientUI)
        self.sendMessageBtn.setGeometry(QtCore.QRect(910, 680, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sendMessageBtn.setFont(font)
        self.sendMessageBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.sendMessageBtn.setObjectName("sendMessageBtn")
        self.messagesListWidget = QtWidgets.QListWidget(ClientUI)
        self.messagesListWidget.setGeometry(QtCore.QRect(270, 100, 711, 551))
        self.messagesListWidget.setObjectName("messagesListWidget")
        self.messagesListWidget.setStyleSheet("color: rgb(255, 255, 255); font-size:17px;")
        self.newContactBtn = QtWidgets.QPushButton(ClientUI)
        self.newContactBtn.setGeometry(QtCore.QRect(120, 70, 31, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newContactBtn.setFont(font)
        self.newContactBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.newContactBtn.setObjectName("newContactBtn")

        self.retranslateUi(ClientUI)
        QtCore.QMetaObject.connectSlotsByName(ClientUI)

    def retranslateUi(self, ClientUI):
        _translate = QtCore.QCoreApplication.translate
        ClientUI.setWindowTitle(_translate("ClientUI", "Dialog"))
        self.appNameLabel.setText(_translate("ClientUI", "Chats"))
        self.greetingsLabel.setText(_translate("ClientUI", "Good day, Sergio."))
        self.greetingsLabel_2.setText(_translate("ClientUI", "Contacts"))
        self.sendMessageBtn.setText(_translate("ClientUI", "Send"))
        self.newContactBtn.setText(_translate("ClientUI", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientUI = QtWidgets.QDialog()
    ui = Ui_ClientUI()
    ui.setupUi(ClientUI)
    ClientUI.show()
    sys.exit(app.exec_())
