from fastapi import FastAPI, HTTPException, Depends, Query

from myapi.models import Bilong
from typing import Annotated, Union
import json
from sqlmodel import Session, SQLModel, create_engine, select


#db
sqlite_file_name = "bilongs.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
    
Session_Dep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/bilongs/{first_name}")
def get_bilong_by_id(first_name: str, session: Session_Dep) -> Bilong:
    bilong = session.get(Bilong, first_name)
    print(bilong)
    if not bilong:
        raise HTTPException(status_code=404, detail="bilong not found")
    return bilong
        
@app.get("/bilongs")
def get_list_of_bilongs(session: Session_Dep, offset: int = 0,limit: Annotated[int, Query(le=100)] = 50)-> list[Bilong]:
    """
    This function returns a list of bilongs.
    """
    bilongs = session.exec(select(Bilong).offset(offset).limit(limit)).all()
    return bilongs


@app.post("/bilongs")
def create_bilong(bilong: Bilong, session: Session_Dep) -> Bilong:
    """
    This function creates a bilong.
    """
    
    session.add(bilong)
    session.commit()
    session.refresh(bilong)
    return bilong
