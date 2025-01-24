from fastapi import FastAPI
from api.features.customers.routes import customer_router
from api.features.countries.routes import country_router

app = FastAPI()

app.include_router(customer_router, prefix="/customers")
app.include_router(country_router, prefix="/countries")