# coding=utf-8
# ********************************************
# 013 - Исключения (Конструкция try - except)
# Gosha Dudar, 2017
# ********************************************
# Writing sgiman, 2017-2022
# Last Modification, 2025
# --------------------------------------------
# print (10/0)
# print (int ('qwert'))
# print ('2' + 1)

#=============================================
# TRY - EXCEPT - ELSE - FINALLY
#=============================================

print("\n*** X / Y (1) ***")
x = int(input('X = '))
y = int(input('Y = '))
try:
    res = x / y
except ZeroDivisionError:
    print("Вы ввели 0")
    res = 0
print(res)

###############################################
print("\n*** 2 ***")
try:
    x = int(input('Чиcло: '))
except ValueError:
    print("Вы ввели не число")
    x = 0
print(x)

###############################################
print("\n*** 3 ***")
print("\n*** X / Y (all try-except) ***")
try:                            # 1. попытка
    x = int(input('X = '))
except ValueError:              # 2. исключение - ошибка
    print("Вы ввели не число")
    x = 0
else:                           # 3. продолжение (без ошибки)
    print("Всё верно - X")
finally:                        # 4. финал
    print("Введен X (final)")

###############################################
print("\n*** 4 ***")
try:                            # 1. попытка
    x = int(input('Y = '))
except ValueError:              # 2. исключение - ошибка
    print("Вы ввели не число")
    y = 0
else:                           # 3. продолжение (без ошибки)
    print("Всё верно - Y")
finally:                        # 4. финал
    print("Введен Y (final)")
#..................................
try:                            # 1. попытка
    res = x / y
except ZeroDivisionError:       # 2. исключение - ошибка
    print("Вы ввели 0")
    res = 0
else:                           # 3. продолжение (без ошибки)
    print("Всё верно - X/Y")
finally:                        # 4. финал
    print("Результат Y (final)")

print('RESULT: ', res)
