import json
import os
from src.protocol import Task

class FileSource:
    """
        Источник задач, загружающий их из JSON-файла.
    """
    def __init__(self, path=""):
        self.path = path
    def get_tasks(self) -> list[Task]:
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"Файл {self.path} не найден")
        with open(self.path, mode='r', encoding='utf-8') as f:
            try:
                tasks = json.load(f)
            except json.decoder.JSONDecodeError:
                return []
        return [Task(id=item["id"], payload=item["payload"]) for item in tasks]


class GeneratorSource:
    """
        Источник задач, генерирующий их программно.
    """
    def __init__(self, num_tasks: int = 5):
        self.num_tasks = num_tasks
    def get_tasks(self) -> list[Task]:
        return [Task(id=i, payload={"source":"generator", "num": i}) for i in range(1, self.num_tasks + 1)]

class APISource:
    """
        API-заглушка для получения задач.
    """
    def __init__(self, url: str = ""):
        self.url = url
    def get_tasks(self) -> list[Task]:
        return [Task(1, {"info": f"Task from API with {self.url}"})]
