from terminal_utils import get_terminal_size, clear_terminal
from todo_list import TodoList

# width, height = get_terminal_size()
# print('width =', width, 'height =', height)

choice = ''
my_list = TodoList()
my_list.add_todo('Learn python')

def render():
  clear_terminal()
  for index, todo in enumerate(my_list.todo_items, start=1):
    print(index, ': ', todo.description)

def get_user_choice():
  # Let users know what they can do.
  print("\n[a] Add a todo")
  print("[c] Choose a todo")
  print("[q] Quit.")
  
  return input("What would you like to do? ")

def get_new_todo():
  new_todo = input("New Todo: ")
  my_list.add_todo(new_todo)


while choice != 'q':
  render()
  choice = get_user_choice()
  if choice == 'a':
    get_new_todo()

