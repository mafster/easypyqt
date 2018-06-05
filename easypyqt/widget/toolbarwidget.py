from PyQt5 import QtWidgets


class ToolBarWidget(QtWidgets.QToolBar):

    def __init__(self, *args, **kwargs):
        super(ToolBarWidget, self).__init__(*args, **kwargs)
