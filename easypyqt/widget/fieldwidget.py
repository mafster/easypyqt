from easypyqt.widget import basicwidget
from PyQt5 import QtWidgets


class FieldWidget(basicwidget.BasicWidget):

    def __init__(self, label, hint=None):
        super(FieldWidget, self).__init__(vertical=False)

        self.label = QtWidgets.QLabel(label)
        self.textField = QtWidgets.QLineEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.textField)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    fw = FieldWidget(label='test label')
    fw.show()

    sys.exit(app.exec_())
