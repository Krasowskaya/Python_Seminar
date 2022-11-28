# 5. Реализуйте алгоритм перемешивания списка.

import random

s = [11,2,3,4,5,6,7,89]
# random.shuffle(s)
# print(s) - через библиотеки
temp = s[0]

for i in range(0,len(s)-2):
    temp = s[i]
    s[i] = s[i+2]
    s[i+2] = s[i-1]
    s[i-1] = temp
print(s)