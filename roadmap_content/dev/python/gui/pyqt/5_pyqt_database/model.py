from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

class TodoModel(QObject):
    data_changed = pyqtSignal()

    def __init__(self, database_path="todo_database.db"):
        super().__init__()

        self.database_path = database_path
        self.initialize_database()

    def initialize_database(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.database_path)

        if not db.open():
            print("Error: Could not open the database.")
            return False

        query = QSqlQuery()
        query.exec(
            '''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL
            )
            '''
        )

    def get_todos(self):
        todos = []

        query = QSqlQuery("SELECT * FROM todos")
        while query.next():
            task = query.value(1)
            todos.append(task)

        return todos

    def add_todo(self, task):
        query = QSqlQuery()
        query.prepare("INSERT INTO todos (task) VALUES (:task)")
        query.bindValue(":task", task)
        query.exec()

        self.data_changed.emit()