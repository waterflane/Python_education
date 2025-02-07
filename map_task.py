# 1
# Умножение всех элементов списка на 2
# numbers = [1, 2, 3, 4, 5]

# 2
# Приведение строк к верхнему регистру
# words = ["hello", "world", "python"]

# 3
# Склеивание строк с добавлением текста
# names = ["Alice", "Bob", "Charlie"]
# ['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']

# 4
# Преобразование температур из Цельсия в Фаренгейты
# Формула: F = C * 9/5 + 32
# celsius = [0, 10, 20, 30, 40]

# 5
# Сложение элементов из двух списков
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#  # [5, 7, 9]

# 6
# Округление чисел
# numbers = [1.2, 2.8, 3.5, 4.9] # round(x)
# [1, 3, 4, 5]

# 7
# Вычисление длины строк
# words = ["apple", "banana", "cherry"]
# [5, 6, 6]

# 8
# Объединение нескольких списков в строки
# first_names = ["John", "Jane", "Jack"]
# last_names = ["Doe", "Smith", "Brown"]
# ['John Doe', 'Jane Smith', 'Jack Brown']

#1

numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*2, numbers)))

#2
words = ["hello", "world", "python"]
print(list(map(lambda x: x.upper(), words)))

#3
names = ["Alice", "Bob", "Charlie"]
print(list(map(lambda x: f'Hello, {x}!', names)))

#4
celsius = [0, 10, 20, 30, 40]
print(list(map(lambda x: x * 9/5 + 32, celsius)))

#5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list(map(lambda x,y: x+y, list1, list2)))

#6
numbers = [1.2, 2.8, 3.5, 4.9]
print(list(map(lambda x: round(x), numbers)))

#7
words = ["apple", "banana", "cherry"]
print(list(map(lambda x: len(x), words)))

#8
first_names = ["John", "Jane", "Jack"]
last_names = ["Doe", "Smith", "Brown"]
print(list(map(lambda x,y: f'{x} {y}', first_names, last_names)))
