from todo_item import TodoItem

class TodoList:
  def __init__(self):
    self.todo_items = []

  def add_todo(self, description):
    todo_item = TodoItem(description)
    self.todo_items.append(todo_item)
