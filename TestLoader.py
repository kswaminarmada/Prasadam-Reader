import sys, DB_manager
from PyQt5 import QtWidgets,QtCore
from test import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dbCon = DB_manager.DatabaseUtility("autoswitch","boards")
        
    def FillTable(self):
        col = self.dbCon.GetColumns("boards")  #self.dbu.GetColumns()
        #table = self.dbcon.GetTable()
        
        headerlbl = []
        for c in range(len(col)):
            headerlbl.append(col[c][0])

        self.ui.tableWidget.setColumnCount(len(headerlbl))
        self.ui.tableWidget.setHorizontalHeaderLabels(headerlbl)
        self.ui.tableWidget.clear()

        '''
        for item in range(len(table)):
            QtGui.QTreeWidgetItem(self.treeWidget)
            for value in range(len(table[item])):
                self.treeWidget.topLevelItem(item).setText(value, str(table[item][value]))
        '''
if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())