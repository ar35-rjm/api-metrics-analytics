import time
import random
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "pending"


class TaskService:
    @staticmethod
    def get_all_tasks():
        time.sleep(random.uniform(0.1, 0.5))
        return [
            {"id": 1, "title": "Configure Arch Linux", "status": "completed"},
            {"id": 2, "title": "Create Dashboard PowerBi", "status": "in_progress"},
        ]

    @staticmethod
    def create_task(task_data: TaskCreate):
        time.sleep(random.uniform(0.1, 0.5))
        return {
            "id": random.randint(3, 100),
            "title": task_data.title,
            "description": task_data.description,
            "status": task_data.status,
        }