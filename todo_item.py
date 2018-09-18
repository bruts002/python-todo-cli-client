from print_utils import print_selected, print_regular
from todo_api import remove_todo, toggle_todo, update_todo, add_todo

class TodoItem:
  def __init__(self, todo):
    description, id, done = todo['todo'], todo['id'], todo['isDone']
    self.description = description
    self.id = id
    self.done = done

  def render(self, show, selected=False):
    text = self.description[0:show].ljust(show)
    if self.done:
      text += '[x]'
    else:
      text += '[ ]'
    if selected:
      print_selected(text)
    else:
      print_regular(text)


  def remove(self):
    remove_todo(self.id)


  def update(self):
    todo = input("Update todo: ")
    update_todo(self.id, todo)
  

  def toggle(self):
    toggle_todo(self.id, not self.done)


  @staticmethod
  def add(list_id):
    todo = input('New todo: ')
    add_todo(list_id, todo)
