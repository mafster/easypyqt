from PyQt5 import QtWidgets, QtCore


class DropdownWidget(QtWidgets.QComboBox):

    dropdown_clicked = QtCore.pyqtSignal()
    text_selected = QtCore.pyqtSignal(str)

    def __init__(self):
        super(DropdownWidget, self).__init__()

    def get_current_selection(self):
        """
        :return:
        """
        return str(self.currentText())

    def showPopup(self):
        self.dropdown_clicked.emit()
        super(DropdownWidget, self).showPopup()
