from PyQt5 import QtWidgets

from easypyqt.dialog import basicdialog


class InfoDialog(basicdialog.BasicDialog):

    def __init__(self, title: str = None, message: str = None, vertical: bool = True, auto_exec: bool = False, exception: Exception = None):
        super(InfoDialog, self).__init__(vertical=vertical, auto_exec=False)

        self.title = title or 'Info'
        self.message = message or '..'
        self.exception = exception

        if exception:
            self.message += self.build_error_message(exception)

        self.messageLabel = QtWidgets.QLabel(self.message)

        self.basic_layout.addWidget(self.messageLabel)

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    @staticmethod
    def build_error_message(exception):
        return '\n\nException: \n\n\t{}'.format(str(exception))

    def pop(self, message=None):
        """
        quick popup message  and call exec_
        :param message: *(str)* message to display. If None will take original message
        :return:
        """
        msg = str(message)

        if self.exception:
            msg += self.build_error_message(self.exception)

        self.messageLabel.setText(msg)

        self.exec_()
