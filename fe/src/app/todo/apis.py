from flask import Blueprint, request
from marshmallow import Schema, fields
from app.di import injector
from core.todo.services import TodoService

todo_service = injector.get(TodoService)

todo_blueprint = Blueprint('todo_blueprint', __name__)

class TodoSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    priority = fields.String(required=True)
    due_date = fields.String(required=True)

@todo_blueprint.route("/", methods=["POST"])
def create_todo():
    todo_schema = TodoSchema()
    errors = todo_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400
    
    data = todo_schema.load(request.get_json())

    todo = todo_service.create_todo(
        title=data["title"],
        description=data["description"],
        priority=data["priority"],
        due_date=data["due_date"]
    )

    return todo_schema.dump(todo)

@todo_blueprint.route("", methods=["GET"])
def get_todo_list():
    todo_list = todo_service.get_todo_list()
    return todo_list

@todo_blueprint.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = todo_service.get_todo(todo_id)
    return todo

@todo_blueprint.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo_schema = TodoSchema()
    errors = todo_schema.validate(request.get_json())
    if errors:
        return {'errors': errors}, 400
    
    data = todo_schema.load(request.get_json())
    todo = todo_service.update_todo(todo_id, data)

    return todo_schema.dump(todo)

@todo_blueprint.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    result = todo_service.delete_todo(todo_id)
    return {'success': result}
