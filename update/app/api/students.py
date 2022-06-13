from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel

from .models import Student

from app.api import db_manager

students = APIRouter()

@students.post('/update')
async def add_student(payload: Student):
    students = await db_manager.get_all_student()
    for student in students:
        if student.npm == payload.npm:
            raise HTTPException(status_code=404, detail="Mahasiswa dengan NPM yang dimaksud sudah ada")
    await db_manager.add_student(payload)
    return {"status": "OK"}
