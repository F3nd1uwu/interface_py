from PyQt6 import QtWidgets, uic, QtCore, QtGui
import sys
import os
from check_db import *
import re
from PIL import Image

os.chdir('./Задание 6. Регистрация в окне')

class AuthorizationWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        uic.loadUi('./ui/Authorization.ui', self)
        self.password2.hide()
        self.main()

    def main(self):
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)
        self.check_db.userdata.connect(self.get_userdata)
        self.base_line_edit = [self.username, self.password]
        self.login.clicked.connect(self.auth)
        self.signup.clicked.connect(self.reg)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    self.notification.setText('Поля с даннми не должны быть пустыми!')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if len(self.username.text()) < 5:
                    self.notification.setText('Ваш логин состоит менее чем из 5 символов.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if not (all(char.isalnum() and char.isascii() for char in self.username.text())):
                    self.notification.setText('Ваш логин состоит не из латинских букв.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if len(self.password.text()) < 8:
                    self.notification.setText('Ваш пароль состоит менее чем из 8 символов.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if not (re.match(r'(?=.*[a-z])', self.password.text())):
                    self.notification.setText('Ваш пароль не содержит хотя бы одну строчную букву.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if not (re.match(r'(?=.*[A-Z])', self.password.text())):
                    self.notification.setText('Ваш пароль не содержит хотя бы одну прописную букву.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if not (re.match(r'(?=.*[0-9])', self.password.text())):
                    self.notification.setText('Ваш пароль не содержит хотя бы одну цифру.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
                if not (re.match(r'(?=.*[!@#$%^&*])', self.password.text())):
                    self.notification.setText('Ваш пароль не содержит хотя бы один специальный символ.')
                    self.password.setText('')
                    self.password2.setText('')
                    return
            funct(self)
        return wrapper

    @check_input
    def reg(self):
        if self.password2.isHidden():
            self.notification.setText('Повторите ваш пароль еще раз, пожалуйста.')
            self.password2.show()
        elif self.password.text() == self.password2.text():
            name = self.username.text()
            passw = self.password.text()
            self.check_db.thr_register(name, passw)
            self.password2.hide()
            self.notification.setText('Теперь вы можете авторизоваться!')

    def auth(self):
        name = self.username.text()
        passw = self.password.text()
        self.check_db.thr_login(name, passw)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        if value == 'Успешная авторизация!':
            auth.hide()
            profile.show()
        self.password.setText('')
        self.password2.setText('')

    def get_userdata(self, value):
        profile.user_data = value
        profile.username = self.username.text()


class ProfileWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi('./ui/profile.ui', self)
        self.notification_data.hide()
        self.notification_passw.hide()
        self.openFile = '1.jpg'
        self.pixmap = QtGui.QPixmap(self.openFile)
        self.pixmap = self.pixmap.scaled(700, 600)
        self.ava.setPixmap(self.pixmap)
        self.main()

    def main(self):
        self.check_db = CheckThread()
        self.check_db.reset_passw_signal.connect(self.signal_handler_profile)
        self.check_db.update_data_signal.connect(self.signal_handler_update_data)
        self.update.clicked.connect(self.update_profile)
        self.logout.clicked.connect(self.logout_func)
        self.reset_passw_btn.clicked.connect(self.reset_passw_func)
        self.update_data_btn.clicked.connect(self.update_data_func)

    def check_input(funct):
        def wrapper(self):
            if len(self.reset_passw.text()) < 8:
                self.notification_passw.show()
                self.notification_passw.setText('Ваш пароль состоит менее чем из 8 символов.')
                self.reset_passw.setText('')
                self.reset_passw2.setText('')
                return
            if not (re.match(r'(?=.*[a-z])', self.reset_passw.text())):
                self.notification_passw.show()
                self.notification_passw.setText('Ваш пароль не содержит хотя бы одну строчную букву.')
                self.reset_passw.setText('')
                self.reset_passw2.setText('')
                return
            if not (re.match(r'(?=.*[A-Z])', self.reset_passw.text())):
                self.notification_passw.show()
                self.notification_passw.setText('Ваш пароль не содержит хотя бы одну прописную букву.')
                self.reset_passw.setText('')
                self.reset_passw2.setText('')
                return
            if not (re.match(r'(?=.*[0-9])', self.reset_passw.text())):
                self.notification_passw.show()
                self.notification_passw.setText('Ваш пароль не содержит хотя бы одну цифру.')
                self.reset_passw.setText('')
                self.reset_passw2.setText('')
                return
            if not (re.match(r'(?=.*[!@#$%^&*])', self.reset_passw.text())):
                self.notification_passw.show()
                self.notification_passw.setText('Ваш пароль не содержит хотя бы один специальный символ.')
                self.reset_passw.setText('')
                self.reset_passw2.setText('')
                return
            funct(self)
        return wrapper

    def update_profile(self):
        self.greetings.setText(f'Здравствуйте, {self.username}!')
        self.surname_line.setText(self.user_data['surname'])
        self.name_line.setText(self.user_data['name'])
        self.patronymic_line.setText(self.user_data['patronymic'])
        self.email_line.setText(self.user_data['email'])
        self.telephone_number_line.setText(self.user_data['telephone_number'])
        self.city_line.setText(self.user_data['city'])
        self.information_line.setText(self.user_data['information'])

    def logout_func(self):
        self.userdata = {}
        self.greetings.setText(f'Здравствуйте, username!')
        self.surname_line.setText('')
        self.name_line.setText('')
        self.patronymic_line.setText('')
        self.email_line.setText('')
        self.telephone_number_line.setText('')
        self.city_line.setText('')
        self.information_line.setText('')
        self.username = ''
        profile.hide()
        auth.show()

    def signal_handler_profile(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        if value == 'Ваш пароль успешно изменен!':
            self.notification_passw.hide()
        self.reset_passw.setText('')
        self.reset_passw2.setText('')

    @check_input
    def reset_passw_func(self):
        if self.reset_passw.text() == self.reset_passw2.text():
            passw = self.reset_passw.text()
            self.check_db.thr_reset_passw(self.username, passw)
            self.notification_passw.setText('')
        elif self.reset_passw.text() != self.reset_passw2.text():
            self.notification_passw.setText('Ваш пароль отличается от повторного!')
            self.reset_passw.setText('')
            self.reset_passw2.setText('')

    def signal_handler_update_data(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        if value == 'Ваши данные успешно сохранены!':
            self.notification_data.hide()

    def update_data_func(self):
        data_flag = True
        surname = self.surname_line.text()
        name = self.name_line.text()
        patronymic = self.patronymic_line.text()

        email = self.email_line.text()
        if email.count('@') != 1:
            self.notification_data.show()
            self.notification_data.setText('Адрес электронной почты должен содержать ровно 1 символ "@".')
            data_flag = False
        if email[0] == '@':
            self.notification_data.show()
            self.notification_data.setText('Адрес электронной почты не может начинаться с "@".')
            data_flag = False
        if email[-1] == '@':
            self.notification_data.show()
            self.notification_data.setText('Адрес электронной почты не может заканчиваться на "@".')
            data_flag = False

        tn = self.telephone_number_line.text()
        if tn[0] != '8' and tn[0:2] != '+7':
            self.notification_data.show()
            self.notification_data.setText('Номер телефона должен начинаться с "8" или "+7".')
            data_flag = False
        if len(tn) != 11 and len(tn) != 12:
            self.notification_data.show()
            self.notification_data.setText('Номер телефона должен содержать 10 цифр после "8" или "+7"')
            data_flag = False

        city = self.city_line.text()
        information = self.information_line.toPlainText()

        if data_flag:
            self.check_db.thr_update_data(self.username, surname, name, patronymic, email, tn, city, information)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    auth = AuthorizationWindow()
    profile = ProfileWindow()
    auth.show()
    sys.exit(app.exec())
