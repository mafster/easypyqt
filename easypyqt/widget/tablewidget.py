from PyQt5 import QtCore, QtGui, QtWidgets


class TableWidget(QtWidgets.QTableWidget):
    """

    """

    def __init__(self, rows=None, columns=None, horizontal_header_list=None, vertical_header_list=None):
        super(TableWidget, self).__init__()

        self.setRowCount(rows or 0)
        self.setColumnCount(columns or 0)

        if horizontal_header_list:
            self.add_horizontal_header_list(horizontal_header_list)
        else:
            self.horizontalHeader().setVisible(False)

        if vertical_header_list:
            self.add_vertical_header_list(vertical_header_list)
        else:
            self.verticalHeader().setVisible(False)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.display_menu)

    def display_menu(self, pos):
        """ implement menu in subclass """
        pass

    def add_horizontal_header_list(self, header_list):
        """

        :param header_list:
        :return:
        """
        self.setColumnCount(len(header_list))
        self.setHorizontalHeaderLabels(header_list)

    def add_vertical_header_list(self, header_list):
        rows = len(header_list)
        if rows > self.rowCount():
            self.setRowCount(rows)
        self.setVerticalHeaderLabels(header_list)

    def get_next_empty_row(self):
        return self.rowCount()

    def get_column_from_header_name(self, header_name):
        """
        Return the column index with header name matching name passed

        :param header_name: *(str)* name of header
        :return:
        """
        for idx in range(self.columnCount()):
            item = self.horizontalHeaderItem(idx)
            if item.text() == header_name:
                return idx

        return None

    def get_all_items_in_column(self, column):
        items = []

        for row in range(self.rowCount()):
            items.append(self.item(row, column))

        return items

    def add_row(self, data):
        """
        Add a single row of data. Simple dict, 1 level deep
        :param data:    *(dict)*
        :return:
        """
        row = self.get_next_empty_row()
        self.insertRow(row)

        for key, value in data.items():

            entry_widget = QtWidgets.QTableWidgetItem(str(value))
            col = self.get_column_from_header_name(header_name=key)
            if col is None:
                # TODO: Potentially create a new column?
                pass
            else:
                self.setItem(row, col, entry_widget)

    def add_row_data(self, data):
        """
        Add multiple rows of data. Dictionary, 2 levels deep.
        :param data:    *(dict(dict))*
        :return:
        """
        for key, value in data.keys():
            self.add_row(value)


if __name__ == '__main__':

    import sys
    import collections

    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    data = collections.OrderedDict()

    data['name'] = 'ball'
    data['project'] = 'test_project'
    data['resource_type'] = 'component'

    tab = TableWidget(horizontal_header_list=data.keys())
    tab.show()

    tab.add_row(data)

    sys.exit(app.exec_())
