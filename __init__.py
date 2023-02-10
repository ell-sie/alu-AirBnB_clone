#!/usr/bin/python3
"""init file to connect storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
