from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SqlAlchemy Setup

# sqlite url
SQLALCHEMY_DATABASE_URL = "sqlite+pysqlite:///./db.sqlite3:"

# engine to interact with sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# local session for transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base to define models
Base = declarative_base()

Base.metadata.create_all(bind=engine)


def get_db() -> SessionLocal:
    """
    It is used by every request and its closed after every request

    Returns: Instance of SessionLocal
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
