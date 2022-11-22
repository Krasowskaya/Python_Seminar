# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# not(x or y or z) = not x and not y and not z

for x in range(2):
    for y in range(2):
        for z in range(2):
            n = (not(x or y or z)) == (not (x) and not (y) and not (z))
            print(f'{x}, {y}, {z} - не ({x} или {y} или {z}) = (не {x} и не {y} и не {z}) - {n}')