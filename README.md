# FastAPI CRUD Operations

Welcome to the FastAPI CRUD Operations project! This application lets you create, read, update, and delete (CRUD) elements using FastAPI, SQLAlchemy, and Pydantic, with PostgreSQL as the database.

<p align="center">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.8+-ffd343.svg" alt="Python">
    </a>
    <a href="https://fastapi.tiangolo.com/">
        <img src="https://img.shields.io/badge/FastAPI-0.95.1-05998a.svg" alt="FastAPI">
    </a>
    <a href="https://www.postgresql.org/">
        <img src="https://img.shields.io/badge/PostgreSQL-16-336791.svg" alt="PostgreSQL">
    </a>
    <a href="https://docs.sqlalchemy.org/">
        <img src="https://img.shields.io/badge/ORM-SQLAlchemy-003b63.svg" alt="ORM">
    </a>
    <a href="https://swagger.io/">
        <img src="https://img.shields.io/badge/Swagger-UI-6db33f.svg" alt="Swagger">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="MIT License">
    </a>
</p>

This FastAPI application provides a streamlined CRUD (Create, Read, Update, Delete) API for managing elements. It utilizes FastAPI's automatic documentation generation and high-performance capabilities. Pydantic ensures robust data validation, ensuring that both incoming and outgoing data adhere to defined schemas. SQLAlchemy facilitates seamless interaction with the PostgreSQL relational database, abstracting complex SQL queries and transactions. This project serves as a great starting point for developing more sophisticated and resilient APIs using FastAPI's efficient and developer-friendly features.

## 🌟 **Introduction**

This project showcases how to build a robust API with FastAPI, a high-performance web framework for Python. Here’s a quick overview:

- **FastAPI**: A modern web framework for building APIs with Python, known for its speed and ease of use.
- **CRUD Operations**: Fundamental actions to manage data—Create, Read, Update, and Delete.
- **ORM**: SQLAlchemy as the Object Relational Mapper (ORM) abstracts database interactions using Python classes.

## 🚀 **Getting Started**

### **1. Setup Your Environment**

#### Install Dependencies

Make sure you have Python installed. Then, install the necessary packages:

```
pip install fastapi sqlalchemy uvicorn pydantic psycopg2
```

#### Create a Virtual Environment

To keep your project dependencies isolated, create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate` 
```

### **2. Project Structure**

Here’s how the project is organized:

```
netclues-fastapi-crud-operations/ 
├── app/ 
│   ├── __init__.py       # Marks app as a package 
│   ├── database.py       # Database connection settings 
│   ├── models.py         # SQLAlchemy data models 
│   ├── schemas.py        # Data validation with Pydantic 
│   ├── crud.py           # CRUD operations 
│   └── main.py           # FastAPI application setup 
├── requirements.txt      # Dependencies list 
└── README.md             # This guide
```

### **3. Understanding the Files**

- `app/__init__.py`: An empty file making `app` a package.
- `app/database.py`: Sets up the connection to the PostgreSQL database using SQLAlchemy.
- `app/models.py`: Defines the data models representing the database tables.
- `app/schemas.py`: Manages data validation and structure using Pydantic.
- `app/crud.py`: Contains the CRUD operations logic.
- `app/main.py`: Entry point for the FastAPI application, defining the routes and configurations.
- `requirements.txt`: Lists all dependencies required for the project.

## 🛠️ **Implementing CRUD Operations**

### **Database Connection** (`app/database.py`)

Connect to the database using SQLAlchemy:

python

```
from sqlalchemy import create_engine, orm 
from sqlalchemy.orm import declarative_base, sessionmaker  

DATABASE_URL = "postgresql+psycopg2://user:password@host:port/database_name" # Replace with your database connection deatils

engine = create_engine(DATABASE_URL) 

Base = declarative_base() 
sessionLocal = sessionmaker(bind=engine)
```

### **Data Models** (`app/models.py`)

Define the structure of your data:

python

```
from datetime import datetime 
from sqlalchemy import Column, Integer, String, DateTime 
from database import Base  

class Element(Base):     
    __tablename__ = "elements"      
    id = Column(Integer, primary_key=True, index=True)     
    title = Column(String)     
    description = Column(String)     
    created_date = Column(DateTime, default=datetime.now, nullable=False)     
    updated_date = Column(DateTime, onupdate=datetime.now, nullable=True)
```

### **Schemas** (`app/schemas.py`)

Validate and structure data:

python

```
from datetime import datetime 
from typing import Optional 
from pydantic import BaseModel  

class ElementBase(BaseModel):     
    title: str     
    description: Optional[str] = None  

class ElementCreate(ElementBase):     
    pass

class ElementUpdate(ElementBase):     
    pass  

class Element(ElementBase):     
    id: int     
    created_date: datetime     
    updated_date: Optional[datetime]      
    
    class Config:         
        from_attributes = True
```

### **CRUD Operations** (`app/crud.py`)

Implement the CRUD logic:

python

```
from sqlalchemy.orm import Session 
from fastapi import HTTPException, status 
import models 
import schemas  

def create_element(db: Session, element: schemas.ElementCreate) -> schemas.Element:     
    db_element = models.Element(**element.dict())     
    db.add(db_element)     
    try:         
        db.commit()     
    except Exception as e:         
        db.rollback()         
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not create element: {e}",         
        )
    db.refresh(db_element)     
    return schemas.Element.from_orm(db_element)  
    
# Similar functions for read, update, delete go here
```

### **FastAPI Application** (`app/main.py`)

Define the API routes:

python

```
from fastapi import FastAPI 
import crud 
import schemas 
from database import sessionLocal  

app = FastAPI() 
db = sessionLocal()  

@app.post("/elements/", response_model=schemas.Element) 
async def create_element(element: schemas.ElementCreate):     
    return crud.create_element(db=db, element=element)  

# Add more CRUD routes for read, update, delete
```

## 📦 **Quick Start**

### **Install the Dependencies**

```
pip install -r requirements.txt  # For Windows 
pip3 install -r requirements.txt # For Linux
```

### **Run the Project**

Navigate to the `app` directory and start the FastAPI server:

```
cd app 
uvicorn main:app --reload
```

### **Access the API**

- **Base URL**: [http://localhost:8000](http://localhost:8000)
- **Swagger UI**: http://localhost:8000/docs

## 👩‍💻 **Contributing**

Feel free to fork this repository and make improvements. Contributions are welcome!

## 📄 **License**

This project is licensed under the MIT License.
