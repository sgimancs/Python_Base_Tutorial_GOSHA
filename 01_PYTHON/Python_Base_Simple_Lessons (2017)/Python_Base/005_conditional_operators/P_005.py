# coding=utf-8
# *****************************
# 005 - Условные операторы
# Gosha Dudar, 2017
# *****************************
# Writing sgiman, 2017-2022
# Last Modification, 2025
# -----------------------------
# if
# elif
# else
# ==
# !=
# >=
# <=

if 1:
    print("True")

if 1:
    print("True\n")
    print("All is okay!")

num = input ("Введите ваше имя: ")
if num == "Test":
    print("True\n")
print("All is okay!")

num = input ("Введите число: ")
if int(num) > 0:
    if int(num) > 10:
        print("Вы ввели число больше 10")
        if int(num) > 50:
            print("Вы ввели число больше 50")
    else:
        print("Вы ввели число меньше 10 и больше 0")
elif int(num) <= -10:
    print("Вы ввели число меньше -10")
else:
    print("Вы ввели число меньше 0 и больше -10")
print("All is okay!")

# Test на присвоение
name = input("\n --> Yes/No for Test: ")
A = 'Yes' if name != "Test" else 'No'
print(A)

