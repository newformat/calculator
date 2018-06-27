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
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self) # init GUI
        self.operators = ['/','+','*','-', '.'] # для условий
        self.was_operation = 0  # индикатор "были ли операции с числами?"
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
        self.pushButton_ac.clicked.connect(self.result_show.clear)
        self.pushButton_x.clicked.connect(partial(self.set_symbol, '*'))
        self.pushButton_minus.clicked.connect(partial(self.set_symbol, '-'))
        self.pushButton_plus.clicked.connect(partial(self.set_symbol, '+'))
        self.pushButton_delit.clicked.connect(partial(self.set_symbol, '/'))
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_ravno.clicked.connect(self.result)
        self.pushButton_dot.clicked.connect(partial(self.set_symbol, '.'))
        # не доработаные (отключены)
        self.pushButton_plus_minus.setDisabled(True)
        self.pushButton_proc.setDisabled(True)


    def set_symbol(self, data):
        if self.was_operation == 1:
            self.was_operation = 0
            self.result_show.clear()

        if len(self.result_show.text()):
            if self.result_show.text()[-1] in self.operators and data in self.operators:
                return
            self.result_show.setText(self.result_show.text() + str(data))
        elif data not in self.operators:
            self.result_show.setText(self.result_show.text() + str(data))


    def result(self):
        try:
            if len(self.result_show.text()) >=3:
                if self.result_show.text()[-1] not in self.operators:
                    self.result_show.setText(str(eval(self.result_show.text())))
                    self.was_operation = 1
        except SyntaxError:
            return


    def clear(self):
        if len(self.result_show.text()):
            self.result_show.setText(self.result_show.text()[:-1])
            self.was_operation = 0



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainCalculator()
    window.show()
    app.exec_()
