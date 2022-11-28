# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. 
#  Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Enter int -->'))
numbers = list()
result = list()

for el in range(-n,n + 1):
    numbers.append(el)
print(numbers)

s = input('Enter indexes --> ')
for i in range(0,len(s),2):
    result.append(numbers[int(s[i])])
print(result)

for m in range(0,len(result) - 1):
    result[m] *= result[m + 1]
    m += 1
print(result[m])
