import requests

config = {
  'protocol': 'http',
  'host': 'localhost',
  'port': '5000'
}

class TodoURLs:
  LIST = '/api/todo_app/list/'
  TODO = '/api/todo_app/todo/'

def get_url(endpoint):
  global config
  return config['protocol'] + '://' + config['host'] + ':' + config['port'] + endpoint


def get_todos(list_name):
  url = get_url(TodoURLs.TODO)
  res = requests.get(url)
  all_todos = res.json()
  todo_list = [todo for todo in all_todos if todo['name'] == list_name]
  list_id = todo_list[0]['id']
  return (list_id, todo_list[0]['todos'])


def add_todo(list_id, desc):
  url = get_url(TodoURLs.TODO)
  payload = {
    'todo': desc,
    'listId': list_id
  }
  requests.post(url, json=payload)


def toggle_todo(id, new_done):
  url = get_url(TodoURLs.TODO)
  payload = {
    'id': id,
    'isDone': new_done
  }
  requests.put(url, json=payload)


def remove_todo(id):
  url = get_url(TodoURLs.TODO)
  payload = { 'todoId': id }
  requests.delete(url, json=payload)

if __name__ == '__main__':
  print(get_todos('Terminal'))
