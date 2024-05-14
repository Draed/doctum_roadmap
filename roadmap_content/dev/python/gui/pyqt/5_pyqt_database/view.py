from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit

class TodoView(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.controller.set_view(self)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(1)  # One column for the todo task
        self.table_widget.setHorizontalHeaderLabels(["Todo Task"])
        layout.addWidget(self.table_widget)

        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        self.add_button = QPushButton("Add Todo", self)
        layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_todo)

        self.setLayout(layout)

    def update_todos(self, todos):
        # Clear the existing table
        self.table_widget.setRowCount(0)

        # Populate the table with todos
        for row, todo in enumerate(todos):
            self.table_widget.insertRow(row)
            item = QTableWidgetItem(todo)
            self.table_widget.setItem(row, 0, item)

    def add_todo(self):
        task = self.line_edit.text()
        if task:
            self.controller.add_todo(task)
            self.line_edit.clear()
