

from config.config import app , db
from flask import request, make_response,jsonify
from schema.todoschema import TodoSchema
from model.todomodel import Todo


@app.route('/api/v1/todo', methods=['POST'])
def create_todo():
   data = request.get_json()
   todo_schema = TodoSchema()
   todo = todo_schema.load(data)
   result = todo_schema.dump(todo.create())
   return make_response(jsonify({"todo": result}), 200)


@app.route('/api/v1/todo', methods=['GET'])
def index():
   get_todos = Todo.query.all()
   todo_schema = TodoSchema(many=True)
   todos = todo_schema.dump(get_todos)
   return make_response(jsonify({"todos": todos}))

@app.route('/api/v1/todo/<id>', methods=['GET'])
def get_todo_by_id(id):
   get_todo = Todo.query.get(id)
   todo_schema = TodoSchema()
   todo = todo_schema.dump(get_todo)
   return make_response(jsonify({"todo": todo}))

@app.route('/api/v1/todo/<id>', methods=['PUT'])
def update_todo_by_id(id):
   data = request.get_json()
   get_todo = Todo.query.get(id)
   if data.get('title'):
       get_todo.title = data['title']
   if data.get('todo_description'):
       get_todo.todo_description = data['todo_description']
   db.session.add(get_todo)
   db.session.commit()
   todo_schema = TodoSchema(only=['id', 'title', 'todo_description'])
   todo = todo_schema.dump(get_todo)

   return make_response(jsonify({"todo": todo}))