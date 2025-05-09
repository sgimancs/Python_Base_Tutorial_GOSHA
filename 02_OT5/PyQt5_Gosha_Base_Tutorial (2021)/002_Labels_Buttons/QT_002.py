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
# ----------------------------------------------------------
# PyQt — это свободное программное обеспечение,
# разработанное британской фирмой Riverbank Computing.
# **********************************************************
# Gosha Dudar, 2023
# Writing sgiman, 2023-2025
#

# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

###########################
# MAIN APPLICATION (MAIN)
###########################
def application():
    app = QApplication(sys.argv)

    # создать окно из класса Window
    window = QMainWindow()
    # window = Window()
    window.setWindowTitle("Простая программа")  # заголовок
    window.setGeometry(300,250,350,200)         # геометрия

    window.show()           # отобразить окно
    sys.exit(app.exec_())   # корректное завершение


############################
# START
############################
if __name__ == "__main__":
    application()
