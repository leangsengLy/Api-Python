from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Product schema
class Product(BaseModel):
    id: int
    name: str
    englishname: str
    price: float
    qty: int
    description: Optional[str] = None

# Fake in-memory "database"
products: List[Product] = []


# Get all products
@app.get("/products", response_model=List[Product])
def get_products():
    return products


# Get product by ID
@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# Add new product
@app.post("/products", response_model=Product)
def add_product(product: Product):
    # Check if product ID already exists
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product ID already exists")
    products.append(product)
    return product


# Update product
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


# Delete product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")

    