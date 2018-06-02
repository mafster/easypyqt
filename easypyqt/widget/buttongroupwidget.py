from easypyqt.widget import basicwidget
from PyQt5 import QtWidgets


class ButtonGroupWidget(basicwidget.BasicWidget):
    
    BACKGROUND_GREEN = 'background-color:rgb(70, 200, 120)'
    FONT_GRAY = 'color:rgb(160, 160, 160)'

    def __init__(self, button_list=None, label=None, vertical=True, exclusive=False):
        """

        :param button_list:     *(list(tuple))* list of string tuples. [(name, label)]
        :param label:           *(str)* visible label or "title" for the button group
        :param vertical:        *(bool)* if True will lay buttons out vertically
        :param exclusive:       *(bool)* if True will highlight button clicked and ghost the rest. Button can be accessed
                                via get_exclusive_button() or get_exclusive_button_name()
        """
        super(ButtonGroupWidget, self).__init__(vertical=vertical)

        self.button_list = button_list or []
        self.exclusive = exclusive

        if label:
            label = QtWidgets.QLabel(label)
            self.layout.addWidget(label)

        for each in self.button_list:
            button = QtWidgets.QPushButton(each[1])
            button.setObjectName(each[0])
            button.exclusive = False
            button.clicked.connect(self.button_clicked)
            self.layout.addWidget(button)

    def get_all_buttons(self):
        return self.findChildren(QtWidgets.QPushButton)

    def get_button_by_name(self, name):
        """
        Returns the QPushButton that has name matching name passed
        :param name:
        :return:
        """
        for each in self.get_all_buttons():
            if each.objectName() == name:
                return each

    def button_clicked(self):
        """
        This executes when a button is clicked.

        :return:
        """
        button = self.sender()
        button.setStyleSheet(self.BACKGROUND_GREEN)

        if self.exclusive:
            print('setting button {} to True'.format(button.objectName()))
            button.exclusive = True
            for each in [x for x in self.get_all_buttons() if x.objectName() != button.objectName()]:
                print('setting button {} to False'.format(each.objectName()))
                each.exclusive = False
                each.setStyleSheet(self.FONT_GRAY)

    def get_exclusive_button(self):
        """
        :return:    *(QtGui.QPushButton)*
        """
        if not self.exclusive:
            raise RuntimeError('This ButtonGroupWidget has not been instantiated with param exclusive = True')

        for each in self.get_all_buttons():
            print('checking button: {}, exclusive: {}'.format(each.objectName(), each.exclusive))
            if each.exclusive:
                return each

    def get_exclusive_button_name(self):
        """
        :return:    *(str)* name of the exclusive button
        """
        return self.get_exclusive_button().objectName()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    buttonList = [('test1', 'TestONE'), ('test2', 'TestTWO')]
    fw = ButtonGroupWidget(button_list=buttonList, label='My Test', exclusive=True)
    fw.show()

    sys.exit(app.exec_())
