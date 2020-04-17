from main_window import *
import sys
from PyQt5.QtWidgets import QMessageBox, QFrame
from FHDataBase import FHProductsDataBase, FHPersonalDataBase
from utils import FHProduct, FHDay, LoadUsernames, SaveUsernames


row_names = ('Name', 'Age', 'Kilocalories (per day)')


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load existing usernames
        self.UserNames = LoadUsernames()
        self.PersonalDB = None
        self.ui.comboBox.addItem('New')
        for username in self.UserNames:
            self.ui.comboBox.addItem(username)
        self.ui.comboBox.setCurrentIndex(0)

        # Hide user form
        self.ui.formLayoutWidget.hide()

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

    def btnClicked_ChooseUser(self):
        name = str(self.ui.comboBox.currentText())
        if name == 'New':
            QMessageBox.about(self, "Message", "Please, choose existing user")
        else:
            if self.PersonalDB is not None:
                self.PersonalDB.Save()
            self.PersonalDB = FHPersonalDataBase(name)
            self.PersonalDB.Open()
            self.ui.formLayoutWidget.show()
        return

    def btnClicked_CreateUser(self):
        name = self.ui.tableWidget.item(0, 0)
        if name is None:
            QMessageBox.about(self, "Message", "Please, fill new user name")
        else:
            if name in self.UserNames:
                QMessageBox.about(self, "Message", "This user name already exist")
            else:
                name = name.text()
        age = self.ui.tableWidget.item(1, 0)
        if age is None:
            QMessageBox.about(self, "Message", "Please, fill new user age")
        else:
            age = int(age.text())
        kilocalories = self.ui.tableWidget.item(2, 0)
        if age is None:
            QMessageBox.about(self, "Message", "Please, fill expected amount of kilocalories")
        else:
            kilocalories = int(kilocalories.text())
        if self.PersonalDB is not None:
            self.PersonalDB.Save()
        self.PersonalDB = FHPersonalDataBase(name)
        self.PersonalDB.Open()
        self.UserNames.append(name)
        self.ui.formLayoutWidget.show()
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    app.exec()
    application.save()