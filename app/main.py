from typing import List
from fastapi import FastAPI
import crud
import schemas
from database import sessionLocal

app = FastAPI()

db = sessionLocal()


# Create an Element
@app.post("/elements/", response_model=schemas.Element)
async def create_element(element: schemas.ElementCreate):
    return crud.create_element(db=db, element=element)


# Read all Elements
@app.get("/elements/", response_model=List[schemas.Element])
def read_elements(skip: int = 0, limit: int = 100):
    return crud.get_elements(db=db, skip=skip, limit=limit)


# Read an Element by ID
@app.get("/elements/{element_id}", response_model=schemas.Element)
async def read_element(element_id: int):
    return crud.get_element(db=db, element_id=element_id)


# Update an Element by ID
@app.put("/elements/{element_id}", response_model=schemas.Element)
async def update_element(element_id: int, element: schemas.ElementUpdate):
    return crud.update_element(db=db, element_id=element_id, element=element)


# Delete an Element by ID
@app.delete("/elements/{element_id}")
async def delete_element(element_id: int):
    crud.delete_element(db=db, element_id=element_id)
    return {"message": "Element deleted successfully"}
