import sys
from PyQt6 import QtCore, QtWidgets


account_content = [
            {'Date': '01/01/2024', 'Value': 60, 'Category': 'car'},
            {'Date': '01/01/2024', 'Value': 12.25, 'Category': 'other' },
            {'Date': '01/01/2024', 'Value': 32.50, 'Category': 'food' },
        ]


class Main_window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main_window, self).__init__(parent)
        self.setGeometry(50, 50, 1100, 750)
        self.setWindowTitle("Programm")  

        # open_new_file = QtWidgets.QAction('New', self)
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Projekt')
        # fileMenu.addAction(open_new_file)

        self.tabWidget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tabWidget)

        self.tab_v1 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_v1, "Tab 1")
        self.openFile =QtWidgets.QPushButton("Choose Tab ", self.tab_v1)
        self.openFile.setGeometry(QtCore.QRect(700, 25, 200, 30))

        # self.tab_v2 = QtWidgets.QWidget()
        # self.tabWidget.addTab(self.tab_v2, "Tab 2")

        self.tab_account = QtWidgets.QTableWidget()
        self.tabWidget.addTab(self.tab_account, 'Account')
        QtWidgets.QPushButton("Choose Tab ", self.tab_account)

        

        ### Account Table (account tab content)
        self.tab_account.setColumnCount(3)
        self.tab_account.setColumnWidth(0, 150)
        self.tab_account.setColumnWidth(1, 200)
        self.tab_account.setColumnWidth(2, 135)

        self.tab_account.setHorizontalHeaderLabels(account_content[0].keys())
        self.tab_account.setRowCount(len(account_content))

        row = 0
        for e in account_content:
            self.tab_account.setItem(row, 0, QtWidgets.QTableWidgetItem(str(e['Date'])))
            self.tab_account.setItem(row, 1, QtWidgets.QTableWidgetItem(str(e['Value'])))
            self.tab_account.setItem(row, 2, QtWidgets.QTableWidgetItem(str(e['Category'])))
            row += 1

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Main_window()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()