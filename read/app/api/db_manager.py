from app.api.models import Student
from app.api.db import students, database


async def get_student(npm):
    query = students.select(students.c.npm==npm)
    return await database.fetch_one(query=query)