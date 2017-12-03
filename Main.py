import sys, DB_manager
from PyQt5 import QtWidgets,QtCore,QtGui
from datetime import datetime
from mysql.connector import Error
from MyConfig import MyConfigs
from MySettings import Ui_Dialog

msgbox = QtWidgets.QMessageBox
class Ui_MainWindow(object):
    MySettings = {}
    DeptGrp = {}
    IsAdmin = False
    def setupUi(self, MainWindow, isAdmin=False):
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
        self.txt.setObjectName("txt")
        self.dt = QtWidgets.QDateEdit(self.centralwidget)
        self.dt.setEnabled(False)
        self.dt.setGeometry(QtCore.QRect(120, 10, 111, 22))
        self.dt.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dt.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dt.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dt.setSpecialValueText("")
        self.dt.setCalendarPopup(True)
        self.dt.setDate(QtCore.QDate(2017, 11, 26))
        self.dt.setObjectName("dt")
        self.cbo = QtWidgets.QComboBox(self.centralwidget)
        self.cbo.setEnabled(False)
        self.cbo.setGeometry(QtCore.QRect(120, 40, 111, 20))
        self.cbo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cbo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.cbo.setEditable(False)
        self.cbo.setCurrentText("")
        self.cbo.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cbo.setMinimumContentsLength(111)
        self.cbo.setFrame(False)
        self.cbo.setModelColumn(0)
        self.cbo.setObjectName("cbo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 551, 301))
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
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
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuCounter = QtWidgets.QMenu(self.menuBar)
        self.menuCounter.setObjectName("menuCounter")
        MainWindow.setMenuBar(self.menuBar)
        self.mnuSettings = QtWidgets.QAction(MainWindow)
        self.mnuSettings.setObjectName("mnuSettings")
        self.mnuDeptGrp = QtWidgets.QAction(MainWindow)
        self.mnuDeptGrp.setObjectName("mnuDeptGrp")
        self.mnuExit = QtWidgets.QAction(MainWindow)
        self.mnuExit.setObjectName("mnuExit")
        self.menuCounter.addAction(self.mnuSettings)
        self.menuCounter.addSeparator()
        self.menuCounter.addAction(self.mnuExit)
        self.menuBar.addAction(self.menuCounter.menuAction())
        
        self.retranslateUi(MainWindow)
        self.mnuExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dt, self.cbo)
        MainWindow.setTabOrder(self.cbo, self.txt)
        MainWindow.setTabOrder(self.txt, self.tableWidget)
        self.IsAdmin = isAdmin
        self.bind_Events(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuCounter.setTitle(_translate("MainWindow", "Counter"))
        self.mnuSettings.setText(_translate("MainWindow", "Settings"))
        self.mnuDeptGrp.setText(_translate("MainWindow", "Department Group"))
        self.mnuExit.setText(_translate("MainWindow", "Exit"))
        
    def bind_Events(self,MainWindow):
        curdate = self.dbCon.SelectCommand("select cast(curdate() as char)")
        year,month,day = curdate[0].split('-')
        MainWindow.setWindowTitle(self.MySettings['location'])
        self.dt.setDate(QtCore.QDate(int(year),int(month),int(day)))
        self.txt.returnPressed.connect(self.BarcodeRead)
        self.mnuSettings.triggered.connect(self.Show_SettingWindow)
        self.FillDepartment()
        self.mnuSettings.setEnabled(self.IsAdmin)
        self.dt.setEnabled(self.IsAdmin)
        self.cbo.setEnabled(self.IsAdmin)

    def __init__(self):
        cfgs = MyConfigs()
        connstring = cfgs.Get_db_config()
        self.MySettings = cfgs.Get_MySetting('MySetting')
        self.DeptGrp = cfgs.Get_MySetting('DepartmentGroup')
        self.dbCon = DB_manager.DatabaseUtility(**connstring)
        
    def FillDepartment(self):
        departments = self.DeptGrp.keys()
        self.cbo.addItems(departments)
        #for dept in departments:
        #   self.cbo.addItem(dept)
        self.cbo.setCurrentText(self.MySettings['departmentgroup'])

    def FillTable(self):
        day,month,year = self.dt.text().split("/")
        dts = "-".join([year,month,day]) 
        depts = self.get_deptIDs()
        #dept = self.cbo.currentText()
        table, headerlbl = self.dbCon.GetTable(
            "reader_pendingqty where ordereddate='{0}' and department in (select dept.Department from department as dept where ID in ({1}))".format(dts, str(depts)))
        Viscols = self.MySettings['visiblecols']
        self.tableWidget.setRowCount(0)
        if self.tableWidget.columnCount() < 1:
            self.tableWidget.setColumnCount(len(headerlbl))
            self.tableWidget.setHorizontalHeaderLabels(headerlbl)
            cols = self.tableWidget.columnCount()
            colwid = int(self.tableWidget.width() / len(str(Viscols).split(',')) )
            for i in range(0,cols):
                if str(Viscols).find(str(i)) < 0:
                    self.tableWidget.setColumnHidden(i,True)
                else:
                    self.tableWidget.setColumnWidth(i,colwid)

                
        for r, r_data in enumerate(table):
            self.tableWidget.insertRow(r)
            for c, data in enumerate(r_data):
                newitem = QtWidgets.QTableWidgetItem(str(data))
                if c>=3:
                    newitem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(r,c,newitem)

    def BarcodeRead(self):
        tkno = self.txt.text()
        if tkno.find('-') < 1: return
        try:
            tknos = tkno.split('-',1)
            tkno = int(tknos[0])
            dpt = int(tknos[1])
            grpdept = self.get_deptIDs()

            if grpdept.find(tknos[1]) >= 0:
                args = [tkno, dpt]
                result_args = self.dbCon.ExecuteStoredProcedure('Insert_ReaderData', args)
            else:
                #msgbox.information(MainWindow,"Invalid Department","Not Valid TokenNo with your Department Group.")
                pass
      
        except Error as e:
            #msgbox.warning(MainWindow,"MySQL Error",str(e.msg))
            pass
        finally:
            self.txt.selectAll()

    def Show_SettingWindow(self):
        self.dlg = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dlg)
        self.dlg.setModal(True)
        self.dlg.show()
        
    def get_deptIDs(self):
        grpName = self.cbo.currentText()
        return self.DeptGrp[grpName]

    def __del__(self):
        self.dbCon.conn.close()
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
