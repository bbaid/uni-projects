# Да се направи подробен коментар към скриптовете на приложените задачи.

##################################################################################
# Задача: Ако е дадена фраза на български (може да бъдат две или повече думи
# написани слято), напишете програма, която изписва с латински букви същата
# дума. При конвертирането:
# а) да се заменят с цифри от 0 до 9 буквите [о,и,д,е,ч,п,ш,т,ъ,щ] и символите @
#    и ! за буквите “а”,”л”;
# б) всяка 3-та буква, ако не е символ или цифра, да се направи главна.
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# A-Z [65;90]
# a-z [97;122]
# 0-9 [48;57]
# А-Я [1040;1065]
# а-я [1072;1097]
# ord('б')-ord('b')=975
# ord('Б')-ord('B')=975

# Дефиниране на буквите от A до Z в ASCII таблицата
AZ = ''.join([chr(i) for i in range(ord('A'), ord('Z')+1)])

# Дефиниране на буквите от a до z в ASCII таблицата
az = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])

# Дефиниране на цифрите от 0 до 9 в ASCII таблицата
num = [chr(i) for i in range(ord('0'), ord('9')+1)]

# Добавяне на специалните символи @ и ! към списъка с цифрите
num.extend(['@', '!'])

# Обединяване на всички символи в един стринг
num = ''.join(num)

# Дефиниране на символите, които трябва да се заменят с цифри
numcod = ''.join(['о', 'и', 'д', 'е', 'ч', 'п', 'ш', 'т', 'ъ', 'щ', 'а', 'л'])

# Дефиниране на българските букви от А до Я
BG = ''.join([chr(i) for i in range(ord('А'), ord('Я')+1)])
BG = BG[:26]

# Дефиниране на българските букви от а до я
bg = ''.join([chr(i) for i in range(ord('а'), ord('я')+1)])
bg = bg[:26]

# Потребителят въвежда фраза на български, която съдържа и символи и цифри
str_input = input('Моля, въведете фраза на български: ')

# Инициализация на променлива за новата фраза
new_phrase = ''

# Заместване на буквите, които трябва да бъдат заменени с цифри, и символите @ и !
for char in str_input:
    k_BG = BG.find(char)
    k_bg = bg.find(char)
    k_numcod = numcod.find(char)
    
    # Заместване на буквите, които трябва да бъдат заменени с цифри
    if k_numcod != -1:
        str_input = str_input.replace(char, num[k_numcod])
    
    # Заместване на малките български букви със съответните им малки латински букви
    elif k_bg != -1:
        str_input = str_input.replace(char, az[k_bg])
    
    # Заместване на големите български букви със съответните им големи латински букви
    elif k_BG != -1:
        str_input = str_input.replace(char, AZ[k_BG])
    else:
        str_input = str_input.replace(char, "#")

# Промяна на всяка 3-та буква, ако не е символ или цифра, да бъде направена главна
for i in range(0, len(str_input)):
    cond_1 = (i+1) % 3 == 0
    cond_2 = str_input[i] in az
    if cond_1 & cond_2:
        str_input = str_input[:i] + str_input[i].upper() + str_input[i+1:]

# Извеждане на новата фраза
print("Новата фраза е: " + str_input)