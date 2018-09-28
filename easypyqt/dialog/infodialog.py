from easypyqt.dialog import basicdialog
from PyQt5 import QtWidgets


class InfoDialog(basicdialog.BasicDialog):

    def __init__(self, title=None, message=None, vertical=True, auto_exec=False):
        super(InfoDialog, self).__init__(vertical=vertical)

        self.title = title or 'Info'
        self.message = message or '..'

        self.messageLabel = QtWidgets.QLabel(self.message)

        self.basic_layout.addWidget(self.messageLabel)

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    def pop(self, message=None):
        """
        quick popup message  and call exec_
        :param message: *(str)* message to display. If None will take original message
        :return:
        """
        if message:
            self.messageLabel.setText(str(message))

        self.exec_()
