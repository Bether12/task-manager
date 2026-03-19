from model import task
import os
import json

class Data:
    def __init__(self):
        self.task_list : list[task.Task] = self.load_data()

    def load_data(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                return [task.Task.from_dict(item) for item in data]
        return []
    
    def save_data(self):
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump([task.to_dict() for task in self.task_list], file, ensure_ascii=False, indent=4)
    
    def add_task(self, name: str, priority: int):
        self.task_list.append(task.Task(name, priority))

    def delete_task(self, index):
        self.task_list.pop(index)
        self.save_data()

    def mark_done(self, index):
        self.task_list[index].type = "done"
        self.save_data()
                