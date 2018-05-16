from PyQt5 import QtWidgets


class BasicWidget(QtWidgets.QWidget):

    def __init__(self, vertical=True, margins=None):
        super(BasicWidget, self).__init__()

        if margins is None:
            margins = [0, 0, 0, 0]

        self.setContentsMargins(margins[0], margins[1], margins[2], margins[3])

        if vertical:
            self.layout = QtWidgets.QVBoxLayout()
        else:
            self.layout = QtWidgets.QHBoxLayout()

        self.layout.setSpacing(2)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = BasicWidget(vertical=False)
    b = QtWidgets.QPushButton('test')
    wdg.layout.addWidget(b)
    wdg.show()

    sys.exit(app.exec_())
