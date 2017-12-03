# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.setWindowModality(QtCore.Qt.WindowModal)
        login.resize(317, 194)
        login.setWindowTitle("Login")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.cboUser = QtWidgets.QComboBox(self.centralwidget)
        self.cboUser.setGeometry(QtCore.QRect(100, 40, 191, 22))
        self.cboUser.setObjectName("cboUser")
        self.txtPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPwd.setGeometry(QtCore.QRect(100, 70, 191, 20))
        self.txtPwd.setInputMask("")
        self.txtPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPwd.setClearButtonEnabled(True)
        self.txtPwd.setObjectName("txtPwd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.label.setMinimumSize(QtCore.QSize(47, 13))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 61, 20))
        self.label_2.setMinimumSize(QtCore.QSize(61, 20))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.cmdLogin = QtWidgets.QPushButton(self.centralwidget)
        self.cmdLogin.setGeometry(QtCore.QRect(90, 120, 75, 31))
        self.cmdLogin.setObjectName("cmdLogin")
        self.cmdCancel = QtWidgets.QPushButton(self.centralwidget)
        self.cmdCancel.setGeometry(QtCore.QRect(170, 120, 75, 31))
        self.cmdCancel.setObjectName("cmdCancel")
        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        self.cmdCancel.clicked.connect(login.close)
        QtCore.QMetaObject.connectSlotsByName(login)
        login.setTabOrder(self.cboUser, self.txtPwd)
        login.setTabOrder(self.txtPwd, self.cmdLogin)
        login.setTabOrder(self.cmdLogin, self.cmdCancel)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("login", "User :"))
        self.label_2.setText(_translate("login", "Password :"))
        self.cmdLogin.setText(_translate("login", "Login"))
        self.cmdCancel.setText(_translate("login", "Cancel"))

