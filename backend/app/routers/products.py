from fastapi import APIRouter, Depends
from app.models.products import Product
from app.schemas.products import ProductCreate
from app.db.base import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db.query()
    return products


@router.get("/product/{id}")
def get_all_products_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found!"


@router.post("/product")
def add_product(product: ProductCreate):
    products.append(product)

@router.put("/product")
def update_product(id: int, product:ProductCreate):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully!"
    return "No product found!"


@router.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "No product found!"
