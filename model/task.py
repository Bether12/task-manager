from datetime import datetime

class Task:
    def __init__(self, name : str, priority: int, type: str = "todo",
                 date_created =datetime.now().strftime("%d/%m/%Y %H:%M"),
                 date_updated = datetime.now().strftime("%d/%m/%Y %H:%M")):
        self.name = name
        self.type = type
        self.priority = priority
        self.date_created = date_created
        self.date_updated = date_updated

    @classmethod
    def from_dict(cls, data):
        task = cls(data["name"], data["priority"])
        task.type = data.get("type", "")
        task.date_created = data.get("date_created", "")
        task.date_updated = data.get("date_updated", "")
        return task

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "priority": self.priority,
            "date_created": self.date_created,
            "date_updated": self.date_updated
        }