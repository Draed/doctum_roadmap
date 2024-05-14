import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        button = QPushButton('Get User Input', self)
        button.clicked.connect(self.showInputDialog)
        layout.addWidget(button)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('User Input Example')
        self.show()

    def showInputDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter something:')

        if ok:
            QMessageBox.information(self, 'Information', f'You entered: {text}')

def main():
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
