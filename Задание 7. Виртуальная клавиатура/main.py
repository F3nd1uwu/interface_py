from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPoint
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.buttons = []
        self.shift_pressed = False
        self.caps_lock = False
        self.setMouseTracking(True)

        self.ui()

    def ui(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Виртуальная клавиатура')
        self.output = QtWidgets.QLineEdit(self)
        self.output.setGeometry(10, 10, 780, 30)

    def mouseDoubleClickEvent(self, event):
        button_char, ok = QtWidgets.QInputDialog.getText(self, "Создание кнопки", "Введите символ для кнопки:")
        if ok and button_char:
            new_button = QtWidgets.QPushButton(button_char, self)
            new_button.move(event.position().toPoint())
            new_button.show()
            new_button.pressed.connect(lambda c=button_char: self.add_character(c))
            new_button.installEventFilter(self)
            self.buttons.append(new_button)

    def add_character(self, char):
        if char.lower() in ('shift', 'caps lock', 'backspace'):
            self.handle_special_keys(char)
        elif self.shift_pressed or self.caps_lock:
            self.output.insert(char.upper())
            if self.shift_pressed:
                self.shift_pressed = False
        else:
            self.output.insert(char)

    def handle_special_keys(self, key):
        if key == 'shift':
            self.shift_pressed = True
        elif key == 'caps lock':
            self.caps_lock = not self.caps_lock
        elif key == 'backspace':
            current_text = self.output.text()
            self.output.setText(current_text[:-1])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())