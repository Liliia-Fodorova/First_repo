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