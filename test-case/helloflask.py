from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
import sys
sys.path.append('..')
from log import Logger
Log = Logger.getLogger(__name__)

import json

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

resource_fields = {
    'code': fields.Integer(default=500),
    'message': fields.String,
    'data': fields.Url('todolist')
}


def abort_if_todo_doesnt_exist(todo_id):
    if not isinstance(todo_id, int):
        Log.error(isinstance(todo_id, int))
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=int)


class TodoList(Resource):

    def post(self):
        args = parser.parse_args()
        abort_if_todo_doesnt_exist(args.task)
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

api.add_resource(TodoList, '/todos', endpoint='todolist')


if __name__ == '__main__':
    app.run(debug=True,port=5001)
