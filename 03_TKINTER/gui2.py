# coding=utf-8
# **********************************
# gui2.py
# Python Tkinter (sample test)
# **********************************
# Writing sgiman, 2025
#

from tkinter import *

#--------------------------------------------------------
# ГЛАВНОЕ ОКНО
#--------------------------------------------------------
root = Tk()  # root - main window
root.title("Графическая программа на Python")
root.geometry("400x300")

# Action (function)
clicks = 0
def click_button():
    global clicks
    clicks += 1
    root.title("Кликов {}".format(clicks))

#--------------------------------------------------------
# ФРЕЙМ
#--------------------------------------------------------
frame = Frame(root)
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)  # установить и разместить

# КНОПКА (на фрейме)
btn = Button(frame, text="Привет",  # текст кнопки
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="20",             # отступ от границ до содержимого по горизонтали
             pady="8",              # отступ от границ до содержимого по вертикали
             font="16",             # высота шрифта
             command=click_button)

btn.pack()          # разместить

root.mainloop()     # главный цикл

