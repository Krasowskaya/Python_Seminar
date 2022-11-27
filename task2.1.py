# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:
# 0,56 -> 11

n = str(input('Enter -->'))
n2 = '.'
while n2 in n:
    n = n.replace(n2,'0',1)
# print(n)

result = 0
for el in range(0,len(n)):
    result = result + int(n[el])
    el += 1
print(result)