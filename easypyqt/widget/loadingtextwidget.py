from typing import Optional

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QLabel

from easypyqt.utils import center_widget_in_another
from easypyqt.widget import basicwidget


class LoadingTextWidget(basicwidget.BasicWidget):
    def __init__(self, text: str, title: Optional[str] = '', time_interval: Optional[int] = 50, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = text
        self.timer = QTimer(self)
        self.time_interval = time_interval
        self.loading_label = QLabel(self)
        self.setWindowTitle(title)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setFixedSize(300, 80)

        self.loading_label.setAlignment(Qt.AlignCenter)
        self.basic_layout.addWidget(self.loading_label)

        # Set to centre of screen
        center_widget_in_another(self, self.parent())

        self.timer.timeout.connect(self.update_loading_text)

    def start_and_show(self):
        self.timer.start(self.time_interval)
        self.show()

    def update_loading_text(self):
        current_text = self.loading_label.text()
        if len(current_text) < len(self.text):
            self.loading_label.setText(current_text + self.text[len(current_text)])
        else:
            self.loading_label.setText('')
