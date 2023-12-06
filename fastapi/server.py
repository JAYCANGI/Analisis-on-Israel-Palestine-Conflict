# server.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

app = FastAPI()



# SQLAlchemy models
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
    took_part_in_the_hostilities = Column(String)
    place_of_residence = Column(String)
    place_of_residence_district = Column(String)
    type_of_injury = Column(String)
    ammunition = Column(String)
    killed_by = Column(String)
    notes = Column(Text)

    def __init__(self, **data):
        print(data)  # Add this line to print the data
        valid_data = {k: v for k, v in data.items() if k not in {'Unnamed: 16'}}
        super().__init__(**valid_data)

    

# Set up a connection to the database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


# FastAPI route to load data from CSV into the database
# FastAPI route to load data from CSV into the database
@app.get("/load-data")
def load_data():
    try:
        # Load data from CSV excluding any unnamed columns
        csv_path = "data.csv"
        df = pd.read_csv(csv_path, index_col=0)  # Assuming the index is in the first column
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Rename columns to match the Item model attributes
        df = df.rename(columns={
            "Name": "name",
            "Date of Event": "date_of_event",
            "Age": "age",
            "Citizenship": "citizenship",
            "Event Location": "event_location",
            "Event Location District": "event_location_district",
            "Event Location Region": "event_location_region",
            "Date of Death": "date_of_death",
            "Gender": "gender",
            "Took Part in the Hostilities": "took_part_in_the_hostilities",
            "Place of Residence": "place_of_residence",
            "Place of Residence District": "place_of_residence_district",
            "Type of Injury": "type_of_injury",
            "Ammunition": "ammunition",
            "Killed By": "killed_by",
            "Notes": "notes"
        })

        # Convert date columns to datetime objects
        date_columns = ["date_of_event", "date_of_death"]
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

        # Print CSV file information
        print("CSV file loaded successfully.")
        print(f"Columns: {df.columns}")
        print(f"Number of rows: {len(df)}")

        # Create tables in the database
        Base.metadata.create_all(bind=engine)
        print("Database tables created.")

        # Open a database session
        db = SessionLocal()

        # Insert data into the database
        for idx, row in df.iterrows():
            try:
                item = Item(**row.to_dict())
                db.add(item)
            except Exception as e:
                print(f"Error inserting data at index {idx}: {str(e)}")

        # Commit the changes
        db.commit()

        print("Data inserted into the database successfully.")

        # Close the database session
        db.close()

        return {"status": "Data loaded successfully!"}
        
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}


# FastAPI health check endpoint
@app.get("/health")
def health_check():
    try:
        # Check if the SQLite database is accessible
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        return {"status": "OK"}
    except Exception as e:
        return {"status": "Error", "error_message": str(e)}

# FastAPI route to serve the dataset
# FastAPI route to serve the dataset
@app.get("/items")
def read_data():
    # Fetch data from the database using SQLAlchemy
    db = SessionLocal()
    data = db.query(Item).all()
    db.close()

    # Convert data to JSON, converting datetime objects to strings
    response_data = [
        {
            "id": item.id,
            "name": item.name,
            "date_of_event": item.date_of_event.strftime("%Y-%m-%dT%H:%M:%S") if item.date_of_event else None,
            "age": item.age,
            "citizenship": item.citizenship,
            "event_location": item.event_location,
            "event_location_district": item.event_location_district,
            "event_location_region": item.event_location_region,
            "date_of_death": item.date_of_death.strftime("%Y-%m-%dT%H:%M:%S") if item.date_of_death else None,
            "gender": item.gender,
            "took_part_in_the_hostilities": item.took_part_in_the_hostilities,
            "place_of_residence": item.place_of_residence,
            "place_of_residence_district": item.place_of_residence_district,
            "type_of_injury": item.type_of_injury,
            "ammunition": item.ammunition,
            "killed_by": item.killed_by,
            "notes": item.notes,
        }
        for item in data
    ]

    return JSONResponse(content=response_data)

