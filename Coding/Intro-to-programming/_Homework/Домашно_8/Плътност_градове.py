# Извлечете градовете с население по-голямо от дадена стойност (напр. 5 млн). 
# Пресметнете плътността на населението на квадратен километър за всеки от градовете.
# Изведете данните на екрана.

# Зареждаме данните 
# city: population; area [km2]
data = """ Tokyo: 13 515 271; 2191
New York: 8 398 748; 778
Paris: 2 148 271; 105
Chicago: 2 705 994; 589
Hong Kong: 7 298 600; 1104 """

# Обработваме данните в удобен за нас формат
cities = []
for line in data.splitlines(): # разделяме стринга на отделни редове с цикъла
    new_line = (line.split(":")[0], int(line.split(":")[1].split(";")[0].replace(" ", "")), int(line.split(":")[1].split(";")[1]))
    cities.append(new_line) #   ^ Тук създаваме редица с членове: първия елемент от разделения стринг line[0], 
                                                                # интежер от първия поделемент на втория елемент line[1][0] и
                                                                # интежер от втория поделемент на втория елемент line[1][1]. 
                                                                # Премахваме интервали и пунктуация

cities_5_mil = []
density = {}

# С един цикъл ще намерим и двете търсени стойности
for city in cities:

    # Намираме градовете с население над 5 млн.
    if city[1] > 5000000:
        cities_5_mil.append(city[0])
    
    # Намираме плътността на населението
    density[city[0]] = round(city[1] / city[2])

# Дефинирам функция която да превърне списъците и речниците в хубави стрингове
def pretty_str(in_str):
    return str(in_str).replace("'", "").replace("[", "").replace("]","").replace("{", "").replace("}","")

cities_5_mil, density = pretty_str(cities_5_mil), pretty_str(density)

print("\nГрадовете с население по-голямо от 5 млн. са:", cities_5_mil)
print("\nГъстотата на населението в тези градове е:", density)