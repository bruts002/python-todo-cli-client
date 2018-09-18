from todo_api import get_todos, add_todo
from todo_item import TodoItem
from terminal_utils import clear_terminal
from print_utils import print_header
from input_utils import Keys
from msvcrt import getch

class TodoList:
  def __init__(self, list_name):
    self.name = list_name
    self.id = -1
    self.current = -1
    self.todos = []
    self.__refresh__()

  def __refresh__(self):
    id, todos = get_todos(self.name)
    self.id = id
    self.todos = list(
      map(
        lambda todo: TodoItem(todo),
        todos
      )
    )

  def render(self):
    show = 20
    print_header(' TODOS             DONE')
    for index, todo in enumerate(self.todos):
      todo.render(show, index == self.current)


  @staticmethod
  def print_edit_options():
    print("\n[u]pdate")
    print("[d]elete")
    print("[t]oggle complete")

  
  def select(self):
    max_index = len(self.todos) - 1
    self.current = 0
    c = '0'.encode('ascii')
    maybe_arrow_key = False
    while c != Keys.ESCAPE:
      clear_terminal() # TODO: don't do this here, use a library and just clear the lists coords
      self.render()
      TodoList.print_edit_options()
      c = getch()
      if maybe_arrow_key:
        if c == Keys.DOWN:
          self.current = min(max_index, self.current + 1)
        elif c == Keys.UP:
          self.current = max(0, self.current - 1)
  
      if c == Keys.PRE_ARROW:
        maybe_arrow_key = True
      else:
        maybe_arrow_key = False
  
      if c == b'u':
        self.update_todo()
      elif c == b'd':
        self.delete_todo()
      elif c == b't':
        self.toggle_todo()
  
    self.current = -1


  def add_todo(self, description):
    add_todo(self.id, description)
    self.__refresh__()


  def update_todo(self):
    self.todos[self.current].update()
    self.__refresh__()


  def toggle_todo(self):
    self.todos[self.current].toggle()
    self.__refresh__()


  def delete_todo(self):
    self.todos[self.current].remove()
    self.__refresh__()

