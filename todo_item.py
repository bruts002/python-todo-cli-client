
class TodoItem:
  def __init__(self, description):
    self.description = description
    self.done = False
  
  def toggle(self):
    self.done = not self.done
