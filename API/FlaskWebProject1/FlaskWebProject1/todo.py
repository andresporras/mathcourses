
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from FlaskWebProject1 import app
from pymongo import MongoClient
from functools import wraps
from jwt import encode, decode

client = MongoClient('localhost', 27017)

db = client['demo']

collection = db['first']

c=collection.find_one()

api=Api(app)


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['x-access-token']
        if not token:
            return 'token is missing', 401
        try:
            data = decode(token, app.config['SECRET_KEY']), 403
            current_user='oscar'
        except:
            return 'token is invalid'
        return f(current_user, *args, **kwargs)
    return decorated

class Todo(Resource):
    @token_required
    def get(current_user, self, todo_id, todo_id2=None):
        if todo_id=="case2":
            abort_if_todo_doesnt_exist(todo_id2)
            return TODOS[todo_id2]
        return '''return default answer {}'''.format(c)

    def delete(self, todo_id, todo_id2):
        abort_if_todo_doesnt_exist(todo_id2)
        del TODOS[todo_id2]
        return '', 204

    def put(self, todo_id,todo_id2):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id2] = task
        return task, 201


api.add_resource(Todo, '/todos/<todo_id>', '/todos/<todo_id>/<todo_id2>')

if __name__ == '__main__':
    app.run(debug=True)