# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LoginForm(object):
    def __init__(self):
        self.login = None
        self.password = None

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(548, 388)
        Form.setStyleSheet("background-color: rgb(41, 41, 41);")
        self.appName = QtWidgets.QLabel(Form)
        self.appName.setGeometry(QtCore.QRect(220, 60, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(28)
        self.appName.setFont(font)
        self.appName.setStyleSheet("color: rgb(255, 255, 255);")
        self.appName.setObjectName("appName")
        self.loginLineEdit = QtWidgets.QLineEdit(Form)
        self.loginLineEdit.setGeometry(QtCore.QRect(160, 130, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginLineEdit.setFont(font)
        self.loginLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(Form)
        self.passwordLineEdit.setGeometry(QtCore.QRect(160, 180, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.loginBtn = QtWidgets.QPushButton(Form)
        self.loginBtn.setGeometry(QtCore.QRect(160, 240, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loginBtn.setFont(font)
        self.loginBtn.setStyleSheet("border-radius:20px;\n"
"color:white;")
        self.loginBtn.setObjectName("loginBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.loginBtn.clicked.connect(self.get_login_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.appName.setText(_translate("Form", "chats"))
        self.loginLineEdit.setText(_translate("Form", "login"))
        self.passwordLineEdit.setText(_translate("Form", "password"))
        self.loginBtn.setText(_translate("Form", "Login"))

    def get_login_data(self, Form):
        self.login = self.loginLineEdit.text()
        self.password = self.passwordLineEdit.text()
        self.Form.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = LoginForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
