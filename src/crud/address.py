from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from src.extensions.database import get_db
from src.models.address import Address
from src.schemas.address import AddressBase


# Methods for interacting with the database
def get_address(address_id: int, db: Session = Depends(get_db)) -> Address:
    """

    Args:
        address_id: Address to be searched for
        db: Session for transaction

    Returns:
        Address
    """
    return db.query(Address).where(Address.id == address_id).first()


def get_all_address(
    db: Session = Depends(get_db), latitude: float = None, longitude: float = None
) -> List[Address]:
    """

    Args:
        db: Session for transaction
        latitude: Filter by all Addresses whose latitude is less than this
        longitude: Filter by all Addresses whose longitude is less than this

    Returns:
        List of matching Addresses.

    """
    if latitude and longitude:
        return (
            db.query(Address)
            .filter(Address.latitude <= latitude, Address.longitude <= longitude)
            .all()
        )
    return db.query(Address).all()


def create_address(address: AddressBase, db: Session = Depends(get_db)) -> Address:
    """

    Args:
        address:
        db: Session for transaction

    Returns:
        Created Address

    """
    db_address = Address(**address.dict())

    try:
        db.add(db_address)
        db.commit()
        db.refresh(db_address)
    except Exception:
        db.rollback()

    return db_address
