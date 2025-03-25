from dataclasses import dataclass
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Bilong(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    first_name  : str = Field(index= True)
    email       : str = Field(index= True)
    phone_number: str = Field(index= True)
    city        : str = Field(index= True)
    birthday    : str = Field(index= True)
    bio         : str = Field(index= True)
    job         : str = Field(index= True)

# @dataclass
# class Bilong:
#     id          : int
#     name        : str
#     first_name  : str
#     email       : str
#     phone_number: str
#     city        : str
#     birthday    : str
#     bio         : str
#     job         : str