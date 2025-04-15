from flask import Blueprint, request
from tasks.task_service import TaskService
from utils.json_msg import json_msg

task_bp = Blueprint("task", __name__, url_prefix="/api/tasks")

@task_bp.route("/add", methods=["POST"])
def create_task():
    try:
        data=request.get_json()
        TaskService.add_task(data)
        return json_msg("Dodano nowy task", "success", 201)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))


@task_bp.route("/remove", methods=["DELETE"])
def delete_task():
    try:
        data=request.get_json()
        TaskService.delete_task(data["nazwa"])
        return json_msg("Usunieto task", "success", 200)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))
    

@task_bp.route("/all", methods=["GET"])
def get_all_tasks():
    try:
        tasks = TaskService.get_all_tasks()
        return json_msg("Lista tasków", "success", 200, data=tasks)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))