# coding=utf-8
# ********************
# 007 - Списки (list)
# Gosha Dudar, 2017
# **********************************
# Writing sgiman, 2017-2022
# Last Modification, 2025
#

l = []  # пустой список
lst = [1, 56, 'x', 34, 1.34, ['S', 't', 'r', 'o', 'k', 'a']]
print(lst)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u'] # обработка строк "list" и "soup" (пропуск литер)
print('LIST+SOUP: ', a)

print('-' * 80)
l.append(23)        # добавляет элемент
l.append(34)
b = [24, 67]
l.extend(b)         # расширяет другим списком
l.insert(1, 60)     # вставляет по индексу
l.append(34)
l.remove(34)        # удаляет первый элемент при совпадении
l.pop()             # удаляет последний или i-тый элемент
print(l.index(24))  # определить индекс
print(l.count(34))  # возвращает номер индекса
l.sort()            # сортировка
l.reverse()         # реверсирование
l.clear()           # очистить список

print(l)
print('-' * 80)

# МНОЖЕСТВА (SET)
nums = {1,2,3,4,5,1,3,5,0}  # mums - SET без дублей (не индексируется, изменяется)
arr = [1,2,3,4,5,1,3,5,0]   # arr - LIST c дублями (индексируется и изменяется)
tpl = 1,2,3,4,5,1,3,5,0     # tpl - TUPLE c дублями (индексируется, не изменяется)

print('SET: ', nums)
for n in nums:
    print(n**2, end=' ')

print('\nLIST:', arr)
print('LIST:', arr[0])

print('TUPLES: ', tpl)
print('TUPLES: ', tpl[0])

