from PyQt6.QtWidgets import QLabel, QPushButton, QMainWindow, QApplication, QWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self, app, parent=None):
        super().__init__(parent)

        self.setWindowTitle('MiniProject')
        self.setFixedSize(600, 600)

        logs = open('logs.txt', 'r')
        f = logs.readlines()
        self.yes_count = int(f[0])
        self.no_count = int(f[1])
        logs.close()

        self.main_func()

    def main_func(self):
        self.yes = QPushButton('За!', self)
        self.yes.move(200, 300)
        self.no = QPushButton('Против!', self)
        self.no.move(300,300)
        self.label = QLabel(f'Всего {self.yes_count} голосов "За" и {self.no_count} голосов "Против".', self)
        self.label.setFixedSize(400, 30)
        self.label.move(185, 270)
        self.close_button = QPushButton('Close App', self)
        self.close_button.clicked.connect(self.close)
        self.close_button.move(500, 570)
        self.reset = QPushButton('Сбросить!', self)
        self.reset.move(250, 370)
        self.reset.clicked.connect(self.reset_func)

        self.yes.clicked.connect(self.yes_func)
        self.no.clicked.connect(self.no_func)


    def yes_func(self):
        self.yes_count += 1
        logs = open('logs.txt', 'w')
        logs.write(str(self.yes_count) + '\n' + str(self.no_count))
        logs.close()
        self.label.setText(f'Всего {self.yes_count} голосов "За" и {self.no_count} голосов "Против".')

    def no_func(self):
        self.no_count += 1
        logs = open('logs.txt', 'w')
        logs.write(str(self.yes_count) + '\n' + str(self.no_count))
        logs.close()
        self.label.setText(f'Всего {self.yes_count} голосов "За" и {self.no_count} голосов "Против".')

    def reset_func(self):
        self.yes_count = 0
        self.no_count = 0
        logs = open('logs.txt', 'w')
        logs.write(str(self.yes_count) + '\n' + str(self.no_count))
        logs.close()
        self.label.setText(f'Всего {self.yes_count} голосов "За" и {self.no_count} голосов "Против".')


def application():
    app = QApplication(sys.argv)

    window = MainWindow(app=app)
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    application()
