# coding=utf-8
# ******************************************
# 006 - Циклы For, While, а также операторы
# Gosha Dudar, 2017
# **********************************
# Writing sgiman, 2017-2022
# Last Modification, 2025
#
# import end as end

i = 0
while i <= 10:
    print(i)
    i += 2

print("")

i = 1000
while i > 100:
    print(i)
    i /= 2

for j in 'hello world':
    #if j == 'w':
    if j == ' ':
        break               # прервать
    #print(j * 2, end='')    # с выводом в одну строку
    print(j + '-', end='')

for j in 'hello world':
    if j == 'a':
        print("\nFIND!")
        break                   # прервать
    # print(j * 3, end = '')    # с выводом в одну строку
else:
    print("\nБуквы а нету в слове")
