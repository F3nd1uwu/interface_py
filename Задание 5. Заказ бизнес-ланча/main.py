from PyQt6 import QtWidgets, uic
import sys

path = 'C:/Code/interface_py/Задание 5. Заказ бизнес-ланча'

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi(f'{path}/ui/MainWindow.ui', self)

        self.main()

    def main(self):
        self.cabbage.clicked.connect(self.pervoe_func_cabbage)
        self.chicken.clicked.connect(self.pervoe_func_chicken)
        self.soup.stateChanged.connect(self.updatePervoe)

    def pervoe_func_cabbage(self):
        if self.cabbage.isChecked() and not self.soup.isChecked():
            self.soup.setChecked(True)

    def pervoe_func_chicken(self):
        if self.chicken.isChecked() and not self.soup.isChecked():
            self.soup.setChecked(True)

    def updatePervoe(self):
        if not self.soup.isChecked():
            self.cabbage.setChecked(False)
            self.chicken.setChecked(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())