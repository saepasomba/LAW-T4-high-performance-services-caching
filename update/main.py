from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.api.models import Student
from app.api.students import students
from app.api.db import metadata, database, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(students)