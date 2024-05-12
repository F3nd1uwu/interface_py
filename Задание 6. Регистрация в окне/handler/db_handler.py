import sqlite3 as sq
import hashlib

def hash_password(password):
    # Создание объекта хеша
    hasher = hashlib.sha256()
    # Кодирование пароля в бинарный вид
    password_encoded = password.encode('utf-8')
    # Вычисление хеша пароля
    hasher.update(password_encoded)
    # Получение хеша в виде строки
    password_hashed = hasher.hexdigest()
    return password_hashed


def login(login, passw, signal, userdata):
    with sq.connect('handler/users.db') as con:
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE username="{login}";')
        value = cur.fetchall()

        if value != [] and value[0][2] == hash_password(passw):
            user_data = {
            'surname': value[0][3],
            'name': value[0][4],
            'patronymic': value[0][5],
            'email': value[0][6],
            'telephone_number': value[0][7],
            'city': value[0][8],
            'information': value[0][9]
            }
            signal.emit('Успешная авторизация!')
            userdata.emit(user_data)
        else:
            signal.emit('Проверьте правильность ввода данных!')

        cur.close()

def register(login, passw, signal):
    with sq.connect('handler/users.db') as con:
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE username="{login}";')
        value = cur.fetchall()

        if value != []:
            signal.emit('Данный логин уже занят!')
        elif value == []:
            cur.execute(f"INSERT INTO users (username, password) VALUES ('{login}', '{hash_password(passw)}')")
            signal.emit('Вы успешно зарегистрировались!')

        cur.close()
    
def reset(login, passw, signal):
    with sq.connect('handler/users.db') as con:
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE username="{login}"')
        value = cur.fetchall()

        if value != []:
            cur.execute(f'UPDATE users SET password="{hash_password(passw)}" WHERE username="{login}"')
            signal.emit('Ваш пароль успешно изменен!')
        else:
            signal.emit('Проверьте правильность ввода данных!')
        
        cur.close()

def update(login, surname, name, patronymic, email, tn, city, information, signal):
    with sq.connect('handler/users.db') as con:
        cur = con.cursor()

        cur.execute(f'SELECT * FROM users WHERE username="{login}"')
        value = cur.fetchall()

        if value != []:
            cur.execute(f'UPDATE users SET surname="{surname}" WHERE username="{login}"')
            cur.execute(f'UPDATE users SET name="{name}" WHERE username="{login}"')
            cur.execute(f'UPDATE users SET patronymic="{patronymic}" WHERE username="{login}"')
            cur.execute(f'UPDATE users SET email="{email}" WHERE username="{login}"')
            cur.execute(f'UPDATE users SET telephone_number="{tn}" WHERE username="{login}"')
            cur.execute(f'UPDATE users SET city="{city}" WHERE username="{login}"')
            cur.execute(f'UPDATE users SET information="{information}" WHERE username="{login}"')
            signal.emit('Ваши данные успешно сохранены!')
        else:
            signal.emit('Проверьте правильность ввода данных!')
        
        cur.close()
