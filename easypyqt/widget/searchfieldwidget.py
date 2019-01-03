from PyQt5 import QtWidgets, QtCore


class SearchFieldWidget(QtWidgets.QLineEdit):

    textEntered = QtCore.pyqtSignal(str)

    def __init__(self, string_list=None):
        super(SearchFieldWidget, self).__init__()

        self.returnPressed.connect(self._selection_made)
        self.setPlaceholderText('search..')

        # Initial
        if string_list:
            self.update_string_list(string_list)

    def _selection_made(self):
        """ Programmatically emit the selection currently made on signal textEntered """
        self.textEntered.emit(str(self.text()))

    def update_string_list(self, string_list):
        """ Recreates the string list """
        model = QtCore.QStringListModel()
        model.setStringList(string_list)

        completer = QtWidgets.QCompleter()
        completer.setModel(model)
        completer.setFilterMode(QtCore.Qt.MatchContains)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        
        self.setCompleter(completer)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    sf = SearchFieldWidget(string_list=['some', 'words', 'in', 'my', 'dictionary'])
    sf.show()

    sys.exit(app.exec_())
