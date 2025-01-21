#ф-я, която пресмята n!
input("Въведи число за факториране")
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)