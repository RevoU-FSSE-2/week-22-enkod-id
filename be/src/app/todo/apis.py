from flask import Blueprint, request
from marshmallow import Schema, fields
from app.di import injector
from core.todo.services import TodoService  # replace with your actual TodoService import

todo_service = injector.get(TodoService)

todo_blueprint = Blueprint('todo_blueprint', __name__)

class TodoSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    priority = fields.String(required=True)
    dueDate = fields.String(required=True)

@todo_blueprint.route("/todo", methods=["POST"])
def add_todo():
    todo_schema = TodoSchema()
    errors = todo_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400

    data = todo_schema.load(request.get_json())

    todo = todo_service.create_todo(
        title=data["title"],
        description=data["description"],
        priority=data["priority"],
        dueDate=data["dueDate"]
    )

    return todo_schema.dump(todo)

@todo_blueprint.route("/todo", methods=["GET"])
def get_todo():
    all_todos = todo_service.get_todo_list()
    return all_todos

@todo_blueprint.route("/todo/<id>", methods=["GET"])
def todo_detail(id):
    todo = todo_service.get_todo(id)
    return todo

@todo_blueprint.route("/todo/<id>", methods=["PUT"])
def todo_update(id):
    todo_schema = TodoSchema()
    errors = todo_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400

    data = todo_schema.load(request.get_json())

    todo = todo_service.update_todo(
        id=id,
        title=data["title"],
        description=data["description"],
        priority=data["priority"],
        dueDate=data["dueDate"]
    )

    return todo_schema.dump(todo)

@todo_blueprint.route("/todo/<id>", methods=["DELETE"])
def todo_delete(id):
    todo_service.delete_todo(id)
    return {"message": "Todo deleted"}