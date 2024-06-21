#!/usr/bin/env python

"""
Playing around with QMainWindow's nested within each other
as dock widgets.
"""

from random import randint

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

_DOCK_OPTS = QtWidgets.QMainWindow.AnimatedDocks
_DOCK_OPTS |= QtWidgets.QMainWindow.AllowNestedDocks
_DOCK_OPTS |= QtWidgets.QMainWindow.AllowTabbedDocks

_DOCK_COUNT = 0
_DOCK_POSITIONS = (
    Qt.LeftDockWidgetArea,
    Qt.TopDockWidgetArea,
    Qt.RightDockWidgetArea,
    Qt.BottomDockWidgetArea
)


def add_docks(window, name):
    global _DOCK_COUNT

    for pos in _DOCK_POSITIONS:

        for _ in range(2):
            _DOCK_COUNT += 1

            sub = QtWidgets.QMainWindow()
            sub.setWindowFlags(Qt.Widget)
            sub.setDockOptions(_DOCK_OPTS)

            color = tuple(randint(20, 230) for _ in range(3))

            label = QtWidgets.QLabel("%s %d content area" % (name, _DOCK_COUNT), sub)
            label.setMinimumHeight(25)
            label.setStyleSheet("background-color: rgb(%d, %d, %d)" % color)
            sub.setCentralWidget(label)

            dock = QtWidgets.QDockWidget("%s %d title bar" % (name, _DOCK_COUNT))
            dock.setWidget(sub)

            window.addDockWidget(pos, dock)


def main():
    main_window = QtWidgets.QMainWindow()
    main_window.resize(1024, 768)
    main_window.setDockOptions(_DOCK_OPTS)

    widget = QtWidgets.QLabel("MAIN APP CONTENT AREA")
    widget.setMinimumSize(300, 200)
    widget.setFrameStyle(widget.Box)
    main_window.setCentralWidget(widget)
    main_window.centralWidget().hide()
    add_docks(main_window, "Main Dock")

    main_window.show()
    main_window.raise_()

    return main_window


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    mw = main()
    app.exec_()
