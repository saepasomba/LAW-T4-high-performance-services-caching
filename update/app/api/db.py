from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://admin:admin@localhost:5432/student_db'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

students = Table(
    'students',
    metadata,
    Column('npm', Integer, primary_key=True),
    Column('nama', String(50)),
)

database = Database(DATABASE_URL)