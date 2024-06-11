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
