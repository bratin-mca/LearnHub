#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:38:13 2025

@author: bratinjana
"""

# database.py
import sqlite3

class Database:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

def create_tables(self):
    self.cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL DEFAULT FALSE
        )
        """
    )
    self.conn.commit()

def close(self):
    self.conn.close()