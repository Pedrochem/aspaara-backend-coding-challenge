from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



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
    start_date = Column(DateTime(), nullable=False)
    end_date = Column(DateTime(), nullable=False)
    client_name = Column(String(255))
    client_id = Column(String(255), nullable=False)
    industry = Column(String(255))
    # todo:
    # required_skills = 
    # optional_skills = 
    is_unassigned = Column(Boolean())


    def __init__(self, record):
        self.id = record['id']
        self.original_id = record['original_id']
        self.talent_id = record['talent_id']
        self.talent_name = record['talent_name']
        self.talent_grade = record['talent_grade']
        self.booking_grade = record['booking_grade']
        self.operating_unit = record['operating_unit']
        self.office_city = record['office_city']
        self.office_postal_code = record['office_postal_code']
        self.job_manager_name = record['job_manager_name']
        self.job_manager_id = record['job_manager_id']
        self.total_hours = record['total_hours']
        self.start_date = record['start_date']
        self.end_date = record['end_date']
        self.client_name = record['client_name']
        self.client_id = record['client_id']
        self.industry = record['industry']
        # self.required_skills = record['required_skills']
        # self.optinal_skills = record['optinal_skills']
        self.is_unassigned = record['is_unassigned']
        