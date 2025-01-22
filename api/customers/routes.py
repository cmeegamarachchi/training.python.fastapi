import json
import aiofiles
import os
from typing import List
from fastapi import APIRouter
from api.customers.schema import Customer

customer_router = APIRouter()

async def read_customers_from_json() -> List[Customer]:
    file_path = os.path.join(os.path.dirname(__file__), 'customers.json')
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        contents = await f.read()
    data = json.loads(contents) 
    return [Customer(**item) for item in data]

@customer_router.get("/", response_model=List[Customer])
async def get_all_customers():
    data = await read_customers_from_json()
    return data

@customer_router.get("/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    data = await read_customers_from_json()
    customer = next((c for c in data if c.id == customer_id), None)
    if customer:
        return customer
    return {"error": "Customer not found"}

@customer_router.post("/", response_model=Customer)
async def create_customer(customer: Customer):
    data = await read_customers_from_json()
    data.append(customer)
    file_path = os.path.join(os.path.dirname(__file__), 'customers.json')
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
        await f.write(json.dumps([c.dict() for c in data], indent=4))
    return customer

@customer_router.put("/{customer_id}", response_model=Customer)
async def update_customer(customer_id: int, customer: Customer):
    data = await read_customers_from_json()
    customer_index = next((i for i, c in enumerate(data) if c.id == customer_id), None)
    if customer_index is not None:
        data[customer_index] = customer
        file_path = os.path.join(os.path.dirname(__file__), 'customers.json')
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
            await f.write(json.dumps([c.dict() for c in data], indent=4))
        return customer
    return {"error": "Customer not found"}