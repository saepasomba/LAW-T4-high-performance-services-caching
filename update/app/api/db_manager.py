from app.api.models import Student
from app.api.db import students, database


async def add_student(payload: Student):
    query = students.insert().values(**payload.dict())

    return await database.execute(query=query)

# async def get_all_movies():
#     query = movies.select()
#     return await database.fetch_all(query=query)

async def get_all_student():
    query = students.select()
    return await database.fetch_all(query=query)

# async def delete_movie(id: int):
#     query = movies.delete().where(movies.c.id==id)
#     return await database.execute(query=query)

# async def update_movie(id: int, payload: MovieIn):
#     query = (
#         movies
#         .update()
#         .where(movies.c.id == id)
#         .values(**payload.dict())
#     )
#     return await database.execute(query=query)