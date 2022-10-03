# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
n = int(input('Введите число: '))
element = -3
for i in range(0,n):
    element**=i
    print(element, end=" ")
    element = -3
    