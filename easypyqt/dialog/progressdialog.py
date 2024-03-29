from typing import Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QProgressBar


class ProgressDialog(QtWidgets.QProgressDialog):

    def __init__(self):
        super(ProgressDialog, self).__init__()

        # self.progress_dialog = QtWidgets.QProgressDialog("Operation in progress.", "Cancel", 0, 0, self)
        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Please Wait")
        # self.progressBar = QProgressBar()
        # self.progressBar.setRange(0, 100)
        # self.layout().addWidget(self.progressBar)
        self.setCancelButton(None)  # Disallow canceling
        self.setRange(0, 100)  # Spinner mode (not a progress bar)
        self.setMinimumDuration(3000)
        self.close()  # Start out hidden

    def show(self, title: Optional[str] = None) -> None:
        if title:
            self.setWindowTitle(title)
        super(ProgressDialog, self).show()
