from main_window import *
import sys
from PyQt5.QtWidgets import QMessageBox, QFrame, QTableWidgetItem
from FHDataBase import FHProductsDataBase, FHPersonalDataBase
from utils import FHProduct, FHDay, LoadUsernames, SaveUsernames
import datetime


row_names = ('Name', 'Desired Weight', 'Kilocalories (per day)')


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

    def save(self):
        if self.PersonalDB is not None:
            self.PersonalDB.Save()
        SaveUsernames(self.UserNames)
        return

    def hide_dayinfo_layout(self):
        self.PersonalDB = None
        self.CurrentDay = None
        self.ui.formLayoutWidget.hide()
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
        else:
            if name in self.UserNames:
                QMessageBox.about(self, "Message", "This user name already exist")
                self.hide_dayinfo_layout()
                return
            else:
                name = name.text()
        weight = self.ui.tableWidget.item(1, 0)
        if weight is None:
            QMessageBox.about(self, "Message", "Please, fill desired weight")
            self.hide_dayinfo_layout()
            return
        else:
            weight = int(weight.text())
        kilocalories = self.ui.tableWidget.item(2, 0)
        if kilocalories is None:
            QMessageBox.about(self, "Message", "Please, fill expected amount of kilocalories")
            self.hide_dayinfo_layout()
            return
        else:
            kilocalories = int(kilocalories.text())
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
            self.ui.comboBox_2.setCurrentIndex(len(days)-1)
        self.ui.formLayoutWidget.show()
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    app.exec()
    application.save()