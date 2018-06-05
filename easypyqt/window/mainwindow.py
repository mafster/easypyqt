from PyQt5 import QtWidgets, QtCore
from easypyqt.widget import basicwidget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, name='mainWindow', title=None, vertical=True, fixedWidth=None, fixedHeight=None):
        """

        :param name:
        :param title:
        :param vertical:
        :param fixedWidth:
        :param fixedHeight:
        """

        super(MainWindow, self).__init__()

        self.title = title
        self.name = str(name)

        # Set object name and window title
        self.setObjectName(self.name)
        if title:
            self.setWindowTitle(str(title))
        else:
            self.setWindowTitle(self.name)

        self.mainWidget = basicwidget.BasicWidget(vertical=vertical)
        self.setCentralWidget(self.mainWidget)
        self.layout = self.mainWidget.layout  # overrides self.layout builtin method

        # fixed heights
        if fixedWidth:
            self.setFixedWidth(int(fixedWidth))
        if fixedHeight:
            self.setFixedWidth(int(fixedHeight))

        self.setWindowFlags(QtCore.Qt.Window)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = MainWindow(name='mainWindow')
    wdg.show()

    sys.exit(app.exec_())
