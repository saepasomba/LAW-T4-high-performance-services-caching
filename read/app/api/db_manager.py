from app.api.models import Student
from app.api.db import students, database


async def get_students(npm):
    query = students.select(movies.c.npm==npm)
    return await database.fetch_one(query=query)