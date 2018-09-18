from terminal_utils import get_terminal_size, clear_terminal
from todo_list import TodoList

# width, height = get_terminal_size()
# print('width =', width, 'height =', height)

list_name = 'Terminal'
my_list = TodoList(list_name)


def render():
  clear_terminal()
  my_list.render()

def get_user_choice():
  print("\n[a]dd a todo")
  print("[c]hoose a todo")
  print("[q]uit.")
  
  return input("What would you like to do? ")

def get_new_todo():
  new_todo = input("New Todo: ")
  my_list.add_todo(new_todo)


def main():
  choice = ''
  while choice != 'q':
    render()
    choice = get_user_choice()
    if choice == 'a':
      get_new_todo()
    elif choice == 'c':
      my_list.select()


if __name__ == '__main__':
  main()

