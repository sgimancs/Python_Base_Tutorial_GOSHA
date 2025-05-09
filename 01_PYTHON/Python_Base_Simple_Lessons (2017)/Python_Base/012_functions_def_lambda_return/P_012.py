# coding=utf-8
# ************************************
# 012 - Функции (def, lambda, return)
# Gosha Dudar, 2017
# ****************************************
# Writing sgiman, 2017-2022
# Last Modification, 2025

print('\n*** 1 ***')

def func(x):
    return x

print(func(23))

###########################################
print("\n*** 2 ***")

def func(x, a):
    return x + a

print(func(23, 12))

###########################################
print("\n*** 3 ***")

def func(x, a):
    return x + a

print(func('Hello', ' World!'))

###########################################
print("\n*** 4 ***")

def func(x, a):
    res = x + a
    return res

print(func('Hello', ' World!'))

###########################################
print("\n*** 5 ***")

def func(x):
    def adding(a):
        return x + a

    return adding

test = func(100)  # подготовка: получить ссылку на функцию test с первым аргументов 100
print(test(250))  # результат после выполнения test
print("\n*** Empty Function ***")

###########################################
print("\n*** 6 ***")

def func():
    pass

print(func())

###########################################
print("\n*** 7 ***")

def func(r, w, y=2):
    return r + w + y

print(func(2, 4))           # могут быть только 2 аргумента
print(func(2, 4, 5))     # все аргументы

###########################################
print("\n*** 8 ***")

def func(*args):
    return args

print(func('sd', 4, 34.33))            # кортеж параметров

###########################################
print("\n*** 9 ***")

def func(**args):
    return args

print(func(a=23, n=56, o=90))                 # словарь параметров
print(func(short='dict', longer='dictionary'))

###########################################
print("\n*** 10 ***")

#---------------------------
# lambda
#---------------------------
print("\n*** lambda ***")                     # анонимные функции
add = lambda x, y: x * y
print(add(2, 5))
print(add('q', 5))

print((lambda x, y: x * y)(2, 6))       # сокращенная запись в одну строку

#-----------------------------------------------------------------------------
# *args - кортеж параметров - (2, 56, 78.56)
# **args - словарь параметров - {'a': 23, 'n': 56, 'o': 90}
#-----------------------------------------------------------------------------
print("\n*** 11 ***")

fun1 = lambda *args: args                     # кортеж параметров
print(fun1(2, 56, 78.56))

fun2 = lambda **args: args                    # словарь параметров
print(fun2(a=23, n=56, o=90))

