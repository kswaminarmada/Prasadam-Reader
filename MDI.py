import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Main import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    count = 0
	
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
            
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QtWidgets.QAction].connect(self.windowaction)
        self.setWindowTitle("MDI demo")
		
    def windowaction(self, q):
        print ("triggered")
		
        if q.text() == "New":
            MainWindow.count = MainWindow.count+1
            sub = QtWidgets.QMdiSubWindow()
            #sub.setWidget(QtWidgets.QTextEdit())
            ui = Ui_MainWindow()
            ui.setupUi(sub)
            sub.setWindowTitle("subwindow"+str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
                
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()
                
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())