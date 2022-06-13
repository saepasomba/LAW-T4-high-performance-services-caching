from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel

from .models import Student

from app.api import db_manager

students = APIRouter()

@students.get('/read/{npm}')
async def get_student(npm: int):
    student = await db_manager.get_student(npm)
    if not student:
        raise HTTPException(status_code=404, detail="Mahasiswa dengan NPM yang dimaksud tidak tersedia")
    else:
        return {
            "status": "OK",
            "npm": student.npm,
            "nama": student.nama
        }
