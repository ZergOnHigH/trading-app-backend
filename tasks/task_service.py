from tasks.task_model import TaskModel
from extensions import mongodb

class TaskService:
    @staticmethod
    def get_repo():
        return mongodb.get_collection("task")

    @staticmethod
    def add_task(data):
        repo = TaskService.get_repo() #definiuje repo i z kąd je wziąść

        if repo.find_one({"nazwa": data["nazwa"]}): #sprawdza czy już istnieje
            raise Exception("Taka nazwa juz istnieje")

        model = TaskModel().load(data) #sprawdza czy dane pasują do modelu
        repo.insert_one(model) # zapisuje do bazy

    @staticmethod
    def delete_task(nazwa):
        repo = TaskService.get_repo()
        result = repo.delete_one({"nazwa": nazwa})

        if result.deleted_count == 0:
            raise Exception("Nie znaleziono taska o danej nazwie")
        

    @staticmethod
    def get_all_tasks():
        repo = TaskService.get_repo()
        tasks = repo.find()
        result = []

        for task in tasks:
            task["_id"] = str(task["_id"])
            result.append(task)

        return result