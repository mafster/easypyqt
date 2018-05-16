from PyQt5 import QtWidgets
from easypyqt.widget import basicwidget


class BasicDialog(QtWidgets.QDialog):

    def __init__(self, vertical=True):
        super(BasicDialog, self).__init__()

        self.basicWidget = basicwidget.BasicWidget(vertical=vertical)
        self.vBoxLayout = QtWidgets.QVBoxLayout()

        self.setLayout(self.vBoxLayout)

        self.vBoxLayout.addWidget(self.basicWidget)
        self.layout = self.basicWidget.layout


if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)

    pd = BasicDialog(vertical=True)

    but = QtWidgets.QPushButton('something')
    pd.layout.addWidget(but)

    pd.exec_()

    sys.exit(app.exec_())
