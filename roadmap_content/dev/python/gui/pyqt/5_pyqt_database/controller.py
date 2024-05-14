from PyQt6.QtCore import QObject

class TodoController(QObject):
    def __init__(self, model):
        super().__init__()

        self.model = model
        self.view = None  # Will be set by the view using set_view method

        # Connect signals from the model to controller methods
        self.model.data_changed.connect(self.update_view)

    def set_view(self, view):
        self.view = view

    def add_todo(self, task):
        self.model.add_todo(task)

    def update_view(self):
        todos = self.model.get_todos()
        if self.view:
            self.view.update_todos(todos)
