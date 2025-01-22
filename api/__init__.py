from fastapi import FastAPI
from api.customers.routes import customer_router

app = FastAPI()

app.include_router(customer_router, prefix="/customers")