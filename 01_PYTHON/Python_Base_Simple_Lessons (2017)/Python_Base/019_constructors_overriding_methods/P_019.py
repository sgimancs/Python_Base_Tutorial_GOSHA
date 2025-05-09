# coding=utf-8
# *********************************************
# 019 - Конструкторы, переопределение методов
# Gosha Dudar, 2017
# *********************************************
# Writing sgiman, 2017-2022
# Last Modification, 2025
#

# ***********
#    Класс
# ***********
class Person:
    name = "Ivan"  # Параметры
    age = 10

    def __init__(self, name, age):  # Конструктор и инициализация
        self.name = name
        self.age = age

    def set(self, name, age):       # Метод, self - содержит экземпляр класса  (аналогичен this)
        self.name = name
        self.age = age

# П О Л И М О Р Ф И З М
class Student(Person):  # Наследование основного класса Person
    course = 1          # Добавить доп. свойство

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


igor = Student("Вася", 19)         # variant 1
igor.set("Игорь", 23, 5)    # variant 2
print("\nИмя:", igor.name, ", возраст -", igor.age, ", курс -", igor.course)

print("\n*** 1 ***")
vlad = Person("Влад", 25)       # Новый объект класса Person
print(vlad.name + " " + str(vlad.age))

print("\n*** 2 ***")
ivan = Person("Иван", 56)       # Новый объект класса Person
print(ivan.name + " " + str(ivan.age))

print('-' * 80)
vasya = Student("Вася", 19)         # создать объект класса
print(vasya.name + " " + str(vasya.age))

vasya.set("Вася", 23, 5)    # задать свойства
print(vasya.name + " " + str(vasya.age)  + " " + str(vasya.course))
print('-' * 80)
