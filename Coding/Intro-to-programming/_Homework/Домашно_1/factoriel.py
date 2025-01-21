# Направете програма за пресмятане на n!, различна от варианта, направени в час.
# Коментар: Мисля, че това аз го направих в час и се разбрахме, че съм мога да кача този вариант

##################################################################
# Script for a func which calculates the factoriel of the argument
# fact(num) = n! = n*(n-1)*...*0
# fact(5) = 5! = 5*4*3*2*1 = 120
def fact(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

print(fact(5))