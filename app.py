from fastapi import FastAPI
from domain.domain import ApartmentRequest, ApartmentResponse
from service.apartment_service import ApartmentService

price_app = FastAPI()

@price_app.post("/predict")
async def predict_price(request: ApartmentRequest)->ApartmentResponse:
    return ApartmentService().predict_price(request=request)