# УСЛОВИЕ:
# Напишете програма, която по два зададени контейнера, намира сечението от елементи, общи и за двата контейнера. 
# Направете програмата да показва на екрана въведените контейнери и елементите на тяхното сечение.


# Ако разбирам правилно "зададени контейнери", това значи предварително готови контейнери
# За да не разхищаваме памет ще използвам редици

cont1 = ('code', 'bomber', 'bride', 'restless', 'mixture', 'preparation', 'advertising', 'sell', 'retain', 'chaos', 'guarantee', 'height', 'element', 'denial', 'mug')
cont2 = ('Karen', 'believed', 'all', 'traffic', 'laws', 'should', 'be', 'obeyed', 'by', 'all', 'except', 'herself', 'code', 'bomber', 'bride', 'restless', 'mixture', 'preparation')

# Превръщаме контейнерите в множества, за да проверим сеченията
set1, set2 = set(cont1), set(cont2)

# Намираме сечението 
new_set = set1 & set2

# Показваме контейнерите на потребителя
print(f"Входящи контейнери:\n{cont1}\n{cont2}\n Сечение на техните елементи:\n{new_set}")