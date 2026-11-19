print("Hello world")
print("Hello Git")

def greet():
    return "Hello"

print (greet(), "Wendy")


fruit = "apple"

match fruit:
    case "appele":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")   
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")   



point = (1, 0)

match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")    



pets = ["dog", "fish", "cat"]

match pets:
    case ["dog", "cat", _]:
        # Випадок, коли є і собака, і кіт
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        # Випадок, коли є тільки собака
        print("There's a dog.")
    case _:
        # Випадок для інших комбінацій
        print("No dogs.")



fruit = 'apple'
for char in fruit:
    print(char)        



alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ")    



some_iterable = ["a", "b", "c"]

for i in some_iterable:
    print(i)    


# //Код з цього прикладу виведе в консоль квадрати чисел списку odd_numbers.

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)    





# # Зчитування рядка від користувача
# user_input = input("Введіть рядок: ")

# # Ініціалізація змінних для підрахунку символів та пробілів
# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# # Підрахунок кількості пробілів
# for char in user_input:
#     if char == " ":
#         space_count += 1

# # Виведення результатів
# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")    



k = 0
while k < 10:
    k = k + 1
print(k)


a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)


for i  in range(5):
    print(i)


for i in range(2, 10):
    print(i)    



for i in range(0, 10, 2):
    print(i)    



some_list = ["apple", "banana", "cherry"]
for index, value in enumerate(some_list):
    print(index, value)    



list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key)


for key in numbers.keys():
    print(key)


for val in numbers.values():
    print(val)


for key, value in numbers.items():
    print(key, value)






val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")    




def print_max(a: int, b: int):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів




def modify_string(original: str) -> str:
    original = "змінено"
    return original

str_var = "оригінал"
print(modify_string(str_var))  # виведе: змінено
print(str_var) 



def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()

outer_func()



def greet(name, message="Привіт"):
    print(f"{message}, {name}!")



from datetime import datetime

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2


from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)



import datetime
now = datetime.datetime.now()
print(now)


from datetime import datetime

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")


#FOR 
def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
    codes = {}  
    # Перебір кожного символу в рядку
    for ch in string:  
        # Перевірка, чи символ вже є в словнику
        if ch not in codes:
            # Додавання пари символ-код в словник  
            codes[ch] = ord(ch)  
    return codes



import time

start_time = time.perf_counter()

for _ in range(1_000_000):
    pass 


end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")




cars = {
    "Ford": 2008,
    "BMW": 2020,
    "VW": 2003,
}

for car in cars.items():
    print(car[0])
    print(car[1])

    for model, year in cars.items():
        print(model, year)



 

import datetime
now = datetime.datetime.now()

print(now)        




list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  

clean = '   spacious   '.strip()
print(clean)


text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)



number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())



user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")


import re

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())



import re

text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches) 



import re

file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)  




import re

text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)



def find_max_vowels(text):
    vowels = "aeiouy"
    for char in text:
        if char.lower() not in vowels:
            text = text.replace(char, ".")

    chains = text.split(".")

    chains.sort(key=len)
    max_seq = chains[-1]
    return max_seq, len(max_seq)

text = "A..o.a.e.e.ye.e asdse asaaaaa asdsad"
max_seq, length = find_max_vowels(text)


print(max_seq, length)        



message = "asdfrdsatesdjhcgdycufydotiloxkaayuislka"

sequences = re.findall(r"[aeiouy]+", message)
max_seq = max(sequences, key=len)
print(sequences)
