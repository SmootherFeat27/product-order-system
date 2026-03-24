from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ➤ Create Product
@router.post("/")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(
        name=product.name,
        sku=product.sku,
        unit_price=product.unit_price,
        stock_level=product.stock_level
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# ➤ Get All Products
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()
