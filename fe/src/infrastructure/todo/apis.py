from src.core.todo import Todo

class TodoAPI:
    todos = {}

    def create_todo(self, title, description, priority, due_date):
        todo = Todo(title, description, priority, due_date)
        todo_id = len(self.todos) + 1
        self.todos[todo_id] = todo

    def get_todo(self, todo_id):
        return self.todos.get(todo_id)

    def update_todo(self, todo_id, title, description, priority, due_date):
        if todo_id in self.todos:
            todo = Todo(title, description, priority, due_date)
            self.todos[todo_id] = todo

    def delete_todo(self, todo_id):
        if todo_id in self.todos:
            del self.todos[todo_id]
