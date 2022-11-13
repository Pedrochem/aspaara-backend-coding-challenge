from fastapi import FastAPI
from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_pagination import Page, Params, paginate
from fastapi import Depends, FastAPI
from models import Talent

engine = create_engine('sqlite:///planning.bd',echo=True)
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()
         

@app.get("/")
def read_root():
    results = session.query(Talent).all()
    return {"all_talents": results}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



    