from PyQt5 import QtCore, QtWidgets
from easypyqt.window import mainwindow


class DockingWindow(mainwindow.MainWindow):

    def __init__(self):
        super(DockingWindow, self).__init__()

        self.setWindowFlags(QtCore.Qt.Widget)
        self.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
