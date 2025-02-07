# 1
# Фильтруем только четные числа из списка.
# 2
# Фильтруем только положительные числа
# 3
# Фильтруем только длинные строки (например, больше 5 символов).
# 4
# Удаляем None из списка.
# 5
# Выбираем студентов с оценкой выше 75.
# 6
# Дан список слов. Оставьте только те, которые начинаются на букву "p".
# 7
# Дан список строк, среди которых могут быть e-mail адреса. Оставьте только строки, содержащие @.


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 60}
]

#1

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spisok = list(filter(lambda x: x%2==0, spisok))
print(spisok)

#2

spisok = [-3, -2, -1, 0, 1, 2, 3]
spisok = list(filter(lambda x: x>=0, spisok))
print(spisok)

#3

spisok = ["apple", "banana", "cherry", "fig", "grape"]
spisok = list(filter(lambda x: len(x)>5, spisok))
print(spisok)

#4

spisok = [0, None, "", "Hello", 42, None, "Python"]
spisok = list(filter(lambda x: x!=None, spisok))
print(spisok)

#5

spisok = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 60}
]
spisok = list(filter(lambda x: x['score']>75, spisok))
print(spisok)

#6

spisok = ["python", "java", "php", "javascript", "perl", "ruby"]
spisok = list(filter(lambda x: x[0]=='p', spisok))
print(spisok)

#7

spisok = ["user@example.com", "hello world", "test@python.org", "no_email_here", "admin@mail.com"]
spisok = list(filter(lambda x: '@' in x, spisok))
print(spisok)