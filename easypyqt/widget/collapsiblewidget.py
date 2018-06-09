from PyQt5 import QtCore, QtWidgets
from easypyqt.widget import basicwidget


class CollapsibleWidget(basicwidget.BasicWidget):

    def __init__(self, vertical=True, panel_vertical_layout=True, length=200):
        super(CollapsibleWidget, self).__init__(vertical=vertical)

        # Data
        self.length = length

        # Widget
        self.header_widget = HeaderWidget(vertical=not vertical)
        self.panel_widget = basicwidget.BasicWidget(vertical=panel_vertical_layout)

        # Layout
        self.main_layout.addWidget(self.header_widget)
        self.main_layout.addWidget(self.panel_widget)

    def add_widget_to_header(self, widget):
        self.header_widget.main_layout.addWidget(widget)

    def add_widget_to_panel(self, widget):
        self.panel_widget.main_layout.addWidget(widget)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    #from unipipe import worker

    #res = worker.ResourceWorker().get_all_resources(project='vfx_test', resource_type='component')

    cw= CollapsibleWidget()
    cw.header_widget.main_layout.addWidget(QtWidgets.QLabel('testo!'))
    cw.panel_widget.main_layout.addWidget(QtWidgets.QLabel('PANO!!'))
    cw.show()

    sys.exit(app.exec_())
