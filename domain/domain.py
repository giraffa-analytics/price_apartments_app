from pydantic import BaseModel

class ApartmentRequest(BaseModel):
    rooms: int
    size: int
    bathrooms: int
    neighbourhood: str
    year_built: int

class ApartmentResponse(BaseModel):
    price: int