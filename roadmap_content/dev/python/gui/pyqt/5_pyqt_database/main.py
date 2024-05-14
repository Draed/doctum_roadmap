from PyQt6.QtWidgets import QApplication
from model import TodoModel
from view import TodoView
from controller import TodoController

def main():
    app = QApplication([])

    # Initialize the database with the model
    todo_model = TodoModel()
    todo_model.initialize_database()

    todo_view = TodoView(TodoController(todo_model))

    # Show the view
    todo_view.show()

    # Execute the application event loop
    app.exec()

if __name__ == "__main__":
    main()
