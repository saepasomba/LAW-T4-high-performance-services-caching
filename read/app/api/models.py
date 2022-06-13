from pydantic import BaseModel

class Student(BaseModel):
    npm: int
    nama: str