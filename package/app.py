from PyQt5 import QtCore, QtGui, QtWidgets
from package.ui.MainWindow import Ui_MainWindow

def run():
    QtWidgets.QApplication.setApplicationName('kiwi-steg')      
    QtWidgets.QApplication.setApplicationVersion('0.5')
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()