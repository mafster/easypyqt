from PyQt5 import QtWidgets


class GridWidget(QtWidgets.QWidget):
    """
        Create a Widget with a Grid Layout

    """
    def __init__(self, rows=None, columns=None):
        super(GridWidget, self).__init__()

        if rows:
            self.rows = rows

        if columns:
            self.columns = columns

        self.layout = QtWidgets.QGridLayout()

        self.setLayout(self.layout)
