
class TodoItem:
  def __init__(self, description, done=False):
    self.description = description
    self.done = done

  def update(self, description):
    self.description = description
  
  def toggle(self):
    self.done = not self.done
