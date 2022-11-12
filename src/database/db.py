import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Talent, Base


engine = create_engine('sqlite:///planning.bd',echo=True)


Talent.__table__.drop(engine,checkfirst=True)
Base.metadata.create_all(engine)

