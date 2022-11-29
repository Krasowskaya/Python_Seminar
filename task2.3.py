# Задайте список из n чисел последовательности (1 + 1/n)^n 
# и выведите на экран их сумму.

# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input('Enter N --> '))
numbers = list()
sum = 0

for el in range(1, n + 1):
    numbers.append((1 + 1 / el)**el)
    el += 1
print(numbers)

for i in range(0,len(numbers)):
    sum += numbers[i]
print('Сумма: ', sum)


