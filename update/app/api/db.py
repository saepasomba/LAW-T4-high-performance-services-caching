from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

from databases import Database

import os

# DATABASE_URL = 'postgresql://saepasomba:123@localhost:5432/student_db'
DATABASE_URI = os.getenv('DATABASE_URI')


engine = create_engine(DATABASE_URI)
metadata = MetaData()

students = Table(
    'students',
    metadata,
    Column('npm', Integer, primary_key=True),
    Column('nama', String(50)),
)

database = Database(DATABASE_URL)