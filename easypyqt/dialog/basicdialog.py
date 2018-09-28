from PyQt5 import QtWidgets
from easypyqt.widget import basicwidget


class BasicDialog(QtWidgets.QDialog):

    def __init__(self, title=None, vertical=True, auto_exec=False):
        super(BasicDialog, self).__init__()

        self.title = title or ''

        self.result_ = None  # Stores the result() as a string

        # Widgets
        self.basicWidget = basicwidget.BasicWidget(vertical=vertical)
        self.vBoxLayout = QtWidgets.QVBoxLayout()

        # Layout
        self.vBoxLayout.addWidget(self.basicWidget)
        self.setLayout(self.vBoxLayout)

        self.basic_layout = self.basicWidget.layout()

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    def reject(self):
        self.result_ = 'reject'
        super(BasicDialog, self).reject()

    def accept(self):
        self.result_ = 'accept'
        super(BasicDialog, self).accept()


if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)

    pd = BasicDialog(vertical=True)

    but = QtWidgets.QPushButton('something')
    pd.basic_layout.addWidget(but)

    pd.exec_()

    sys.exit(app.exec_())
