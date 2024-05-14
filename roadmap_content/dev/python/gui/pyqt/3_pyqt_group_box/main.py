import sys
from PyQt6.QtWidgets import  (
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QPushButton, 
    QInputDialog, 
    QMessageBox,
    QGroupBox

)
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    groupBox = QGroupBox("Exclusive Radio Buttons")
    radio1 = QRadioButton("Radio button 1")
    radio2 = QRadioButton("Radio button 2")
    radio3 = QRadioButton("Radio button 3")
    radio1.setChecked(True)