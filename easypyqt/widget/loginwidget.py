from typing import Callable, Any

from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton

from easypyqt.widget import basicwidget
from easypyqt.widget.fieldwidget import FieldWidget


class LoginWidget(basicwidget.BasicWidget):
    """
        Widget used to login to a serer
        """
    loginResult = QtCore.pyqtSignal(object)

    def __init__(self, login_process: Callable[[str, str], Any]):
        super(LoginWidget, self).__init__(vertical=False)
        self.login_process = login_process

        self.username_field = FieldWidget(label='Username')
        self.password_field = FieldWidget(label='Password', password=True)
        self.submit_button = QPushButton('Submit')

        self.submit_button.clicked.connect(self.handle_login)

        self.basic_layout.addWidget(self.username_field)
        self.basic_layout.addWidget(self.password_field)
        self.basic_layout.addWidget(self.submit_button)

    def handle_login(self):
        result = self.login_process(self.username_field.text(), self.password_field.text())
        self.loginResult.emit(result)
