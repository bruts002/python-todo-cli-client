import requests

list_name = 'Terminal'
config = {
  'protocol': 'http',
  'host': 'localhost',
  'port': '5000'
}

class TodoURLs:
  LIST = '/api/todo_app/list'
  TODO = '/api/todo_app/todo'

def get_url(endpoint):
  global config
  return config['protocol'] + '://' + config['host'] + ':' + config['port'] + endpoint


def get_todos():
  url = get_url(TodoURLs.TODO)
  res = requests.get(url)
  all_todos = res.json()
  global list_name
  todo_list = [todo for todo in all_todos if todo['name'] == list_name]
  print(todo_list[0]['todos'])

if __name__ == '__main__':
  get_todos()
