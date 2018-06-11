from easypyqt.widget import basicwidget


class ListWidget(basicwidget.BasicWidget):

    def __init__(self, vertical=True):
        super(ListWidget, self).__init__(vertical=vertical)

    def add_item(self, widget):
        self.basic_layout.addWidget(widget)

    def clear(self):
        for i in reversed(range(self.basic_layout.count())):
            self.basic_layout.itemAt(i).widget().setParent(None)