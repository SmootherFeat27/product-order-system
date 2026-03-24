from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/vendors", tags=["Vendors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ➤ Create Vendor
@router.post("/")
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    db_vendor = models.Vendor(
        name=vendor.name,
        contact=vendor.contact,
        rating=vendor.rating
    )
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

# ➤ Get All Vendors
@router.get("/")
def get_vendors(db: Session = Depends(get_db)):
    return db.query(models.Vendor).all()
