from handler.db_handler import *
from PyQt6 import QtCore, QtGui, QtWidgets

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    userdata = QtCore.pyqtSignal(dict)
    reset_passw_signal = QtCore.pyqtSignal(str)
    update_data_signal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name, passw, self.mysignal, self.userdata)

    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)

    def thr_reset_passw(self, name, passw):
        reset(name, passw, self.reset_passw_signal)

    def thr_update_data(self, username, surname, name, patronymic, email, tn, city, information):
        update(username, surname, name, patronymic, email, tn, city, information, self.update_data_signal)