import sys, DB_manager
from PyQt5 import QtWidgets,QtCore,QtGui
from datetime import datetime
from mysql.connector import Error
from MyConfig import MyConfigs

msgbox = QtWidgets.QMessageBox
class Ui_MainWindow(object):
    MySettings = {}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 408)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setGeometry(QtCore.QRect(30, 70, 81, 20))
        self.lbl.setMaximumSize(QtCore.QSize(81, 16777215))
        self.lbl.setText("Reader ID :")
        self.lbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl.setObjectName("lbl")
        self.txt = QtWidgets.QLineEdit(self.centralwidget)
        self.txt.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.txt.setAlignment(QtCore.Qt.AlignCenter)
        self.txt.setObjectName("txt")
        self.dt = QtWidgets.QDateEdit(self.centralwidget)
        self.dt.setEnabled(True)
        self.dt.setGeometry(QtCore.QRect(120, 10, 111, 22))
        self.dt.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dt.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dt.setSpecialValueText("")
        self.dt.setCalendarPopup(True)
        self.dt.setDate(QtCore.QDate(2017, 11, 26))
        self.dt.setObjectName("dt")
        self.cmd = QtWidgets.QPushButton(self.centralwidget)
        self.cmd.setGeometry(QtCore.QRect(240, 70, 61, 21))
        self.cmd.setText("Ok")
        self.cmd.setDefault(True)
        self.cmd.setObjectName("cmd")
        self.cbo = QtWidgets.QComboBox(self.centralwidget)
        self.cbo.setEnabled(True)
        self.cbo.setGeometry(QtCore.QRect(120, 40, 111, 20))
        self.cbo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.cbo.setEditable(False)
        self.cbo.setCurrentText("")
        self.cbo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cbo.setMinimumContentsLength(111)
        self.cbo.setFrame(False)
        self.cbo.setModelColumn(0)
        self.cbo.setObjectName("cbo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 551, 301))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(30, 10, 81, 20))
        self.lbl_2.setMaximumSize(QtCore.QSize(81, 16777215))
        self.lbl_2.setText("Current Date :")
        self.lbl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_2.setObjectName("lbl_2")
        self.lbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_3.setGeometry(QtCore.QRect(30, 40, 81, 21))
        self.lbl_3.setMaximumSize(QtCore.QSize(81, 16777215))
        self.lbl_3.setText("Department :")
        self.lbl_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_3.setObjectName("lbl_3")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.bind_Events()
        
        MainWindow.setTabOrder(self.dt, self.cbo)
        MainWindow.setTabOrder(self.cbo, self.txt)
        MainWindow.setTabOrder(self.txt, self.cmd)
        MainWindow.setTabOrder(self.cmd, self.tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def bind_Events(self):
        curdate = self.dbCon.SelectCommand("select cast(curdate() as char)")
        year,month,day = curdate[0].split('-')
        self.dt.setDate(QtCore.QDate(int(year),int(month),int(day)))
        self.txt.returnPressed.connect(self.BarcodeRead)
        self.cmd.clicked.connect(self.FillTable)
        self.FillDepartment()

    def __init__(self):
        
        cfgs = MyConfigs()
        connstring = cfgs.Get_db_config()
        self.MySettings = cfgs.Get_MySetting('MySetting')
        self.dbCon = DB_manager.DatabaseUtility(**connstring)
        
    def FillDepartment(self):
        departments = self.dbCon.SelectCommand("select `Department` from department")
        for dept in departments:
            self.cbo.addItem(dept[0])

    def FillTable(self):
        day,month,year = self.dt.text().split("/")
        dts = "-".join([year,month,day]) 
        Viscols = self.MySettings['visiblecols']
        depts = self.MySettings['departmentgroup']
        dept = self.cbo.currentText()
        table, headerlbl = self.dbCon.GetTable(
            "reader_pendingqty where ordereddate='{0}' and department in (select dept.Department from department as dept where ID in ({1}))".format(dts, str(depts)))

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(len(headerlbl))
        self.tableWidget.setHorizontalHeaderLabels(headerlbl)
        cols = self.tableWidget.columnCount()
        for i in range(0,cols):
            if str(Viscols).find(str(i)) < 0:
                self.tableWidget.setColumnHidden(i,True)
                
        for r, r_data in enumerate(table):
            self.tableWidget.insertRow(r)
            for c, data in enumerate(r_data):
                newitem = QtWidgets.QTableWidgetItem(str(data))
                if c>=3:
                    newitem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(r,c,newitem)

                

    def BarcodeRead(self):
        tkno = self.txt.text()
        try:
            tknos = tkno.split('-',1)
            tkno = int(tknos[0])
            dpt = int(tknos[1])
            grpdept = str(self.MySettings['departmentgroup'])

            if grpdept.find(tknos[1]) >= 0:
                args = [tkno, dpt]
                result_args = self.dbCon.ExecuteStoredProcedure('Insert_ReaderData', args)
            else:
                msgbox.information(MainWindow,"Invalid Department","Not Valid TokenNo with your Department Group.")
      
        except Error as e:
            msgbox.warning(MainWindow,"MySQL Error",str(e.msg))
    
        finally:
            self.txt.selectAll()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
