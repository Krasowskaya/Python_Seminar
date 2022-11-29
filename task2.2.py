# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('--->'))
result = list()
fact = 1

for el in range(1, n + 1):
        fact *= el
        n -= 1
        result.append(fact)
print(result)