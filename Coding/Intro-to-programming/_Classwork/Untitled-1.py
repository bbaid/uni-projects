# Внимание, коментарите на самите функции съм писал на английски,
# за да си спестя малко време в сменянето на езици


# 1. Да се създаде потребителска функция, която по зададени цели числа , n, a и b създава и връща списък с n редици,
#    като всяка редица разполага с по два елемента: a ( основа) и ha (височина към а).
L = []
from random import randint
from functools import reduce
def triangle_list(n, a, b):
    """ returns a n - long list of tupples with two elements that are from the range a - b"""
    for n in range(n):
        T = (randint(a, b), randint(a, b)) # generates a tupple of two numbers between a and b
        L.append(T)
    return L

# generates a variable with the output of the triangle list func, given the user's input
t_list = triangle_list(20, 1, 40)

# 2. Напишете lambda функция за пресмятане лицето на триъгълник по зададени основа и височина (лице=0.5 *основа*височина).

triangle_area = lambda a, b: 0.5 * a * b

# 3. Напишете комбинация от map, filter и reduce, такава, че да пресметнете сумата на всички лица, които са по-големи от 10 и по малки от 20.

areas = list(map(triangle_area, (value[0] for value in t_list), (value[1] for value in t_list)))
filtered = list(filter(lambda x: 10 < x < 20, areas))
reduced = reduce(lambda x, y: x+y, filtered)

# 4. Принтирайте подходящо резултатите.
print("Количество генерирани триъгълници:", len(t_list))
print("Произволна извадка на основа и височина от триъгълниците:", "a =", t_list[randint(1, len(t_list))][0], "Ha =", t_list[randint(1, len(t_list))][1])
print("Списък на всички лица:", areas)
print("Списък на лицата между 10 и 20", filtered)
print("Сумата на филтрираните лица", reduced)