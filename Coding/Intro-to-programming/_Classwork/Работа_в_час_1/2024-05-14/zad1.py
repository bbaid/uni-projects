# Зад. 1 Даден е списък от редици, в който всяка редица съдържа името на държава и броя на определен вид животни в тази държава, 
# изчислете общия брой животни във всички държави и след това изчислете средния брой животни за всяка страна.

# Зареждаме списъка
countries_animal = [("USA", 5000),
                    ("India", 8000),
                    ("Brazil", 6000),
                    ("China", 7000),
                    ("Russia", 5500)]

S = 0
for i in range(len(countries_animal)):
    S = S + countries_animal[i][1]
    print(S)