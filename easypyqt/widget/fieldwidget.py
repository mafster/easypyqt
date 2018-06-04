from easypyqt.widget import basicwidget
from PyQt5 import QtWidgets


class FieldWidget(basicwidget.BasicWidget):

    def __init__(self, label, hint=None):
        super(FieldWidget, self).__init__(vertical=False)

        self.label = QtWidgets.QLabel(label)
        self.text_field = QtWidgets.QLineEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_field)

    def get_text(self):
        """ Return text contained in the QLineEdit """
        return self.text_field.text()


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    fw = FieldWidget(label='test label')
    fw.show()

    sys.exit(app.exec_())
