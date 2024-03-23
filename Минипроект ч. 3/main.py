import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import json


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('ui/MainWindow.ui', self)

        self.signals()
        self.icons()
        self.variables()

    def variables(self):
        self.file_name = ''
        self.user_info = {}

    def signals(self):
        self.exit_btn.clicked.connect(self.close)
        self.exit_act.triggered.connect(lambda: MainWindow.close(self))
        self.new_vote.triggered.connect(self.create_new_dialog_n)
        self.change_vote.triggered.connect(self.create_new_dialog_c)
        self.open_vote.triggered.connect(self.open_file_func)
        self.argument_box.currentIndexChanged.connect(self.update_lcd)
        self.vote_btn.clicked.connect(self.vote_func)

    def icons(self):
        self.new_vote.setIcon(QIcon('ico/new.png'))
        self.open_vote.setIcon(QIcon('ico/open.png'))
        self.close_vote.setIcon(QIcon('ico/close.png'))
        self.exit_act.setIcon(QIcon('ico/exit.png'))
        self.change_vote.setIcon(QIcon('ico/change.png'))
        self.reset_votes.setIcon(QIcon('ico/reset.png'))
        self.vote_btn.setIcon(QIcon('ico/check.png'))
        self.exit_btn.setIcon(QIcon('ico/exit.png'))

    def create_new_dialog_n(self):
        self.NewFlag = True
        NewWindow(self).show()
        #self.hide() Добавить в самом конце
    
    def create_new_dialog_c(self):
        self.NewFlag = False
        NewWindow(self).show()
        #self.hide() Добавить в самом конце
    
    def open_file_func(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(None, 'Открыть...', '', '*.json')[0]
        if self.file_name:
            try:
                with open(self.file_name, 'r') as file:
                    self.user_info = json.load(file)
                    self.logic()
            except FileNotFoundError:
                pass
    
    def save_file_func(self):
        if self.file_name:
            with open(self.file_name, 'w') as file:
                json.dump(self.user_info, file)
        else:
            pass

    def logic(self):
        self.question_lbl.setText(list(self.user_info.keys())[0])
        for value in self.user_info.values():
            for item in value:
                self.argument_box.addItem(item[0])
    
    def update_lcd(self):
        index = self.argument_box.currentIndex()
        value = list(self.user_info.values())[0][index][1]
        self.votes_number.display(int(value))

    def vote_func(self):
        index = self.argument_box.currentIndex()
        value = int(self.user_info[list(self.user_info.keys())[0]][index][1]) + 1
        self.user_info[list(self.user_info.keys())[0]][index][1] = str(value)
        self.votes_number.display(value)
        self.save_file_func()


class NewWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        uic.loadUi('ui/arguments.ui', self)

        self.user_info = {}

        self.new_signals()
        self.new_icons()

    def new_icons(self):
        self.up.setIcon(QIcon('ico/up.png'))
        self.down.setIcon(QIcon('ico/down.png'))
        self.create_arg.setIcon(QIcon('ico/plus.png'))
        self.delete_arg.setIcon(QIcon('ico/trash.png'))

    def new_signals(self):
        self.buttonBox.accepted.connect(self.save_func)
        self.create_arg.clicked.connect(self.add_to_list)
        self.delete_arg.clicked.connect(self.delete_from_list)
        self.up.clicked.connect(self.up_func)
        self.down.clicked.connect(self.down_func)

    def add_to_list(self):
        all_items = []
        for index in range(self.list_of_args.count()):
            item = self.list_of_args.item(index)
            all_items.append(item.text())
        if self.edit_arg.text() not in all_items:
            self.list_of_args.addItem(self.edit_arg.text())
            self.edit_arg.setText('')
        else:
            pass

    def delete_from_list(self):
        selected_item = self.list_of_args.currentItem()
        if selected_item:
            self.list_of_args.takeItem(self.list_of_args.row(selected_item))

    def up_func(self):
        selected_item = self.list_of_args.currentItem()
        if selected_item:
            index1 = self.list_of_args.row(selected_item)
            if index1 != 0:
                index2 = index1 - 1
                print(index1, index2) #Проверка индексов, потом убрать
                item1 = self.list_of_args.takeItem(index1)
                item2 = self.list_of_args.takeItem(index2)
                self.list_of_args.insertItem(index2 - 2, item1) #Проблема в индексах, при takeItem убирается из листа 2 элемента, что нарушает порядок
                self.list_of_args.insertItem(index1 - 1, item2) #Надо как то пофиксить. Так же для down_func
                self.list_of_args.setCurrentRow(index2)

    def down_func(self):
        selected_item = self.list_of_args.currentItem()
        if selected_item:
            index1 = self.list_of_args.row(selected_item)
            if index1 != self.list_of_args.count():
                index2 = index1 + 1
                print(index1, index2) #Проверка индексов, потом убрать
                item1 = self.list_of_args.takeItem(index1)
                item2 = self.list_of_args.takeItem(index2)
                self.list_of_args.insertItem(index1 - 2, item2)
                self.list_of_args.insertItem(index2 - 1, item1)
                self.list_of_args.setCurrentRow(index2)

    def save_func(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(None, 'Сохранить как...', '', '*.json')[0]
        if file_name:
            try:
                with open(file_name, 'w') as file:
                    json.dump(self.user_info, file)
            except Exception as e:
                print(f"Ошибка сохранения: {e}")
        else:
            pass
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
