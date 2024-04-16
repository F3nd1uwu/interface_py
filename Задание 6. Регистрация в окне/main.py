from PyQt6 import QtWidgets, uic, QtCore, QtGui
import sys
import os
from check_db import *

os.chdir('./Задание 6. Регистрация в окне')

class AuthorizationWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        uic.loadUi('./ui/Authorization.ui', self)
        self.main()

    def main(self):
        self.login.clicked.connect(self.login_func)
        self.signup.clicked.connect(self.register_func)

    def register_func(self):
        name = ''
        passw = ''
        if name and passw:
            name = self.username.text()
            passw = self.password.text()
            self.notification.setText('Повторите пароль...')
            self.password.setText('')
            if passw == self.password.text():
                # сохраняем данные в бд
                self.notification.setText('Вы успешно зарегистрировались! Введите данные для входа...')

    def login_func(self):
        pass


class ProfileWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        uic.loadUi('./ui/profile.ui', self)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    auth = AuthorizationWindow()
    profile = ProfileWindow()
    auth.show()
    sys.exit(app.exec())