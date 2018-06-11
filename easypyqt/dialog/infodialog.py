from easypyqt.dialog import basicdialog
from PyQt5 import QtWidgets


class InfoDialog(basicdialog.BasicDialog):

    def __init__(self, message=None, vertical=True, ):
        super(InfoDialog, self).__init__(vertical=vertical)

        self.messageLabel = QtWidgets.QLabel(message or '')

        self.basic_layout.addWidget(self.messageLabel)

    def pop(self, message=None):
        """
        quick popup message  and call exec_
        :param message: *(str)* message to display. If None will take original message
        :return:
        """
        if message:
            self.messageLabel.setText(str(message))

        self.exec_()
