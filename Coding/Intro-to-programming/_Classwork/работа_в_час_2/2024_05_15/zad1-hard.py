#zad1-hard

# Зад. 1 Даден е списък от редици, в който всяка редица съдържа името на държава и броя на определен вид животни в тази държава, 
# изчислете общия брой животни във всички държави и след това изчислете средния брой животни за всяка страна.

from functools import reduce
# Зареждаме списъка
countries_animal = [("USA", 5000),
                    ("India", 8000),
                    ("Brazil", 6000),
                    ("China", 7000),
                    ("Russia", 5500)]

animal_count = map(lambda x: x[1], countries_animal)
animal_sum = reduce(lambda x, y: x+y, animal_count)
animal_avr = animal_sum / len(countries_animal)
print(animal_sum, animal_avr)