from fastapi import FastAPI, HTTPException
from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_pagination import Page, Params, paginate, add_pagination
from fastapi import Depends, FastAPI
from models import Talent,Talent_Response

engine = create_engine('sqlite:///planning.bd',echo=True)
Session = sessionmaker(bind=engine)
session = Session()

         
tags_metadata = [
    {
        "name": "pagination",
        "description": "Get all talents with pagination",
    },
    {
        "name": "sorted",
        "description": "Get all talents with pagination and sorting. Define 'asc' or 'desc' for either the startDate or endDate pathparamenters",
    },
    {
        "name": "filtered",
        "description": "Get all talents with pagination and filtering."
    }
]
app = FastAPI(openapi_tags=tags_metadata)


# retrieve all talents with pagination
@app.get("/talents/", response_model=Page[Talent_Response], tags=["pagination"])
def pagination(params: Params = Depends()):
    results = session.query(Talent).all()
    return paginate(results,params)
     

# retrieve talents sorted by startDate or endDate
@app.get("/talents/sorted", response_model=Page[Talent_Response], tags=["sorted"])
def sorting(params: Params = Depends(), startDate: Union[str, None] = None, endDate: Union[str, None] = None):
    if (startDate and endDate )or (not startDate and not endDate):
        raise HTTPException(status_code=400, detail="Provide either startDate or endDate")

    if startDate:
        if startDate == 'asc':
            results = session.query(Talent).order_by(Talent.start_date.asc()).all()
        elif startDate == 'desc':
            results = session.query(Talent).order_by(Talent.start_date.desc()).all()
    elif endDate:
        if endDate == 'asc':
            results = session.query(Talent).order_by(Talent.end_date.asc()).all()
        elif endDate == 'desc':
            results = session.query(Talent).order_by(Talent.end_date.desc()).all()
    
    return paginate(results,params)

# retrieve talents with filtering
@app.get("/talents/filtered",response_model=Page[Talent_Response], tags=["filtered"])
def filtering(params: Params = Depends(),
                original_id: Union[str,None] = None,
                talent_id : Union[str,None] = None,
                talent_name : Union[str,None] = None,
                talent_grade: Union[str,None] = None, 
                booking_grade : Union[str,None] = None, 
                operating_unit : Union[str,None] = None, 
                office_city : Union[str,None] = None, 
                office_postal_code : Union[str,None] = None, 
                job_manager_name : Union[str,None] = None, 
                job_manager_id : Union[str,None] = None, 
                total_hours : Union[str,float] = None,
                client_name: Union[str,None] = None,
                client_id : Union[str,None] = None,
                industry : Union[str,None] = None,
                is_unassigned: Union[bool,None] = None):

    parameters = locals().copy()
    query = session.query(Talent)
    # iterate over parameters not null add them to the query
    for attr in [x for x in parameters if parameters[x] is not None]:
        if attr == 'params': continue
        query = query.filter(getattr(Talent, attr) == (parameters[attr]))
    
    return paginate(query.all(),params)

