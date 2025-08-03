import tempfile
import os
from fastapi import UploadFile

def save_temp_file(file: UploadFile) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.file.read())
        return tmp.name

def delete_file(path: str):
    if os.path.exists(path):
        os.remove(path)
