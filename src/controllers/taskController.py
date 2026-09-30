from fastapi import APIRouter, HTTPException
from src.services.taskService import TaskCreate, TaskService

router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])

@router.get("/")
def get_tasks():
    return TaskService.get_all_tasks()

@router.post("/")
def create_task(task: TaskCreate):
    return TaskService.create_task(task)