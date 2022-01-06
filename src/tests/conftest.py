import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app import create_web_app
from src.extensions.database import Base
from src.extensions.database import get_db


@pytest.fixture(scope="session", autouse=True)
def init_app():
    yield create_web_app()


@pytest.fixture(scope="session", autouse=True)
def init_db(init_app):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            for table in Base.metadata.sorted_tables:
                db.execute(table.delete())
            db.commit()
            db.close()

    init_app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def app(init_app):
    """
    Access Fast Apis test_client
    """
    return TestClient(init_app)
