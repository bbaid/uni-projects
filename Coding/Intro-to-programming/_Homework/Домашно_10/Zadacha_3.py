# Направете try/raise/except конструкция за въвеждане на цяло число от клавиатурата, като ако не сме въвели цяло число да има подходящо съобщение в клаузата except. 
# Кръстете raise грешката “notInteger”. Обърнете внимание, че първо трябва да създадем обект от даден клас.

class notInteger(Exception): # Създаваме клас за грешката
    pass

while True:
    try:
        number = input("Въведете цяло число: ")
        if not number.isdigit():
            raise notInteger("Въведете коректно цяло число!")
        number = int(number)
        break
    except notInteger as e:
        print(e)