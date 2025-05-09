# coding=utf-8
# **********************************************************
# QT_002 - Библиотека PyQT5. Надписи и кнопки
# QT_004 - Всплывающие окна (QMessageBox)
# ----------------------------------------------------------
# Python 3.13.3
# jetBrain PyCharm 2024.2.3
# Designer 5.14 (Qt)
# ----------------------------------------------------------
# pip install pyqt5
# pip install pyqt5-tools
# pyuic5 -x app.ui -o app.py
# **********************************************************
# Gosha Dudar, 2023
# Writing sgiman, 2023-2025
#

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# ------------------------------------------
# КЛАСС WINDOW (наследуется от QMainWindow)
# ------------------------------------------
class Window(QMainWindow):

    # КОНСТРУКТОР
    def __init__(self):
        super(Window, self).__init__()                  # свойства родительского класса
        self.cnt = 0                                    # счётчик кликов

        # TITLE
        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 250, 350, 200)
        self.new_text = QtWidgets.QLabel(self)

        # LABEL
        self.main_text = QtWidgets.QLabel(self)         # задать текстовую метку
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        # BUTTON
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    # -------------------------
    # ДОБАВИТЬ ТЕКСТОВУЮ МЕТКУ
    # -------------------------
    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()
        self.cnt += 1
        print(f"COUNT: {self.cnt}", "add")    # action


###########################
# application() - main
###########################
def application():
    app = QApplication(sys.argv)

    # создать окно из класса Window
    window = Window()
    window.setWindowTitle("Простая программа")  # заголовок
    window.setGeometry(300, 250, 350, 200)  # геометрия

    window.show()  # отобразить окно
    sys.exit(app.exec_())  # корректное завершение


############################
# START
############################
if __name__ == "__main__":  # автозапуск приложения при старте
    application()
