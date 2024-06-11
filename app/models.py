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
