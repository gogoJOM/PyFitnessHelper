from main_window import *
import sys
from PyQt5.QtWidgets import QMessageBox
from FHDataBase import FHProductsDataBase, FHPersonalDataBase
from utils import FHProduct, FHDay


row_names = ('Name', 'Age', 'Kilocalories (per day)')


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.verticalLayoutWidget.hide()
        self.ui.pushButton_3.clicked.connect(self.ui.verticalLayoutWidget.hide)

        self.PersonalDB = None

        # Table with User info
        self.ui.tableWidget.setRowCount(len(row_names))
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setVerticalHeaderLabels(row_names)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Fill values'])

        # Choose Excisting User
        self.ui.pushButton.clicked.connect(self.btnClicked_ChooseUser)

        # Create New User
        self.ui.pushButton_2.clicked.connect(self.btnClicked_CreateUser)

    def btnClicked_ChooseUser(self):
        return

    def btnClicked_CreateUser(self):
        name = self.ui.tableWidget.item(0, 0)
        if name is None:
            QMessageBox.about(self, "Message", "Please, fill new user name")
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
        self.PersonalDB = FHPersonalDataBase(name)
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec_())