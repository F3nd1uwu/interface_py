import sys
from PyQt6.QtCore import pyqtSlot
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIcon


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('files/MainWindow.ui', self)
        self.pushButton_7.setIcon(QIcon('files/menu_FILL0_wght400_GRAD0_opsz24.png'))
        self.pushButton_4.setIcon(QIcon('files/view_kanban_FILL0_wght400_GRAD0_opsz24.png'))
        self.pushButton_6.setIcon(QIcon('files/check_box_outline_blank_FILL0_wght400_GRAD0_opsz24.png'))
        self.pushButton_5.setIcon(QIcon('files/cached_FILL0_wght400_GRAD0_opsz24.png'))
        self.pushButton_3.setIcon(QIcon('files/logout_FILL0_wght400_GRAD0_opsz24.png'))

        logs = open('logs.txt', 'r')
        f = logs.readlines()
        logs.close()
        if f != []:
            self.yes_count = int(f[0])
            self.no_count = int(f[1])
            self.editLabel = f[2]
            self.editButton1 = f[3]
            self.editButton2 = f[4]
        else:
            logs = open('logs.txt', 'w')
            logs.write('0' + '\n' + '0' + '\n' + '0' + '\n' + '0' + '\n' + '0')
            logs.close()
            self.yes_count = 0
            self.no_count = 0
            self.editLabel = '0'
            self.editButton1 = '0'
            self.editButton2 = '0'

        self.setWindowTitle('MiniProject2')

        self.main()

    def main(self):
        self.pushButton_3.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.yes_func)
        self.pushButton_2.clicked.connect(self.no_func)
        self.pushButton_5.clicked.connect(self.reset_func)
        self.pushButton_4.clicked.connect(self.update_label)
        self.pushButton_6.clicked.connect(self.update_buttons)

        self.label.setText(f'{self.editLabel}')
        self.label_2.setText(f'{self.editButton1} - {self.yes_count}.')
        self.label_3.setText(f'{self.editButton1} - {self.no_count}.')
        self.pushButton.setText(f'{self.editButton1}')
        self.pushButton_2.setText(f'{self.editButton2}')

    def yes_func(self):
        self.yes_count += 1
        logs = open('logs.txt', 'w')
        logs.write(str(self.yes_count) + '\n' + str(self.no_count) + '\n' + self.editLabel + '\n' + self.editButton1 + '\n' + self.editButton2)
        logs.close()
        self.label_2.setText(f'{self.editButton1} - {self.yes_count}.')

    def no_func(self):
        self.no_count += 1
        logs = open('logs.txt', 'w')
        logs.write(str(self.yes_count) + '\n' + str(self.no_count) + '\n' + self.editLabel + '\n' + self.editButton1 + '\n' + self.editButton2)
        logs.close()
        self.label_3.setText(f'{self.editButton2} - {self.no_count}.')

    def reset_func(self):
        self.yes_count = 0
        self.no_count = 0
        logs = open('logs.txt', 'w')
        logs.write(str(self.yes_count) + '\n' + str(self.no_count) + '\n' + self.editLabel + '\n' + self.editButton1 + '\n' + self.editButton2)
        logs.close()
        self.label_2.setText(f'{self.editButton1} - {self.yes_count}.')
        self.label_3.setText(f'{self.editButton2} - {self.no_count}.')

    def update_label(self):
        self.window_for_label = LabelWindow(self)
        self.window_for_label.show()
        self.hide()

    def update_buttons(self):
        self.window_for_buttons = ButtonsWindow(self)
        self.window_for_buttons.show()
        self.hide()

class LabelWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        uic.loadUi('files/Question.ui', self)

        self.main_label()

    def main_label(self):
        self.setWindowTitle('LabelEdit')
        self.setFixedSize(400, 200)

        self.buttonBox.accepted.connect(self.ok_func)
        self.buttonBox.rejected.connect(self.back_func)


    def back_func(self):
        self.parent.show()

    def ok_func(self):
        self.parent.editLabel = self.lineEdit.text().strip()
        logs = open('logs.txt', 'w')
        logs.write(str(self.parent.yes_count) + '\n' + str(self.parent.no_count) + '\n' + self.parent.editLabel + '\n' + self.parent.editButton1 + '\n' + self.parent.editButton2)
        logs.close()
        self.parent.label.setText(f'{self.parent.editLabel}')
        self.parent.show()


class ButtonsWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        uic.loadUi('files/Buttons.ui', self)

        self.main_button()

    def main_button(self):
        self.setWindowTitle('ButtonsEdit')
        self.setFixedSize(400, 200)

        self.buttonBox.accepted.connect(self.ok_func)
        self.buttonBox.rejected.connect(self.back_func)


    def back_func(self):
        self.parent.show()

    def ok_func(self):
        self.parent.editButton1 = self.lineEdit.text().strip()
        self.parent.editButton2 = self.lineEdit_2.text().strip()
        logs = open('logs.txt', 'w')
        logs.write(str(self.parent.yes_count) + '\n' + str(self.parent.no_count) + '\n' + self.parent.editLabel + '\n' + self.parent.editButton1 + '\n' + self.parent.editButton2)
        logs.close()
        self.parent.pushButton.setText(f'{self.parent.editButton1}')
        self.parent.pushButton_2.setText(f'{self.parent.editButton2}')
        self.parent.label_2.setText(f'{self.parent.editButton1} - {self.parent.yes_count}.')
        self.parent.label_3.setText(f'{self.parent.editButton2} - {self.parent.no_count}.')
        self.parent.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
