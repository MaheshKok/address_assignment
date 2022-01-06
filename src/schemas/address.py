from pydantic import BaseModel
from pydantic import validator


class AddressBase(BaseModel):
    latitude: float
    longitude: float
    primary: bool
    pin_code: int

    @validator("latitude")
    def validate_latitude(cls, value):
        # Taken from official google docs:
        # https://support.google.com/maps/answer/18539?hl=en&co=GENIE.Platform%3DDesktop
        assert -90.0 <= value <= 90.0, "latitude must lie within -90 and 90"
        return value

    @validator("longitude")
    def validate_longitude(cls, value):
        # Taken from official google docs:
        # https://support.google.com/maps/answer/18539?hl=en&co=GENIE.Platform%3DDesktop
        assert -180.0 <= value <= 180.0, "longitude must lie within -180 and 180"
        return value


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
