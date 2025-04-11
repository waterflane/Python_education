class AppError(Exception):
    """ Базовая ошибка"""
    pass
class LoginError(AppError):
    """ Ошибка при входе"""
    pass    
class PermissionDenied(AppError):
    """ Нет доступа """
    pass 


USERS = {
    "admin": {"password": "root", "role": "admin"},
    "vasya": {"password": "123", "role": "user"},
    "petya": {"password": "python", "role": "guest"},
}

def login(username, password):
    if USERS[username]['password'] == password and USERS[username]['role'] == 'admin':
        print('Доступ разрешён', username)
        return 1
    elif username not in USERS or USERS[username]['password'] != password:
        raise PermissionError('Неправильный логин или пароль')
    else:
        raise PermissionError('Нет доступа!')
    return 0


def do_action(key, action):
    if key == 1:
        if action == "Удалить все логи":
            print('Логи удалены!')
    return 1

# try:
#     u = login("vasya", "123")
#     do_action(u, "Удалить все логи")
# except AppError as err:
#     print('Ошибка:', err)
# do_action(u, "Удалить все логи")

u = login("admin", "root")
do_action(u, "Удалить все логи")