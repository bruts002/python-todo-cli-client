from todo_item import TodoItem

class TodoList:
  def __init__(self):
    self.todo_items = []

  def add_todo(self, description, done=False):
    todo_item = TodoItem(description, done)
    self.todo_items.append(todo_item)

  def update_todo(self, index, description):
    self.todo_items[index].update(description)

  def toggle_todo(self, index):
    self.todo_items[index].toggle()

  def delete_todo(self, index):
    del self.todo_items[index]
