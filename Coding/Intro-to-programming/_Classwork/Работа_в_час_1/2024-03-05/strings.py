# Работа със стрингове (работете във файл, а не в конзола): създайте една стрингова променлива със стойност “В петък ще празнуваме”. 
# Като знаете, че s[0] извлича първия символ от стринга и len(s) връща дължината на стринга, опитайте да направите цикъл,
# който обхожда стринга от ляво на дясно и отпечатва на екрана всеки един символ от него. Тествайте всички методи за стрингове, които знаете.

s = "В петък ще празнуваме"
for chr in s:
    print(chr)

print("\n")

for i in range(len(s)):
    print(s[i])