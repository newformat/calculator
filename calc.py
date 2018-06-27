# Тут мы используем подход с конвертированным макетом дизайна.
import sys
from PyQt5 import QtWidgets
from functools import partial
from ui.form import * # сам GUI

class MainCalculator(QtWidgets.QMainWindow, Ui_MainForm):
    '''
    set_symbol      добавляет символы в поле result_show
    result          функция кнопки '='
    clear           очищает поле на -1 символ с конца.
    clear_ac        очищает буфер выражения и result_show
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self) # init GUI
        self.operators = ['/','+','*','-'] # для условий
        self.expression = [] # под выражение
        # ввод чисел
        self.pushButton_0.clicked.connect(partial(self.set_symbol, 0))
        self.pushButton_1.clicked.connect(partial(self.set_symbol, 1))
        self.pushButton_2.clicked.connect(partial(self.set_symbol, 2))
        self.pushButton_3.clicked.connect(partial(self.set_symbol, 3))
        self.pushButton_4.clicked.connect(partial(self.set_symbol, 4))
        self.pushButton_5.clicked.connect(partial(self.set_symbol, 5))
        self.pushButton_6.clicked.connect(partial(self.set_symbol, 6))
        self.pushButton_7.clicked.connect(partial(self.set_symbol, 7))
        self.pushButton_8.clicked.connect(partial(self.set_symbol, 8))
        self.pushButton_9.clicked.connect(partial(self.set_symbol, 9))
        # остальное
        self.pushButton_ac.clicked.connect(self.clears_ac)
        self.pushButton_x.clicked.connect(partial(self.set_symbol, '*'))
        self.pushButton_minus.clicked.connect(partial(self.set_symbol, '-'))
        self.pushButton_plus.clicked.connect(partial(self.set_symbol, '+'))
        self.pushButton_delit.clicked.connect(partial(self.set_symbol, '/'))
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_ravno.clicked.connect(self.result)
        self.pushButton_dot.clicked.connect(partial(self.set_symbol, '.'))
        self.pushButton_plus_minus.clicked.connect(self.append_minus)


    def set_symbol(self, data):

        if data not in self.operators:
            if self.check_dot(data): return
            self.result_show.setText(self.result_show.text() + str(data))
        elif data == '=':
            self.result()
        else:
            if len(self.expression) and (self.expression[-1] in self.operators) and (self.result_show.text() in self.operators):
                return
            elif self.result_show.text():
                self.expression.append(self.result_show.text())
                self.expression.append(data)
                self.result_show.clear()


    def check_dot(self, data):
        if self.result_show.text().count('.') and data == '.':
            return 1
        elif not self.result_show.text() and data == '.':
            return 1
        elif len(self.result_show.text()) == 1 and self.result_show.text() == '0' and data != '.':
            return 1
        return 0


    def result(self):
        if self.result_show.text():
            try:
                self.result_show.setText(str(eval(''.join(self.expression) + self.result_show.text())))
            except ZeroDivisionError:
                print('на ноль делить нельзя')
            self.expression.clear()


    def clear(self):
        if len(self.result_show.text()):
            self.result_show.setText(self.result_show.text()[:-1])


    def clears_ac(self):
        self.result_show.clear()
        self.expression.clear()


    def append_minus(self):
        if len(self.result_show.text()) and self.result_show.text()[0] == '-':
            self.result_show.setText(self.result_show.text()[1:])
        elif len(self.result_show.text()):
            self.result_show.setText("-" + self.result_show.text())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainCalculator()
    window.setFixedSize(window.width(),window.height())
    window.show()
    app.exec_()
