import re
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


#Открываем файл
logs = open('logs.txt', 'a')
user_input = input('Добро пожаловать в программу! Для продолжения введите "log" или "reg": ')

#регистрация пользователя
if user_input == 'reg':
        logs = open('logs.txt', 'a')
        logs.write('----------------------------' + '\n')

        # login
        while True:
            try:
                log = input('Введите свой логин (Логин состоит не менее чем из 5 символов из набора латинских букв и цифр): ')
                temp = open('logs.txt', 'r')
                logs_for_read = temp.readlines()
                temp.close()
                temp = 'Логин: ' + log + '\n'

                if len(log) < 5:
                    print('Ваш логин состоит менее чем из 5 символов.')
                    raise ValueError()
                if not (all(char.isalnum() and char.isascii() for char in log)):
                    print('Ваш логин состоит не из латинских букв.')
                    raise ValueError()
                if temp in logs_for_read:
                    print(f'Пользователь с логином "{log}" уже существует.')
                    raise ValueError()
                else:
                    logs.write('Логин: ' + log + '\n')
                    print('Ваш логин записан.', '\n')
                break
            except ValueError:
                print('Попробуйте снова.', '\n')

        # password
        while True:
            try:
                pas = input('Введите пароль (Пароль должен состоять не менее чем из 8 символов, содержать '
                            'как минимум одну строчную и одну прописную букву, хотя бы одну цифру и хотя '
                            'бы один специальный символ): ')
                if len(pas) < 8:
                    print('Ваш пароль состоит менее чем из 8 символов.')
                    raise ValueError()
                if not (re.match(r'(?=.*[a-z])', pas)):
                    print('Ваш пароль не содержит хотя бы одну строчную букву.')
                    raise ValueError()
                if not (re.match(r'(?=.*[A-Z])', pas)):
                    print('Ваш пароль не содержит хотя бы одну прописную букву.')
                    raise ValueError()
                if not (re.match(r'(?=.*[0-9])', pas)):
                    print('Ваш пароль не содержит хотя бы одну цифру.')
                    raise ValueError()
                if not (re.match(r'(?=.*[!@#$%^&*])', pas)):
                    print('Ваш пароль не содержит хотя бы один специальный символ.')
                    raise ValueError()
                else:
                    pas_r = input('Повторите ваш пароль: ')
                    if pas == pas_r:

                        logs.write('Пароль: ' + hash_password(pas) + '\n')
                        print('Ваш пароль записан.', '\n')
                    else:
                        print('Пароль введен неверно.')
                        raise ValueError()
                break
            except ValueError:
                print('Попробуйте снова.', '\n')

        # email
        while True:
            try:
                email = input('Введите ваш email: ')
                if email.count('@') != 1:
                    print('Адрес электронной почты должен содержать ровно 1 символ "@".')
                    raise ValueError()
                if email[0] == '@':
                    print('Адрес электронной почты не может начинаться с "@".')
                    raise ValueError()
                if email[-1] == '@':
                    print('Адрес электронной почты не может заканчиваться на "@".')
                    raise ValueError()
                else:
                    logs.write('Почта: ' + email + '\n')
                    print('Ваша электронная почта записана.', '\n')
                break
            except ValueError:
                print('Попробуйте снова.', '\n')

        # telephone number
        while True:
            try:
                tn = input('Введите ваш номер телефона: ')
                if tn[0] != '8' and tn[0:2] != '+7':
                    print('Номер телефона должен начинаться с "8" или "+7".')
                    raise ValueError()
                if len(tn) != 11 and len(tn) != 12:
                    print('Номер телефона должен содержать 10 цифр после "8" или "+7"')
                    raise ValueError()
                else:
                    logs.write('Номер телефона: ' + tn + '\n')
                    print('Ваш номер телефона записан.', '\n')
                break
            except ValueError:
                print('Попробуйте снова.', '\n')

        user_input = input('Желаете заполнить поля ФИО, город и "о себе"? ("Y" or "N"): ')
        if user_input == 'Y':
            logs.write('Дополнительная информация: \n')
            logs.write('\t ФИО: ' + input('Введите ваше ФИО: ') + '\n')
            logs.write('\t Город: ' + input('Введите ваш город: ') + '\n')
            logs.write('\t О себе: ' + input('Введите информацию "о себе": ') + '\n')

        #Завершение регистрации
        print('Вы зарегистрировались в системе. Ваши данные успешно сохранены.')
        logs.write('----------------------------' + '\n\n\n')
        logs.close()

#Вход по логину
elif user_input == 'log':
    logs = open('logs.txt', 'r').read()
    lines = open('logs.txt', 'r').readlines()
    user_input = input('Введите ваш логин: ')
    if user_input in logs:
        for line in lines:
            if user_input in line:
                k = lines.index(line) + 1
                user_password = lines[k][8:].strip()
                break

        #Проверка пароля
        while True:
            try:
                user_input_password = input('Введите ваш пароль: ')
                if hash_password(user_input_password) != user_password:
                    print('Пароль введен неверно. \n')
                    raise ValueError()
                else:
                    print('Пароль введен верно! Добро пожаловать в ваш профиль!')
                break
            except ValueError:
                print('Попробуйте снова.', '\n')

    else:
        print('Такого пользователя не существует. Зарегистрируйтесь в системе.')

#Неверный ввод login или registration
else:
    print('Неверно введена команда. Попробуйте снова.')
