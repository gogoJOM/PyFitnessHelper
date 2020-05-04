from main_window import *
import sys
from PyQt5.QtWidgets import QMessageBox, QFrame, QTableWidgetItem
from FHDataBase import FHProductsDataBase, FHPersonalDataBase
from utils import FHProduct, FHDay, LoadUsernames, SaveUsernames
import datetime

row_names = ('Name', 'Desired Weight', 'Kilocalories (per day)')
meal_names = ('Breakfast', 'Lunch', 'Dinner', 'Snacks')


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load existing usernames
        self.UserNames = LoadUsernames()
        self.PersonalDB = None
        self.CurrentDay = None
        self.ui.comboBox.addItem('New')
        for username in self.UserNames:
            self.ui.comboBox.addItem(username)
        self.ui.comboBox.setCurrentIndex(0)

        # Load Product database
        self.ProductDB = FHProductsDataBase()
        self.ProductDB.Open()
        self.init_product_combobox()

        # Hide user form
        self.hide_dayinfo_layout()

        # Table with User info
        self.ui.tableWidget.setRowCount(len(row_names))
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setVerticalHeaderLabels(row_names)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Fill values'])

        # Choose Excisting User
        self.ui.pushButton.clicked.connect(self.btnClicked_ChooseUser)

        # Create New User
        self.ui.pushButton_2.clicked.connect(self.btnClicked_CreateUser)

        # Add product to meal
        self.ui.pushButton_3.clicked.connect(self.btnClicked_Add)

        # Add product to DB
        self.ui.pushButton_5.clicked.connect(self.btnClicked_CreateProduct)

    def save(self):
        if self.PersonalDB is not None:
            self.PersonalDB.Save()
        SaveUsernames(self.UserNames)
        self.ProductDB.Save()
        return

    def hide_dayinfo_layout(self):
        self.PersonalDB = None
        self.CurrentDay = None
        self.ui.frame.hide()
        if not hasattr(self.ui, 'new_product_frame'):
            self.ui.new_product_frame = QtWidgets.QFrame()
            self.ui.new_product_frame.setLayout(self.ui.gridLayout_2)
        self.ui.new_product_frame.hide()
        return

    def init_product_combobox(self):
        self.ui.comboBox_4.addItem('New')
        items = list(self.ProductDB.keys())
        for item in items:
            self.ui.comboBox_4.addItem('{} {}kc/100g'.format(item, self.ProductDB[item]))
        self.ui.comboBox_4.setCurrentIndex(0)

        for item in meal_names:
            self.ui.comboBox_3.addItem(item)
        self.ui.comboBox_3.setCurrentIndex(0)

        return

    def btnClicked_ChooseUser(self):
        name = str(self.ui.comboBox.currentText())
        if name == 'New':
            QMessageBox.about(self, "Message", "Please, choose existing user")
            self.hide_dayinfo_layout()
        else:
            if self.PersonalDB is not None:
                self.PersonalDB.Save()
            self.PersonalDB = FHPersonalDataBase(name)
            self.PersonalDB.Open()
            self.show_user_info()
            self.show_daysDB()
        return

    def show_user_info(self):
        if self.PersonalDB is not None:
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(self.PersonalDB.name))
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(self.PersonalDB.desired_weight))
            self.ui.tableWidget.setItem(2, 0, QTableWidgetItem(self.PersonalDB.desired_kcal))
        return

    def btnClicked_CreateUser(self):
        name = self.ui.tableWidget.item(0, 0)
        if name is None:
            QMessageBox.about(self, "Message", "Please, fill new user name")
            self.hide_dayinfo_layout()
            return
        if name.text() in self.UserNames:
            QMessageBox.about(self, "Message", "This user name already exist")
            self.hide_dayinfo_layout()
            return
        name = name.text()
        weight = self.ui.tableWidget.item(1, 0)
        if weight is None:
            QMessageBox.about(self, "Message", "Please, fill desired weight")
            self.hide_dayinfo_layout()
            return
        try:
            weight = int(weight.text())
        except:
            QMessageBox.about(self, "Message", "Weight is not a number")
            self.hide_dayinfo_layout()
            return
        kilocalories = self.ui.tableWidget.item(2, 0)
        if kilocalories is None:
            QMessageBox.about(self, "Message", "Please, fill expected amount of kilocalories")
            self.hide_dayinfo_layout()
            return
        try:
            kilocalories = int(kilocalories.text())
        except:
            QMessageBox.about(self, "Message", "Kilocalories is not a number")
            self.hide_dayinfo_layout()
            return
        if self.PersonalDB is not None:
            self.PersonalDB.Save()
        self.PersonalDB = FHPersonalDataBase(name, desired_weight=weight, desired_kcal=kilocalories)
        self.PersonalDB.Open()
        self.UserNames.append(name)
        self.show_daysDB()
        return

    def show_daysDB(self):
        if self.PersonalDB is not None:
            days = list(self.PersonalDB.keys())
            now = datetime.datetime.now()
            today = "{}-{}-{}".format(now.day, now.month, now.year)
            if today not in days:
                days.append(today)
                self.PersonalDB[today] = FHDay()
            self.CurrentDay = self.PersonalDB[today]
            for day in days:
                self.ui.comboBox_2.addItem(day)
            self.ui.comboBox_2.setCurrentIndex(len(days) - 1)
        self.ui.frame.show()
        return

    def btnClicked_Add(self):
        product = str(self.ui.comboBox_4.currentText())
        if product == 'New':
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            self.ui.new_product_frame.show()
            return

        day = str(self.ui.comboBox_2.currentText())
        meal = str(self.ui.comboBox_3.currentText())
        product = str(self.ui.comboBox_4.currentText())
        product = ' '.join(product.split(' ')[:-1])
        self.CurrentDay = self.PersonalDB[day]
        amount = self.ui.spinBox.value() * self.ProductDB[product] / 100
        if amount > 0:
            fh_product = FHProduct(product, amount)
            if meal == 'Breakfast':
                self.CurrentDay.AddBreakfast(fh_product)
            elif meal == 'Lunch':
                self.CurrentDay.AddLunch(fh_product)
            elif meal == 'Dinner':
                self.CurrentDay.AddDinner(fh_product)
            else:
                self.CurrentDay.AddSnack(fh_product)

        return

    def btnClicked_CreateProduct(self):
        product_name = self.ui.lineEdit.text()
        if product_name == '':
            return
        if product_name in self.ProductDB:
            return
        kc = self.ui.lineEdit_2.text()
        if kc == '':
            return
        try:
            kc = int(kc)
        except:
            return
        self.ProductDB[product_name] = kc
        self.ui.comboBox_4.addItem('{} {}kc/100g'.format(product_name, self.ProductDB[product_name]))
        self.ui.new_product_frame.hide()
        return

    def show_day(self):
        self.ui.tableWidget1.setRowCount(len(meal_names))
        self.ui.tableWidget1.setColumnCount(2)
        self.ui.tableWidget.setVerticalHeaderLabels(meal_names)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Product names', 'kc'])
        # if self.PersonalDB is not None and self.CurrentDay is not None:
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    app.exec()
    application.save()