# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('--->'))
result = list()
fact = 1



for el in range(1, n):
    
    while n > 1:
        el += 1
        fact *= n
        n -= 1
        print(result)
    else:
        print('1')


# while n > 1:
#     factorial *= n
#     print(factorial, end=" ")
#     n -= 1

# for el in range(1,n - 1):
#     m *= el
#     result.append(m)
# print(result)