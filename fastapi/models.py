# models.py
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date_of_event = Column(DateTime)
    age = Column(Integer)
    citizenship = Column(String)
    event_location = Column(String)
    event_location_district = Column(String)
    event_location_region = Column(String)
    date_of_death = Column(DateTime)
    gender = Column(String)
    took_part_in_the_hostilities = Column(Boolean)
    place_of_residence = Column(String)
    place_of_residence_district = Column(String)
    type_of_injury = Column(String)
    ammunition = Column(String)
    killed_by = Column(String)
    notes = Column(Text)
