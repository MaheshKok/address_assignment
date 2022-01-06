from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.crud.address import create_address
from src.crud.address import get_address
from src.crud.address import get_all_address
from src.extensions.database import get_db
from src.schemas.address import Address
from src.schemas.address import AddressBase

address_router = APIRouter()


# Routes for interacting with the API
@address_router.post("/address", response_model=Address, status_code=201)
def create_address_view(address: AddressBase, db: Session = Depends(get_db)) -> Address:
    """
    Creates Address in our db

    Args:
        address: attributes of an Address
        db: sqlalchemy session for transaction

    Returns:
        Created Address

    """
    db_address = create_address(address, db)
    return db_address


# it will fetch all latitude and longitude which are smaller than what specified in query params
@address_router.get("/address", response_model=List[Address])
def get_all_address_view(
    db: Session = Depends(get_db),
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
) -> List[Address]:
    """

    Args:
        db: sqlalchemy session for transaction
        latitude: latitude of Address
        longitude: longitude of Address

    Returns:
        Matching List of Addresses

    """
    return get_all_address(db, latitude, longitude)


@address_router.get("/address/{address_id}")
def get_address_view(address_id: int, db: Session = Depends(get_db)) -> Address:
    """

    Args:
        address_id: address to search for
        db: sqlalchemy session for transaction

    Returns:
        Address

    """
    return get_address(address_id, db)


@address_router.get("/")
async def root():
    return {"message": "This is public Endpoint!"}


def register_json_routes(app):
    pass
