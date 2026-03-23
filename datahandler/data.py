from model import task
import os
import json
import csv

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
    
    def add_task(self, name: str, priority: int, status=None, date_created=None, date_updated=None):
        if status:
            if date_created:
                if date_updated:
                    self.task_list.append(task.Task(name, priority, type=status, date_created=date_created, date_updated=date_updated))
                    self.save_data()
                else:
                    self.task_list.append(task.Task(name, priority, type=status, date_created = date_created))
                    self.save_data()
            else:
                self.task_list.append(task.Task(name, priority, type=status))
                self.save_data()
        else:
            self.task_list.append(task.Task(name, priority))
            self.save_data()

    def delete_task(self, index):
        self.task_list.pop(index)
        self.save_data()

    def mark_done(self, index):
        self.task_list[index].type = "done"
        self.save_data()

    def import_csv(self, file):
        if not file:
            return
        
        try:
            with open(file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for task in reader:
                    print(task)
                    priority = int(task[0])
                    name = task[1]
                    date_created = task[2]
                    date_updated = task[3]
                    status = task[4]
                    self.add_task(name, priority, status=status, date_created=date_created, date_updated=date_updated)

            return 0
        
        except Exception as e:
            return e

    def export_csv(self, file):
        if not file:
            return

        try:
            with open(file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                writer.writerow(["Priority", "Task Name", "Date Created", "Date Updated", "Status"])

                for task in self.task_list:
                    writer.writerow([task.priority, task.name, task.date_created, task.date_updated, task.type])
            return 0

        except Exception as e:
            return e
                