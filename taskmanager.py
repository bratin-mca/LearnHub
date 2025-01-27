#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:46:49 2025

@author: bratinjana
"""

# taskmanager.py
from fastapi import FastAPI
from controllers import router

app = FastAPI()
app.include_router(router)

if __name__ == "__taskmanager__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)