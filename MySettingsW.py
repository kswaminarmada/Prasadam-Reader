from PyQt5 import QtCore, QtGui, QtWidgets
from MyConfig import MyConfigs
import DB_manager

msgbox = QtWidgets.QMessageBox
class Ui_Dialog(QtWidgets.QDialog):
    MySettings = {}
    dbConnection = {}
    DeptGroups = {}
    changedgroupname = ''
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.setWindowFilePath("")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(230, 270, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabdbConnection = QtWidgets.QWidget()
        self.tabdbConnection.setObjectName("tabdbConnection")
        self.formLayoutWidget = QtWidgets.QWidget(self.tabdbConnection)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 40, 221, 144))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txthost = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txthost.setObjectName("txthost")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txthost)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtdatabase = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtdatabase.setObjectName("txtdatabase")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtdatabase)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtuser = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtuser.setObjectName("txtuser")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtuser)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtpwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtpwd.setObjectName("txtpwd")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtpwd)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtport = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtport.setObjectName("txtport")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtport)
        self.tabWidget.addTab(self.tabdbConnection, "Data Connection")
        self.tabMySettings = QtWidgets.QWidget()
        self.tabMySettings.setObjectName("tabMySettings")
        self.label_6 = QtWidgets.QLabel(self.tabMySettings)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tabMySettings)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 61, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lstVisCols = QtWidgets.QListWidget(self.tabMySettings)
        self.lstVisCols.setGeometry(QtCore.QRect(110, 90, 131, 111))
        self.lstVisCols.setObjectName("lstVisCols")
        self.label_8 = QtWidgets.QLabel(self.tabMySettings)
        self.label_8.setGeometry(QtCore.QRect(0, 50, 101, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.cboDeptGrp = QtWidgets.QComboBox(self.tabMySettings)
        self.cboDeptGrp.setGeometry(QtCore.QRect(110, 50, 241, 22))
        self.cboDeptGrp.setObjectName("cboDeptGrp")
        self.txtLocation = QtWidgets.QLineEdit(self.tabMySettings)
        self.txtLocation.setGeometry(QtCore.QRect(110, 20, 151, 20))
        self.txtLocation.setObjectName("txtLocation")
        self.tabWidget.addTab(self.tabMySettings, "Counter Settings")
        self.tabDeptGrp = QtWidgets.QWidget()
        self.tabDeptGrp.setAccessibleName("")
        self.tabDeptGrp.setAccessibleDescription("")
        self.tabDeptGrp.setObjectName("tabDeptGrp")
        self.label_9 = QtWidgets.QLabel(self.tabDeptGrp)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 91, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.lstDepartment = QtWidgets.QListWidget(self.tabDeptGrp)
        self.lstDepartment.setGeometry(QtCore.QRect(120, 40, 241, 192))
        self.lstDepartment.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lstDepartment.setObjectName("lstDepartment")
        self.cmdSaveGroups = QtWidgets.QPushButton(self.tabDeptGrp)
        self.cmdSaveGroups.setGeometry(QtCore.QRect(40, 210, 75, 23))
        self.cmdSaveGroups.setObjectName("cmdSaveGroups")
        self.cboGroupName = QtWidgets.QComboBox(self.tabDeptGrp)
        self.cboGroupName.setGeometry(QtCore.QRect(120, 10, 241, 22))
        self.cboGroupName.setEditable(True)
        self.cboGroupName.setObjectName("cboGroupName")
        self.label_10 = QtWidgets.QLabel(self.tabDeptGrp)
        self.label_10.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tabDeptGrp, "Department Group")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.tabWidget, self.txtLocation)
        self.setTabOrder(self.txtLocation, self.cboDeptGrp)
        self.setTabOrder(self.cboDeptGrp, self.lstVisCols)
        self.setTabOrder(self.lstVisCols, self.cboGroupName)
        self.setTabOrder(self.cboGroupName, self.lstDepartment)
        self.setTabOrder(self.lstDepartment, self.cmdSaveGroups)
        self.Bind_Events()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Settings"))
        self.label.setText(_translate("Dialog", "Host :"))
        self.label_2.setText(_translate("Dialog", "Database :"))
        self.label_3.setText(_translate("Dialog", "User :"))
        self.label_4.setText(_translate("Dialog", "Password :"))
        self.label_5.setText(_translate("Dialog", "Port :"))
        self.label_6.setText(_translate("Dialog", "Visible Columns :"))
        self.label_7.setText(_translate("Dialog", "Location :"))
        self.label_8.setText(_translate("Dialog", "Department Group :"))
        self.label_9.setText(_translate("Dialog", "Group Name :"))
        self.cmdSaveGroups.setText(_translate("Dialog", "Save Groups"))
        self.label_10.setText(_translate("Dialog", "Select Department :"))
        
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        cfgs = MyConfigs()
        self.dbConnection = cfgs.Get_db_config()
        self.MySettings = cfgs.Get_MySetting('MySetting')
        self.DeptGroups = cfgs.Get_MySetting('DepartmentGroup')
        self.dbCon = DB_manager.DatabaseUtility(**self.dbConnection)

    def SetSettingValues(self,SettingName='dbConnection'):
        try:
            if SettingName == 'dbConnection' or 'All' :
                self.txthost.setText(self.dbConnection['host'])
                self.txtdatabase.setText(self.dbConnection['database'])
                self.txtuser.setText(self.dbConnection['user'])
                self.txtpwd.setText(self.dbConnection['password'])
                self.txtport.setText(self.dbConnection['port'])
                self.txtLocation.setText(self.MySettings['location'])
                self.cboDeptGrp.setCurrentText(self.MySettings['departmentgroup'])
                self.cboGroupName.currentText = self.MySettings['departmentgroup']
                self.set_lstVisCol(self.MySettings['visiblecols'])
                self.load_Department()
                self.load_DepartmentGroup()
                self.changedgroupname = self.cboGroupName.currentText
                
        except :
            msgbox.warning(Dialog,"Something wrong","Error while setting values")
            
    def Bind_Events(self):
        self.SetSettingValues()
        self.cboGroupName.currentIndexChanged[int].connect(self.cboGroupName_currentIndexChanged)
        self.tabWidget.tabBarClicked[int].connect(self.tabDeptGrp_Clicked)
        self.cboGroupName.editTextChanged[str].connect(self.cboGroupName_EditTextChanged)
        self.cmdSaveGroups.clicked.connect(self.SaveGroups)
        self.buttonBox.accepted.connect(self.SaveSettings)
    
    def set_lstVisCol(self,VisibleCols=""):
        tbl,cols = self.dbCon.GetTable("reader_pendingqty where 1=0")
        self.lstVisCols.clear()
        self.lstVisCols.addItems(cols)
        for indx in range(0,self.lstVisCols.count()):
            itm = self.lstVisCols.item(indx)
            itm.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            itm.setCheckState(QtCore.Qt.Unchecked)
            if VisibleCols.find(str(indx))>=0:
                itm.setCheckState(QtCore.Qt.Checked)
                
    def get_lstVisCol(self):
        cols= []
        for indx in range(0,self.lstVisCols.count()):
            itm = self.lstVisCols.item(indx)
            if itm.checkState() == QtCore.Qt.Checked:
                cols.append(str(indx))
        
        return ",".join(cols)

    def get_SelectedGrpDept(self):
        cols= []
        for indx in range(0,self.lstDepartment.count()):
            itm = self.lstDepartment.item(indx)
            if itm.checkState() == QtCore.Qt.Checked:
                cols.append(str(indx+1))
        
        return ",".join(cols)

    def load_DepartmentGroup(self):
        for itm in self.DeptGroups.items():
            self.cboDeptGrp.addItem(itm[0])
            self.cboGroupName.addItem(itm[0])

        self.cboDeptGrp.currentText = self.MySettings['departmentgroup']
        self.cboGroupName.currentText = self.MySettings['departmentgroup']
        self.cboGroupName.setCurrentText(self.changedgroupname)

    def cboGroupName_currentIndexChanged(self,ind):
        for grps in self.DeptGroups.items():
            if grps[0] == self.cboGroupName.itemText(ind) :
                for indx in range(self.lstDepartment.count()):
                    itm = self.lstDepartment.item(indx)
                    if str(grps[1]).find(str(indx+1))>=0:
                        itm.setCheckState(QtCore.Qt.Checked)
                    else:
                        itm.setCheckState(QtCore.Qt.Unchecked)

    def load_Department(self):
        departments = self.dbCon.SelectCommand("select `Department` from department order by ID")
        self.lstDepartment.setSortingEnabled(False)
        for dept in departments:
            itm = QtWidgets.QListWidgetItem(self.lstDepartment) 
            itm.setText(dept[0])
            itm.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            itm.setCheckState(QtCore.Qt.Unchecked)

    def tabDeptGrp_Clicked(self,indx):
        if self.tabWidget.tabText(indx) == "Department Group":
            if self.cboGroupName.count() > 0:
                indx = self.cboGroupName.findText(self.cboGroupName.currentText)
                self.cboGroupName_currentIndexChanged(indx)

    def SaveGroups(self):
        if len(self.changedgroupname)>0:
            isNew = True
            for grp in self.DeptGroups.items():
                if str(grp[0]).lower() == str(self.changedgroupname).lower():
                    isNew = False
                    break 

            if isNew :
                e={}
                e[self.changedgroupname] = self.get_SelectedGrpDept()
                self.DeptGroups.update(e)
                msgbox.information(self,'New Group','Group : {0} , Added  successfully.'.format(self.changedgroupname))
            else:
                self.DeptGroups[self.changedgroupname] = self.get_SelectedGrpDept()
                msgbox.information(self,'Update Group','Group : {0} , Updated successfully.'.format(self.changedgroupname))

            #cfgs.WriteConfig('DepartmentGroup',self.DeptGroups)
            self.load_DepartmentGroup()
        else:
            msgbox.information(self,'','Please, Select or Create Group.')

    def cboGroupName_EditTextChanged(self,txt):
        self.changedgroupname = txt

    def SaveSettings(self):
        cfgs = MyConfigs()
            
        self.dbConnection['host']= self.txthost.text()
        self.dbConnection['database']= self.txtdatabase.text()
        self.dbConnection['user']= self.txtuser.text()
        self.dbConnection['password']= self.txtpwd.text()
        self.dbConnection['port']= self.txtport.text()

        self.MySettings['visiblecols'] = self.get_lstVisCol()
        self.MySettings['departmentgroup'] = self.cboDeptGrp.currentText
        self.MySettings['location'] = self.txtLocation.text()

        cfgs.WriteConfig('dbConnection',self.dbConnection)
        cfgs.WriteConfig('MySetting',self.MySettings)
        cfgs.WriteConfig('DepartmentGroup',self.DeptGroups)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Ui_Dialog()
    Dialog.setupUi()
    Dialog.show()
    sys.exit(app.exec_())

