from easypyqt.widget import basicwidget


class ListWidget(basicwidget.BasicWidget):

    def __init__(self, vertical=True):
        super(ListWidget, self).__init__(vertical=vertical)

    def add_item(self, widget):
        self.main_layout.addWidget(widget)

    def clear(self):
        for i in reversed(range(self.main_layout.count())):
            self.main_layout.itemAt(i).widget().setParent(None)