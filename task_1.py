# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
n = int(input('Введите число: '))
element = 1
print(element, end = " ")
for i in range(1,n+3,2):
    if i%2 == 0:
        element *=3
        print(element, end=" ")
    else:
        element *=-3
        print(element, end=" ")