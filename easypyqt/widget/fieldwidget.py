from easypyqt.widget import basicwidget
from PyQt5 import QtWidgets


class FieldWidget(basicwidget.BasicWidget):

    def __init__(self, label, default=None, hint=None, tool_tip=None):
        super(FieldWidget, self).__init__(vertical=False)

        self.label = QtWidgets.QLabel(label)
        self.text_field = QtWidgets.QLineEdit()

        self.basic_layout.addWidget(self.label)
        self.basic_layout.addWidget(self.text_field)

        if tool_tip:
            self.text_field.setToolTip(str(tool_tip))

        if hint:
            self.text_field.setPlaceholderText(str(hint))

        if default:
            self.text_field.setText(str(default))

    def get_text(self):
        """ Return text contained in the QLineEdit """
        return self.text_field.text()

    def __getattr__(self, item):
        """ Attempt pass through most calls to the text_field """
        try:
            return getattr(self.text_field, item)
        except AttributeError:
            return super(FieldWidget, self).__getattribute__(item)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    fw = FieldWidget(label='test label', hint='default', tool_tip='please')
    fw.show()

    sys.exit(app.exec_())
