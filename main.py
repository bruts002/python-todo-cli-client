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
  print("[f]ocus list")
  print("[q]uit.")
  
  return input("What would you like to do? ")


def main():
  choice = ''
  while choice != 'q':
    render()
    choice = get_user_choice()
    if choice == 'f':
      my_list.focus()


if __name__ == '__main__':
  main()

