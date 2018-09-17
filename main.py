from terminal_utils import get_terminal_size, clear_terminal
from todo_api import get_todos
from todo_list import TodoList
from msvcrt import getch

# width, height = get_terminal_size()
# print('width =', width, 'height =', height)

choice = ''
selected_todo_index = -1
my_list = TodoList()
todos = get_todos()
for todo in todos:
  my_list.add_todo(todo['todo'], todo['isDone'])

class Colors:
  HEADER = '\033[95m'
  BLACK = '\033[30m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

class Backgrounds:
  BLACK  = "\033[0;100m"   # Black
  RED    = "\033[0;101m"     # Red
  GREEN  = "\033[0;102m"   # Green
  YELLOW = "\033[0;103m"  # Yellow
  BLUE   = "\033[0;104m"    # Blue
  PURPLE = "\033[10;95m"  # Purple
  CYAN   = "\033[0;106m"    # Cyan
  WHITE  = "\033[0;107m"   # White

class Keys:
  PRE_ARROW = b'\xe0'
  ESCAPE    = b'\x1b'
  DOWN      = b'P'
  UP        = b'H'
  ENTER     = b'\r'


show = 20

def print_done(done):
  if done:
    return '[x]'
  else:
    return '[ ]'

def print_selected(item, done):
  print(
    Backgrounds.YELLOW,
    Colors.OKBLUE,
    item[0:show].ljust(show),
    print_done(done),
    Colors.ENDC
  )

def print_regular(item, done):
  print(
    ' ',
    item[0:show].ljust(show),
    print_done(done)
  )

def print_header():
  print(
    Backgrounds.WHITE,
    Colors.BLACK,
    '#  TODOS             DONE',
    Colors.ENDC
  )


def render():
  clear_terminal()
  print_header()
  for index, todo in enumerate(my_list.todo_items, start=1):
    description = str(index) + '. ' + todo.description
    if index == selected_todo_index + 1:
      print_selected(description, todo.done)
    else:
      print_regular(description, todo.done)

def get_user_choice():
  # Let users know what they can do.
  print("\n[a] Add a todo")
  print("[c] Choose a todo")
  print("[q] Quit.")
  
  return input("What would you like to do? ")

def get_new_todo():
  new_todo = input("New Todo: ")
  my_list.add_todo(new_todo)

def choose_todo():
  max_todo_number = len(my_list.todo_items) - 1
  global selected_todo_index
  selected_todo_index = 0
  c = '0'.encode('ascii')
  maybe_arrow_key = False
  while c != Keys.ESCAPE:
    render()
    print_edit_options()
    c = getch()
    if maybe_arrow_key:
      if c == Keys.DOWN:
        selected_todo_index = min(max_todo_number, selected_todo_index + 1)
      elif c == Keys.UP:
        selected_todo_index = max(0, selected_todo_index - 1)

    if c == Keys.PRE_ARROW:
      maybe_arrow_key = True
    else:
      maybe_arrow_key = False

    if c == b'u':
      update_todo()
    elif c == b'd':
      delete_todo()
    elif c == b't':
      toggle_todo()

    # print('You entered', c)
    # print('selected_todo_index = ', selected_todo_index)
  selected_todo_index = -1

def print_edit_options():
  print("\n[u]pdate")
  print("[d]elete")
  print("[t]oggle complete")

def update_todo():
  description = input('Updated description: ')
  my_list.update_todo(selected_todo_index, description)

def delete_todo():
  global selected_todo_index
  my_list.delete_todo(selected_todo_index)
  max_todo_number = len(my_list.todo_items) - 1
  selected_todo_index = min(max_todo_number, selected_todo_index)

def toggle_todo():
  my_list.toggle_todo(selected_todo_index)


while choice != 'q':
  render()
  choice = get_user_choice()
  if choice == 'a':
    get_new_todo()
  elif choice == 'c':
    choose_todo()

