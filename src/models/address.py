from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy.orm import validates

from src.extensions.database import Base


class Address(Base):
    __tablename__ = "addresses"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    primary = Column(Boolean, default=False)
    pin_code = Column(Integer, nullable=True)
