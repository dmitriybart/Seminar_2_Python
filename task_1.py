# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
n = int(input('Введите чиссло: ')
element = 1
print(element, end = " ")
for i range (n-1):
    if i%2 == 0:
        element *=3
        print(element, end=" ")
    else:
        element *= -3
        print(element, end=" ")