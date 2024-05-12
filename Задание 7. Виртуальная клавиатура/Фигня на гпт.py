import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QInputDialog
from PyQt6.QtCore import Qt, QPoint, QEvent

class VirtualKeyboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.buttons = []
        self.grid_size = 40
        self.shift_pressed = False
        self.caps_lock = False
        self.dragging = False
        self.drag_start_pos = None
        self.dragged_button = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            for button in self.buttons:
                if button.geometry().contains(event.position().toPoint()):
                    self.dragging = True
                    self.dragged_button = button
                    self.drag_start_pos = event.position().toPoint() - button.pos()
                    break
            else:
                super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.dragging and event.button() == Qt.MouseButton.LeftButton:
            new_pos = event.position().toPoint() - self.drag_start_pos
            new_pos.setX((new_pos.x() // self.grid_size) * self.grid_size)
            new_pos.setY((new_pos.y() // self.grid_size) * self.grid_size)

            intersects = False
            for button in self.buttons:
                if button != self.dragged_button and button.geometry().contains(new_pos):
                    intersects = True
                    break

            if not intersects:
                self.dragged_button.move(new_pos)

            self.dragging = False
            self.dragged_button = None
            self.drag_start_pos = None
        else:
            super().mouseReleaseEvent(event)


    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Virtual Keyboard')
        self.output = QLineEdit(self)
        self.output.setGeometry(10, 10, 780, 30)

    def mouseDoubleClickEvent(self, event):
        button_char, ok = QInputDialog.getText(self, "Create Button", "Enter character for the button:")
        if ok and button_char:
            new_button = QPushButton(button_char, self)
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

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.MouseMove and source in self.buttons:
            if event.buttons() == Qt.MouseButton.LeftButton:
                new_pos = event.position().toPoint()
                # Определяем новую позицию клавиши с учетом привязки к сетке
                new_pos.setX((new_pos.x() // self.grid_size) * self.grid_size)
                new_pos.setY((new_pos.y() // self.grid_size) * self.grid_size)
                
                # Проверяем, не находится ли новая позиция внутри другой кнопки
                intersects = False
                for button in self.buttons:
                    if button != source and button.geometry().contains(new_pos):
                        intersects = True
                        break
                
                # Если новая позиция не пересекается с другими кнопками, перемещаем клавишу
                if not intersects:
                    source.move(new_pos)
                    return True
        return super().eventFilter(source, event)



    def keyPressEvent(self, event: QEvent):
        if event.key() == Qt.Key.Key_Tab:
            index = (self.buttons.index(self.focusWidget()) + 1) % len(self.buttons)
            self.buttons[index].setFocus()
        elif event.key() in (Qt.Key.Key_Up, Qt.Key.Key_Down, Qt.Key.Key_Left, Qt.Key.Key_Right):
            self.navigate_buttons(event.key())
        else:
            super().keyPressEvent(event)

    def navigate_buttons(self, key):
        current_button = self.focusWidget()
        index = self.buttons.index(current_button)
        row = index // 10  # Assuming 10 buttons per row for simplicity
        col = index % 10
        if key == Qt.Key.Key_Right and col < 9:
            self.buttons[index + 1].setFocus()
        elif key == Qt.Key.Key_Left and col > 0:
            self.buttons[index - 1].setFocus()
        elif key == Qt.Key.Key_Down and row < (len(self.buttons) // 10):
            self.buttons[min(index + 10, len(self.buttons) - 1)].setFocus()
        elif key == Qt.Key.Key_Up and row > 0:
            self.buttons[max(index - 10, 0)].setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VirtualKeyboard()
    ex.show()
    sys.exit(app.exec())
