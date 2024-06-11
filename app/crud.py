from typing import List, Dict
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


def get_element(db: Session, element_id: int) -> schemas.Element:
    db_element = db.query(models.Element).filter(models.Element.id == element_id).first()
    if db_element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Element not found")
    return schemas.Element.from_orm(db_element)


def get_elements(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.Element]:
    db_elements = db.query(models.Element).order_by(models.Element.id.asc()).offset(skip).limit(limit).all()
    return [schemas.Element.from_orm(element) for element in db_elements]


def update_element(db: Session, element_id: int, element: schemas.ElementUpdate) -> schemas.Element:
    db_element = db.query(models.Element).filter(models.Element.id == element_id).first()
    if db_element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Element not found")
    for field, value in element.dict().items():
        setattr(db_element, field, value)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not update element: {e}",
        )
    db.refresh(db_element)
    return schemas.Element.from_orm(db_element)


def delete_element(db: Session, element_id: int) -> Dict[str, str]:
    db_element = db.query(models.Element).filter(models.Element.id == element_id).first()
    if db_element is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Element not found")
    db.delete(db_element)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Could not delete element: {e}",
        )
    return {"message": "Element deleted successfully"}
