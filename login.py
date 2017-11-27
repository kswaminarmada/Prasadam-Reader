from PyQt5 import QtCore, QtGui, QtWidgets
import DB_manager
from Main import Ui_MainWindow

msgbox = QtWidgets.QMessageBox

class Ui_login(object):
    def __init__(self):
        self.dbCon = DB_manager.DatabaseUtility("prasadam")
    
    def Mainwinshow(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        login.hide()
        self.MainWindow.show()
        
    def checklogin(self):
        user = self.cboUser.currentText()
        pwd = self.txtPwd.text()
        tbl = self.dbCon.GetTable("users where UserName = '{0}' and Password = '{1}'".format(user,pwd))
        if len(tbl)> 0:
            self.Mainwinshow()
        else:
            msgbox.information(login,"Invalid Credentials","Invalid Password, try Again",msgbox.Ok)
            self.txtPwd.setFocus() 

    def FillUsers(self):
        tbl = self.dbCon.RunCommand("select UserName from users")
        for usr in tbl:
            self.cboUser.addItem(usr[0])

    def setupUi(self, login):
        login.setObjectName("login")
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
        self.cmdLogin.clicked.connect(self.checklogin)
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
        self.FillUsers()

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("login", "User :"))
        self.label_2.setText(_translate("login", "Password :"))
        self.cmdLogin.setText(_translate("login", "Login"))
        self.cmdCancel.setText(_translate("login", "Cancel"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

