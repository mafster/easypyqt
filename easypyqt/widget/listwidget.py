from PyQt5 import QtWidgets


class ListWidget(QtWidgets.QListWidget):

    def __init__(self, items, *args):
        super(ListWidget, self).__init__(*args)

        if items:
            self.list_items(items)

    def list_items(self, items):

        for each in items:
            pass
