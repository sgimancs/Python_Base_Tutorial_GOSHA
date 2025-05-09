# coding=utf-8
# **********************************
# Python Tkinter (sample test)
# Gosha Dudar
# **********************************
# Writing sgiman, 2025

from tkinter import *
from tkinter.messagebox import showerror

from PyQt5.QtWidgets import QMessageBox
from pyexpat.errors import messages

# Main Window
root = Tk()


# Action (button)
def btn_click():
    print("Some text")
    login = loginInput.get()
    password = passField.get()
    info_str = f'Данные: {str(login)}, {str(password)}'
    # messagebox.showinfo(title='Название', message=info_str)
    # message.showerror(title='', message='Error always!!!')

# ОКНО
root['bg'] = '#fafafa'              # background
root.title("Название программы")     # title
root.wm_attributes('-alpha', 0.7)   # transparent
root.geometry('300x250')            # size (WxH),location(XxY)

root.resizable(width=False, height=False)       # disable resizable

# ХОЛСТ
canvas = Canvas(root, width=300, height=250)    # холст для графики
canvas.pack()                                   # разместить

# ФРЕЙМ
frame = Frame(root, bg='blue')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

# МЕТКА
title = Label(frame, text="Текстовая подсказка", bg='black', fg='white', font=40)
title.pack()
# title.grid()
# title.place()

# КНОПКА
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

# ВВОД
loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show='*')
passField.pack()


root.mainloop()     # main cycle


