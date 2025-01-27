#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:23:42 2025

@author: bratinjana
"""

# models.py
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
