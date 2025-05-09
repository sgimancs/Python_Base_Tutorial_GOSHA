# coding=utf-8
# ****************************************
# 010 - Словари (dict), а также их методы
# Gosha Dudar, 2017
# ****************************************
# Writing sgiman, 2017-2022
# Last Modification, 2025
# ----------------------------------------
# key : value
#

# -1-
print("\n*** LIST DICTIONARY ***")
d = {'test': 1, 'test_2': "TeST"}
print(d)
print('test: ', d['test'])
print('test_2:', d['test_2'])
print('-' * 80)

# -2-
print("\n*** DICTIONARY ***")
d = dict(short='dict', longer='dictionary')
print(d)            # {'short': 'dict', 'longer': 'dictionary'}
d['short'] = 234
print(d)            # {'short': 234, 'longer': 'dictionary'}
print('-' * 80)

# -3-
# Словарь в виде списка с кортежами - (key, value)
d = dict([(23, 24), (56, 87)])
print(d)            # {23: 24, 56: 87}
print('-' * 80)

# -4-
# Словарь из ключей
d = dict.fromkeys(['a', 'b', 'c'], 1)           # заполнить все ключи value = 1
print (d)                                                       # {'a': 1, 'b': 1, 'c': 1}
d = dict.fromkeys(['a', 'b', 'c'], [1, 2, 3])   # заполнить все ключи списком
print (d)                                                       # {'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}
print('-' * 80)

# -5-
# заполнение словаря циклом итераций
d = {a: a ** 2 for a in range(10)}   # 10 циклов для степени 2
#print(range(10))                    # range(0, 10)
print(d)                             # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print('-' * 80)

# СЛОВАРЬ = {словарь{ФИО} - список[АДРЕС] - словарь{ТЕЛЕФОНЫ}}
print("\n*** PERSON ***")

# Словарь с вложениями
person = {
    'name': {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'},               # словарь: (ФИО)
    'address': ['r.Андрюшки', 'ул.Васильковская д. 236', 'кв.12'],                                  # список: адрес (город, улица/дом, квартира)
    'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23=65', 'mobile_phone_2': 'Нет'} # словарь: телефоны (тип : номер)
}

print('СЛОВАРЬ: ', person)
print('.' * 80)

print(person['name']['first_name'])     # имя
print(person['name']['last_name'])      # фамилия
print(person['address'][0])             # город
print(person['address'][1])             # улица/дом
print(person['phone']['mobile_phone'])  # телефон
print('.' * 80)

print(person.values())  # Вывести все значения из словаря
print(person.keys())    # Вывести все ключи из словаря
print('.' * 80)

person.clear()          # Очиcтить словарь
print(person)
print('-' * 80)
