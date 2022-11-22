# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
 

arr = [(x1, y1),(x2, y2)]

lst = [(((arr[i][0] - arr[i+1][0])**2 + (arr[i][1] - arr[i+1][1])**2)**0.5) for i in range(len(arr) - 1)]
print(lst)

# def distance(x1, y1, x2, y2):
#     c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# c = distance(x1, y1, x2, y2)
# print(c)