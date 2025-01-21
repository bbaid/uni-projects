# Имаме списък от списъци със числа. Да се намери сумата на всички числа

L = [[12,3,4],[5,3,44],[12,12,2]]
S = 0
for i in range(len(L)):
    for j in range(len(L[i])):
        print(S)
        S = S + L[i][j]
print(S)

# Ще превърнем списъка от списъци в редица от редици
T = tuple(L)
for i in range(len(L)):
    if i == 0:
        T = tuple(T[i]) + T[i+1:]
    else:
        T = T[:i]+ tuple(T[i]+T[i+1:])
print(T)