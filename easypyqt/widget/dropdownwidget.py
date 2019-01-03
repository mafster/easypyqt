from PyQt5 import QtWidgets, QtCore


class DropdownWidget(QtWidgets.QComboBox):

    dropdownClicked = QtCore.pyqtSignal()
    textSelected = QtCore.pyqtSignal(str)  # Similar to the builtin activated signal but passes text name

    def __init__(self):
        super(DropdownWidget, self).__init__()

        self.activated.connect(self._text_selected)

    def _text_selected(self):
        """ """
        self.textSelected.emit(self.get_current_selection())

    def get_current_selection(self):
        """
        :return:
        """
        return str(self.currentText())

    def showPopup(self):
        self.dropdownClicked.emit()
        super(DropdownWidget, self).showPopup()
