import ijson
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Talent
from sqlalchemy import create_engine

DATA_FILE_PATH = os.path.join( os.getcwd(),'..', '..','planning.json' )

engine = create_engine('sqlite:///planning.bd',echo=True)

Talent.__table__.drop(engine,checkfirst=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def load_data():
    with open(DATA_FILE_PATH, 'r') as f:
        for record in ijson.items(f,'item'):
            talent = Talent(record)
            session.add(talent)

load_data()
session.commit()
session.close()
