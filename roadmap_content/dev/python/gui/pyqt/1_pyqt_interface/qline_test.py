import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_line_edit = QLineEdit(self)
        layout.addWidget(self.input_line_edit)

        button = QPushButton('Print Input', self)
        button.clicked.connect(self.printInput)
        layout.addWidget(button)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('User Input Example')
        self.show()

    def printInput(self):
        text = self.input_line_edit.text()

        if text:
            QMessageBox.information(self, 'Information', f'You entered: {text}')
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter something.')

def main():
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
