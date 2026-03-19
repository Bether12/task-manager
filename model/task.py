from datetime import datetime

class Task:
    def __init__(self, name : str, priority: int):
        self.name = name
        self.type = "todo"
        self.priority = priority
        self.date_created = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.date_updated = datetime.now().strftime("%d/%m/%Y %H:%M")
