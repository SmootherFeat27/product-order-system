from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import purchase_order, vendor, product
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(purchase_order.router)
app.include_router(vendor.router)
app.include_router(product.router)

@app.get("/")
def read_root():
    return {"message": "API Running"}
