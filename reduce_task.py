from functools import reduce

# 2 Вычитание чисел
# Вычислить разность всех чисел в списке.
# numbers = [3, 7, 2, 9, 5]

# 2 Максимальное число
# Найди наибольшее число в списке.
# numbers = [3, 7, 2, 9, 5]

# 3 Поиск самого короткого слова
# Найди самое короткое слово в списке.
# words = ["apple", "banana", "kiwi", "pear"]

# 4 Сумма квадратов чисел
# Вычисли сумму квадратов чисел.
# numbers = [1, 2, 3, 4]

# 5 Перемножение только нечётных чисел
# Найди произведение только нечётных чисел
# в списке.
# numbers = [1, 2, 3, 4, 5]



1
def f(a,b):
    return a - b

l = [23,21,45,98]
print(reduce(f,l))

2
def f(a,b):
    return max(a,b)

l = [3,7,2,9,5]
print(reduce(f,l))

3
def f(a,b):
    if len(a) > len(b):
        return b
    else: return a

words = ["apple", "banana", "kiwi", "pear"]
print(reduce(f, words))

4
def f(a,b):
    return a + b**2

numbers = [1, 2, 3, 4]
print(reduce(f, numbers))

5
def f(a,b):
    if b % 2 == 1:
        return a * b
    else: return a

numbers = [1, 2, 3, 4, 5]
print(reduce(f, numbers))