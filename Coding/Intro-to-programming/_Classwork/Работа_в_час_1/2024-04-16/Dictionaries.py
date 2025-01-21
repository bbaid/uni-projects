# Създайте речник въз основа на два списъка, които се въвеждат от потребителя. 
# Нека списъците бъдат въведени като низове, които след това се превръщат в списъци чрез метода split. 
# За създаването на речника използвайте:
#       [x]   - Кратката форма на for-цикъл
#       []   - Присвояване на стойност за всеки ключ от речника
#       [x]   - Ф-ята за създаване на речник dict() в комбинация със zip()
#       [x]   - Метода update()
my_dict = {}

print("Enter two lists with whatever items you want. Use a space as a delimiter")
# list_1 = input("Enter the first list: ")
# list_2 = input("Enter the second list: ")

# For debugging
list_1 = ("tree bush shrub")
list_2 = ("1 2 3")

result_1 = list_1.split(" ")
result_2 = list_2.split(" ")

# my_dict = {result_1[n]: result_2[n] for n in range(len(result_1))}

# my_dict = dict(zip(result_1, result_2))

my_dict = dict.fromkeys(result_1)
for i in range(len(result_1)):
    my_dict[result_1[i]] = result_2[i]

my_dict = {}
for i in range(len(result_1)):
    my_dict.update({result_1[i]:result_2[i]})

print(my_dict)

