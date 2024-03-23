import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PythonApp')
        self.setFixedSize(600, 600)

        self.click_counter = 0
        self.label = QLabel('0 clicks', self)
        self.button = QPushButton('Click me!', self)
        self.button.resize(100, 25)
        self.button.move(250, 287)
        self.label.resize(100, 25)
        self.label.move(255, 262)
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.close)
        self.exit_button.resize(100, 30)
        self.exit_button.move(500, 570)
        self.button.clicked.connect(self.counter_func)
        self.moveable_button = QPushButton('I am moving!', self)
        self.moveable_button.resize(100, 25)
        self.moveable_button.clicked.connect(self.move_func)
        self.yes = QPushButton('Yes!', self)
        self.no = QPushButton('No!', self)
        self.labelyn = QLabel('Push "Yes" or "No"', self)
        self.yes.move(0, 570)
        self.no.move(100, 570)
        self.labelyn.move(50, 540)
        self.yes.clicked.connect(self.yes_func)
        self.no.clicked.connect(self.no_func)
        self.new_window = QPushButton('Create new QDialog!', self)
        self.new_window.resize(200, 30)
        self.new_window.move(200, 570)
        self.new_window.clicked.connect(self.new_window_func)

    def counter_func(self):
        self.click_counter += 1
        self.label.setText(f'{self.click_counter} clicks')

    def move_func(self):
        self.moveable_button.move(self.moveable_button.x() + 5, self.moveable_button.y())
        if self.moveable_button.x() == 500:
            self.moveable_button.move(0, 0)

    def yes_func(self):
        self.labelyn.move(90, 540)
        self.labelyn.setText('YES!')

    def no_func(self):
        self.labelyn.move(92, 540)
        self.labelyn.setText('NO!')

    def new_window_func(self):
        self.second_window = SecondWindow(self)
        self.second_window.show()
        self.hide()


class SecondWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.SecondUi()

    def SecondUi(self):
        self.setWindowTitle('New window')
        self.setFixedSize(600, 600)
        self.dialog_message = QLabel('You create new window!', self)
        self.dialog_message.move(250, 280)
        self.back_button = QPushButton('Back', self)
        self.back_button.clicked.connect(self.back_func)

    def back_func(self):
        self.window = MainWindow()
        self.window.show()
        self.hide()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
