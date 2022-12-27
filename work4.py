#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
#3 -> [2, 3, -3, -2, -1, 0, 1]

n = int(input('Ведите число: '))
num = range(n*-1, n+1)
numbers = list(num) 
print(numbers)
numbers = numbers[-2:] + numbers[:-2]
print(numbers)