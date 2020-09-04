import json
from flask import Blueprint, request, jsonify

todos = [
  { 'id': 1, 'title': 'Hello, TodoApp!', 'done': False }
]

app = Blueprint('todos', __name__)

@app.route('/todos', methods = [ 'GET' ])
def getTodos():
  return { 'todos': todos }

@app.route('/todos', methods = [ 'POST' ])
def create():
  global todos
  jsonobj = json.loads(request.data)
  id = len(todos) + 1
  newtodo = { 'id': id, 'title': jsonobj['title'], 'done': False }
  todos.append(newtodo)
  response = jsonify(newtodo)
  response.status_code = 201
  return response

@app.route('/todos/<int:id>', methods = [ 'GET' ])
def getTodo(id):
  filterd = list(filter(lambda item: item['id'] == id, todos))
  if len(filterd) == 0:
    response = jsonify({})
    response.status_code = 404
    return response
  else:
    return filterd[0]

@app.route('/todos/<int:id>', methods = [ 'DELETE' ])
def deleteTodo(id):
  global todos
  filterd = list(filter(lambda item: item['id'] == id, todos))
  if len(filterd) == 0:
    response = jsonify({})
    response.status_code = 404
    return response
  else:
    todos.remove(filterd[0])
    response = jsonify({})
    response.status_code = 204
    return response
