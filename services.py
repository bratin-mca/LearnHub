#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:40:54 2025

@author: bratinjana
"""

# services.py
from typing import List
from models import Task, TaskUpdate
from database import Database

class TaskService:
    def __init__(self, db: Database):
        self.db = db
    
    def create_task(self, task: Task) -> Task:
        self.db.cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task.title, task.description, task.completed),
        )
        self.db.conn.commit()
        task_id = self.db.cursor.lastrowid
        return {**task.dict(), "id": task_id}
    
    def read_tasks(self) -> List[Task]:
        self.db.cursor.execute("SELECT * FROM tasks")
        tasks = self.db.cursor.fetchall()
        return tasks
    
    def read_task(self, task_id: int) -> Task:
        self.db.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = self.db.cursor.fetchone()
        if not task:
            return {"error": "Task not found"}
        return task
    
    def update_task(self, task_id: int, task: TaskUpdate):
        self.db.cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
        (task.title, task.description, task.completed, task_id),
        )
        self.db.conn.commit()
        self.db.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        updated_task = self.db.cursor.fetchone()
        return updated_task
    
    def delete_task(self, task_id: int):
        self.db.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.db.conn.commit()
        return {"message": "Task deleted successfully"}