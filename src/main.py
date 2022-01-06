from src.app import create_web_app

app = None

if not app:
    app = create_web_app()


# if __name__ == '__main__':
#     uvicorn.run("main.app:app", port=8001, host="127.0.0.1", reload=True)


#
# from fastapi import FastAPI, Depends
# from pydantic import BaseModel
# from typing import List
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker, Session
# from sqlalchemy import Boolean, Column, Float, String, Integer
#
# from src.extensions.database import Base, engine, SessionLocal
#
# app = FastAPI()
#
# # # SqlAlchemy Setup
# # SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./db.sqlite3:"
# # engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # Base = declarative_base()
#
# Base.metadata.create_all(bind=engine)
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# # A SQLAlchemny ORM Address
# class Address(Base):
#     __tablename__ = "addresses"
#
#     id = Column(Integer, primary_key=True)
#     latitude = Column(Float, nullable=False)
#     longitude = Column(Float, nullable=False)
#     primary = Column(Boolean, default=False)
#     pin_code = Column(Integer, nullable=True)
#
#
# # A Pydantic Address
# class AddressBase(BaseModel):
#     latitude: float
#     longitude: float
#     primary: bool
#     pin_code: int
#
#     class Config:
#         orm_mode = True
#
#
# def get_address(db: Session, address_id: int):
#     return db.query(Address).where(Address.id == address_id).first()
#
#
# def get_all_address(db: Session):
#     return db.query(Address).all()
#
#
# def create_address(db: Session, address: AddressBase):
#     db_address = Address(**address.dict())
#     db.add(db_address)
#     db.commit()
#     db.refresh(db_address)
#
#     return db_address
#
#
# # Routes for interacting with the API
# @app.post("/address/", response_model=AddressBase)
# def create_address_view(address: AddressBase, db: Session = Depends(get_db)):
#     db_address = create_address(db, address)
#     return db_address
#
#
# @app.get("/address/", response_model=List[AddressBase])
# def get_address_view(db: Session = Depends(get_db)):
#     return get_all_address(db)
#
#
# @app.get("/address/{address_id}")
# def get_address_view(address_id: int, db: Session = Depends(get_db)):
#     return get_address(db, address_id)
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World!"}
#

# uvicorn.run("main:app", reload=True)
