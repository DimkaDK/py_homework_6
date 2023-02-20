"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:
[-5,9,0,3,-1,-2,1,4,-2,1-,2,0,-9,8,10,-9,0,-5,-5,7]
5
15
Вывод: [1,9,13,14,19]
"""

import random

numberElements = int(input("Введите кол-во элементов: "))
bottomLine = int(input("Введите минимальное значение элемента: "))
upperBound = int(input("Введите максимальное значение элемента: "))

list = []
endList = []

for i in range(0, numberElements):
    list.append(random.randint(-10, 10))

print(list)

endList = [i for i in range(0, numberElements) if list[i] >= bottomLine and list[i] <= upperBound]

print(endList)
