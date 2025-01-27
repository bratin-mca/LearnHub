#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:42:38 2025

@author: bratinjana
"""

# controllers.py
from typing import List
from fastapi import APIRouter, Depends
from models import Task, TaskUpdate
from services import TaskService
import os

router = APIRouter()

def get_task_service() -> TaskService:
    from database import Database
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    DATABASE_PATH = os.path.join(BASE_DIR, '../TestDB.db')
    db = Database(DATABASE_PATH)
    return TaskService(db)

@router.post("/tasks/", response_model=Task)
def create_task(task: Task, service: TaskService = Depends(get_task_service)):
    #service: TaskService = get_task_service()
    return service.create_task(task)

@router.get("/tasks/", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    #service: TaskService = get_task_service()
    return service.read_tasks()

@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, service: TaskService = Depends(get_task_service)):
    #service: TaskService = get_task_service()
    return service.read_task(task_id)

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, service: TaskService = Depends(get_task_service)):
    #service: TaskService = get_task_service()
    return service.update_task(task_id, task)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    #service: TaskService = get_task_service()
    return service.delete_task(task_id)
