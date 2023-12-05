# server.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd


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

# Set up a connection to the database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# FastAPI route to load data from CSV into the database

@app.get("/load-data")
def load_data():
    try:
        # Load data from CSV
        csv_path = "data.csv"
        df = pd.read_csv(csv_path)

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
        for _, row in df.iterrows():
            item = Item(**row.to_dict())
            db.add(item)

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
@app.get("/items")
def read_data():
    # Fetch data from the database using SQLAlchemy
    db = SessionLocal()
    data = db.query(Item).all()
    db.close()

    # Convert data to JSON
    response_data = [{"id": item.id, "name": item.name, "date_of_event": item.date_of_event,
                     "age": item.age, "citizenship": item.citizenship, "event_location": item.event_location,
                     "event_location_district": item.event_location_district, "event_location_region": item.event_location_region,
                     "date_of_death": item.date_of_death, "gender": item.gender,
                     "took_part_in_the_hostilities": item.took_part_in_the_hostilities,
                     "place_of_residence": item.place_of_residence, "place_of_residence_district": item.place_of_residence_district,
                     "type_of_injury": item.type_of_injury, "ammunition": item.ammunition,
                     "killed_by": item.killed_by, "notes": item.notes} for item in data]

    return JSONResponse(content=response_data)
