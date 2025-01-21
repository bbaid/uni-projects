# Да се напише програма, която:
# - Създава речник с ключове символните низове ‘S' и ‘N' и стойности, списъци от реални числа. 
#   Списъкът съответстващ на ключа ‘S' съдържа тези елементи от Lat_degrees, за които съответните елементи от Lat_pole са ‘S' (т.е. [0, 10, ..., 90]). 
#   Списъкът съответстващ на ключа ‘N', съдържа тези елементи от Lat_degrees за които съответните елементи от Lat_pole са ‘N' (т.е. [23.43, 30, ..., 90].
# - Извежда елементите от двата списъка на екрана, всеки списък на отделен ред.

Lat_degrees = (0, 10, 23.43, 30, 23.43, 66.57, 70, 66.57, 90,90)
Lat_pole = ("S", "S", "N", "N", "S", "S", "N", "N", "N", "S")

if len(Lat_degrees) == len(Lat_pole):
    for i in range(len(Lat_degrees)):
        simple_dict[Lat_degrees[i]] = Lat_pole[i]
        
set_dict = {}
set_dict.fromkeys(set(Lat_pole))

S, N = [], []
for i, pole in enumerate(Lat_pole):
    if pole == "S":
        S.append(Lat_degrees[i])
    if pole == "N":
        N.append(Lat_degrees[i])
        
my_dict = {"S": S, "N": N}
print
print(my_dict)