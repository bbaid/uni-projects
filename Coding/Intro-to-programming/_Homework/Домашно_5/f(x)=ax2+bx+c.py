# Да се направи списък от 8 произволни цели числа x в интервала [0,100]. 
# За всяко число да се изчисли формулата f(x)=a*x^2+b*x+c, където a, b и c са произволно генерирани константи. 
# Резултатите да се оформят в редица FX с наредени редици от вида: (x, f(x)).
#################################################################################################################
from random import randint
x_list = []
fx_list = []
final_list = []
for i in range(8):
    x_list.append(randint(0, 100))

# Генерираме константите, като използваме съкратен запис за няколко променливи заедно, както и за for цикъла (3те завъртания са за трите променливи)
a, b, c = [randint(1, 10) for _ in range(3)]

# Изчисляване на формулата, като в този случай i е стойността на списъка
for x in x_list:
    fx_list.append(a*x**2+b*x+c)

# Съединяваме съдържанието на двата цикъла
for i in range(len(x_list)):
    final_list.append((x_list[i], fx_list[i])) # ВАЖНО! Тук скобите са двойни, защото веднъж е функцията append() и вътре в аргумента създаваме редицата с вторите скоби

print(f"Изведена е редица от стойностите на x и f(x),\nпри формулата {a}*x^2 + {b}*x + {c}:\n", result_tuple := tuple(final_list))