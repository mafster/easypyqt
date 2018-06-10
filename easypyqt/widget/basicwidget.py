from PyQt5 import QtWidgets
import OnionLogger


class BasicWidget(QtWidgets.QWidget):

    def __init__(self, vertical=True, margins=None):
        super(BasicWidget, self).__init__()

        if margins is None:
            margins = [0, 0, 0, 0]

        self.setContentsMargins(margins[0], margins[1], margins[2], margins[3])

        if vertical:
            self.main_layout = QtWidgets.QVBoxLayout()
        else:
            self.main_layout = QtWidgets.QHBoxLayout()

        self.main_layout.setSpacing(2)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)

        self.log = OnionLogger.Logger(__name__)

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = BasicWidget(vertical=False)
    b = QtWidgets.QPushButton('test')
    wdg.main_layout.addWidget(b)
    wdg.show()

    sys.exit(app.exec_())
