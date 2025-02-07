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
def filt(zov):
    if zov%2 ==0:
        return True
    return False

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spisok = list(filter(filt, spisok))
print(spisok)

#2
def filt(zov):
    if zov>=0:
        return True
    return False

spisok = [-3, -2, -1, 0, 1, 2, 3]
spisok = list(filter(filt, spisok))
print(spisok)

#3
def filt(zov):
    if len(zov)<5:
        return True
    return False

spisok = ["apple", "banana", "cherry", "fig", "grape"]
spisok = list(filter(filt, spisok))
print(spisok)

#4
def filt(zov):
    if zov==None:
        return False
    return True

spisok = [0, None, "", "Hello", 42, None, "Python"]
spisok = list(filter(filt, spisok))
print(spisok)

#5
def filt(zov):
    if zov['score']>75:
        return True
    return False

spisok = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 90},
    {"name": "David", "score": 60}
]
spisok = list(filter(filt, spisok))
print(spisok)

#6
def filt(zov):
    if zov[0]=='p':
        return True
    return False

spisok = ["python", "java", "php", "javascript", "perl", "ruby"]
spisok = list(filter(filt, spisok))
print(spisok)

#7
def filt(zov):
    if '@'in zov:
        return True
    return False

spisok = ["user@example.com", "hello world", "test@python.org", "no_email_here", "admin@mail.com"]
spisok = list(filter(filt, spisok))
print(spisok)