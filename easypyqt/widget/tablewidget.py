from PyQt5 import QtWidgets


class TableWidget(QtWidgets.QTableWidget):
    """

    """

    def __init__(self, rows=None, columns=None, horizontal_header_list=None, vertical_header_list=None, hide_horizontal_header=False, hide_vertical_header=False):
        super(TableWidget, self).__init__()

        self.setRowCount(rows or 0)
        self.setColumnCount(columns or 0)

        if horizontal_header_list:
            self.add_horizontal_header_list(horizontal_header_list)

        if vertical_header_list:
            rows = len(vertical_header_list)
            if rows > self.rowCount():
                self.setRowCount(rows)
            self.setHorizontalHeaderLabels(vertical_header_list)

        if hide_horizontal_header:
            self.horizontalHeader().setVisible(False)

        if hide_vertical_header:
            self.verticalHeader().setVisible(False)

    def add_horizontal_header_list(self, header_list):
        """

        :param header_list:
        :return:
        """
        self.setColumnCount(len(header_list))
        self.setHorizontalHeaderLabels(header_list)

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
        :param data:    *(dict)*
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

    tab.add_row_data(data)

    sys.exit(app.exec_())
