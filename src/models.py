import json
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sqlalchemy.sql import func
from pydantic import BaseModel

Base = declarative_base()

class Talent_Response(BaseModel):
    id : int
    original_id : str
    talent_id : str
    talent_name : str
    talent_grade : str
    booking_grade : str
    operating_unit : str
    office_city : str
    office_postal_code : str
    job_manager_name : str
    job_manager_id : str
    total_hours : float
    start_date : datetime
    end_date : datetime
    client_name : str
    client_id : str
    industry : str
    required_skills : object
    optional_skills : object
    is_unassigned : bool
    # items : int
    # total : int
    # page : int
    # size: int

    class Config:
        orm_mode = True


class Talent (Base):
    __tablename__ = 'talents'
    
    id = Column(Integer(), primary_key=True)
    original_id = Column(String(255), unique=True, nullable=False)
    talent_id = Column(String(255))
    talent_name = Column(String(255))
    talent_grade = Column(String(255))
    booking_grade = Column(String(255))
    operating_unit = Column(String(255), nullable=False)
    office_city = Column(String(255))
    office_postal_code = Column(String(255), nullable=False)
    job_manager_name = Column(String(255))
    job_manager_id = Column(String(255))
    total_hours = Column(Float(), nullable=False)
    start_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    end_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    client_name = Column(String(255))
    client_id = Column(String(255), nullable=False)
    industry = Column(String(255))
    required_skills = Column(JSON)
    optional_skills = Column(JSON)
    is_unassigned = Column(Boolean())


    def __init__(self, record):
        self.id = record['id']
        self.original_id = record['originalId']
        self.talent_id = record['talentId']
        self.talent_name = record['talentName']
        self.talent_grade = record['talentGrade']
        self.booking_grade = record['bookingGrade']
        self.operating_unit = record['operatingUnit']
        self.office_city = record['officeCity']
        self.office_postal_code = record['officePostalCode']
        self.job_manager_name = record['jobManagerName']
        self.job_manager_id = record['jobManagerId']
        self.total_hours = record['totalHours']
        self.start_date = datetime.strptime(record['startDate'], '%m/%d/%Y %I:%M %p')
        self.end_date = datetime.strptime(record['endDate'], '%m/%d/%Y %I:%M %p')
        self.client_name = record['clientName']
        self.client_id = record['clientId']
        self.industry = record['industry']
        self.required_skills = record['requiredSkills']
        self.optional_skills = record['optionalSkills']
        self.is_unassigned = record['isUnassigned']
        