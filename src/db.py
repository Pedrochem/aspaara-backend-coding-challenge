import ijson
import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base,Talent
from sqlalchemy import create_engine

DATA_FILE_PATH = os.path.join( os.getcwd(),'..','planning.json' )

# recreates talent table
def create_db(load_data):
    engine = create_engine('sqlite:///planning.bd',echo=True)

    Talent.__table__.drop(engine,checkfirst=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    if load_data:
        # populate database via json file 
        with open(DATA_FILE_PATH, 'r') as f:
            for record in ijson.items(f,'item'):
                talent = Talent(record)
                session.add(talent)

    session.commit()
    session.close()