from PyQt6 import QtWidgets, uic
import sys

path = 'C:/Code/interface_py/Задание 5. Заказ бизнес-ланча'

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi(f'{path}/ui/MainWindow.ui', self)

        self.total = 0
        self.cart = set()
        self.pricelist = {'cabbage': 100, 'chicken': 80, 'potato': 150, 'pilaf': 120, 'olivie': 60, 'cezar': 90, 'pie': 50, 'icecream': 50, 'tea': 20, 'coffee': 50}
        self.numbers_of_positions = 0
        self.buttonBox.setEnabled(False)

        self.main()

    def main(self):
        self.cabbage.clicked.connect(self.pervoe_func_cabbage)
        self.chicken.clicked.connect(self.pervoe_func_chicken)
        self.soup.stateChanged.connect(self.updatePervoe)

        self.potato.clicked.connect(self.vtoroe_func_potato)
        self.pilaf.clicked.connect(self.vtoroe_func_pilaf)
        self.hot.stateChanged.connect(self.updateVtoroe)

        self.olivie.clicked.connect(self.salad_func_olivie)
        self.cezar.clicked.connect(self.salad_func_cezar)
        self.salad.stateChanged.connect(self.updateSalad)

        self.pie.clicked.connect(self.desert_func_pie)
        self.icecream.clicked.connect(self.desert_func_icecream)
        self.desert_2.stateChanged.connect(self.updateDesert)

        self.tea.clicked.connect(self.drink_func_tea)
        self.coffee.clicked.connect(self.drink_func_coffee)
        self.drink.stateChanged.connect(self.updateDrink)

        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.pay)

# Первое блюдо

    def pervoe_func_cabbage(self):
        self.soup.setChecked(True)
        self.cart.add('cabbage')
        if 'chicken' in self.cart:
            self.total -= 80
            self.cart.remove('chicken')
        self.total += 100
        self.price.display(self.total)
        self.cabbage.setEnabled(False)
        self.chicken.setEnabled(True)
        self.logic()

    def pervoe_func_chicken(self):
        self.soup.setChecked(True)
        self.cart.add('chicken')
        if 'cabbage' in self.cart:
            self.total -= 100
            self.cart.remove('cabbage')
        self.total += 80
        self.price.display(self.total)
        self.cabbage.setEnabled(True)
        self.chicken.setEnabled(False)
        self.logic()

    def updatePervoe(self):
        if not self.soup.isChecked():
            for x in self.cart:
                if x == 'cabbage' or x == 'chicken':
                    self.total -= self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()
        else:
            for x in self.cart:
                if x == 'cabbage' or x == 'chicken':
                    self.total += self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()

# Второе блюдо

    def vtoroe_func_potato(self):
        self.hot.setChecked(True)
        self.cart.add('potato')
        if 'pilaf' in self.cart:
            self.total -= 120
            self.cart.remove('pilaf')
        self.total += 150
        self.price.display(self.total)
        self.potato.setEnabled(False)
        self.pilaf.setEnabled(True)
        self.logic()

    def vtoroe_func_pilaf(self):
        self.hot.setChecked(True)
        self.cart.add('pilaf')
        if 'potato' in self.cart:
            self.total -= 150
            self.cart.remove('potato')
        self.total += 120
        self.price.display(self.total)
        self.potato.setEnabled(True)
        self.pilaf.setEnabled(False)
        self.logic()

    def updateVtoroe(self):
        if not self.hot.isChecked():
            for x in self.cart:
                if x == 'potato' or x == 'pilaf':
                    self.total -= self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()
        else:
            for x in self.cart:
                if x == 'potato' or x == 'pilaf':
                    self.total += self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()

# Салаты

    def salad_func_olivie(self):
        self.salad.setChecked(True)
        self.cart.add('olivie')
        if 'cezar' in self.cart:
            self.total -= 90
            self.cart.remove('cezar')
        self.total += 60
        self.price.display(self.total)
        self.olivie.setEnabled(False)
        self.cezar.setEnabled(True)
        self.logic()

    def salad_func_cezar(self):
        self.salad.setChecked(True)
        self.cart.add('cezar')
        if 'olivie' in self.cart:
            self.total -= 60
            self.cart.remove('olivie')
        self.total += 90
        self.price.display(self.total)
        self.olivie.setEnabled(True)
        self.cezar.setEnabled(False)
        self.logic()

    def updateSalad(self):
        if not self.salad.isChecked():
            for x in self.cart:
                if x == 'olivie' or x == 'cezar':
                    self.total -= self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()
        else:
            for x in self.cart:
                if x == 'olivie' or x == 'cezar':
                    self.total += self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()

# Десерты

    def desert_func_pie(self):
        self.desert_2.setChecked(True)
        self.cart.add('pie')
        if 'icecream' in self.cart:
            self.total -= 50
            self.cart.remove('icecream')
        self.total += 50
        self.price.display(self.total)
        self.pie.setEnabled(False)
        self.icecream.setEnabled(True)
        self.logic()

    def desert_func_icecream(self):
        self.desert_2.setChecked(True)
        self.cart.add('icecream')
        if 'pie' in self.cart:
            self.total -= 50
            self.cart.remove('pie')
        self.total += 50
        self.price.display(self.total)
        self.pie.setEnabled(True)
        self.icecream.setEnabled(False)
        self.logic()

    def updateDesert(self):
        if not self.desert_2.isChecked():
            for x in self.cart:
                if x == 'pie' or x == 'icecream':
                    self.total -= self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()
        else:
            for x in self.cart:
                if x == 'pie' or x == 'icecream':
                    self.total += self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()

# Напиток

    def drink_func_tea(self):
        self.drink.setChecked(True)
        self.cart.add('tea')
        if 'coffee' in self.cart:
            self.total -= 50
            self.cart.remove('coffee')
        self.total += 20
        self.price.display(self.total)
        self.tea.setEnabled(False)
        self.coffee.setEnabled(True)
        self.logic()

    def drink_func_coffee(self):
        self.drink.setChecked(True)
        self.cart.add('coffee')
        if 'tea' in self.cart:
            self.total -= 20
            self.cart.remove('tea')
        self.total += 50
        self.price.display(self.total)
        self.tea.setEnabled(True)
        self.coffee.setEnabled(False)
        self.logic()

    def updateDrink(self):
        if not self.drink.isChecked():
            for x in self.cart:
                if x == 'tea' or x == 'coffee':
                    self.total -= self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()
        else:
            for x in self.cart:
                if x == 'tea' or x == 'coffee':
                    self.total += self.pricelist[x]
                    self.price.display(self.total)
                    self.logic()

    def logic(self):
        self.numbers_of_positions = 0

        for x in (self.soup, self.hot, self.salad, self.desert_2, self.drink):
            if x.isChecked():
                self.numbers_of_positions += 1

        if self.numbers_of_positions >= 2:
            self.buttonBox.setEnabled(True)
            print(self.numbers_of_positions)
        else:
            self.buttonBox.setEnabled(False)
            print(self.numbers_of_positions)

        print(self.numbers_of_positions)

    def pay(self):
        self.notification.setText(f'Итого к оплате {self.total}. Можете подойти к терминалу для оплаты заказа.')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())