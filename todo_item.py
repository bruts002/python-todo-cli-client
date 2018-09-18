from print_utils import print_selected, print_regular

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


  def update(self, description):
    self.description = description
  
  def toggle(self):
    self.done = not self.done
