from PyQt5 import QtWidgets


class TableWidget(QtWidgets.QTableWidget):
    """

    """

    def __init__(self, rows=None, columns=None, horizontalHeaderList=None, verticalHeaderList=None, hideHorizontalHeader=False, hideVerticalHeader=False):
        super(TableWidget, self).__init__()

        self.setRowCount(rows or 0)
        self.setColumnCount(columns or 0)

        if horizontalHeaderList:
            self.setColumnCount(len(horizontalHeaderList))
            self.setHorizontalHeaderLabels(horizontalHeaderList)

        if verticalHeaderList:
            rows = len(verticalHeaderList)
            if rows > self.rowCount():
                self.setRowCount(rows)
            self.setHorizontalHeaderLabels(verticalHeaderList)

        if hideHorizontalHeader:
            self.horizontalHeader().setVisible(False)

        if hideVerticalHeader:
            self.verticalHeader().setVisible(False)
