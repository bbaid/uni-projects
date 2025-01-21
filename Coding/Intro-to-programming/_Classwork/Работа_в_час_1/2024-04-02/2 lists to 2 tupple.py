# Създайте наредени двойки редици въз основа на два списъка, които се въвеждат от потребителя. 
# Нека списъците бъдат въведени като низове, които след това се превръщат в списъци чрез метода split. 
# За създаването на двойките редици използвайте:
#   - Кратката форма на for-цикъл
#   - Ф-ята zip()

print("Enter two lists with whatever items you want. Use \", \" as a denominator.")
list_1 = input("Enter the first list: ")
list_2 = input("Enter the second list: ")


print("Variant 1")

result_1 = list_1.split(", ")
result_2 = list_2.split(", ")

zipped = zip(result_1, result_2)

print(list(zipped))

print("Variant 2")

ordered = [(result_1[n], result_2[n]) for n in range(len(result_1))]
print(ordered)