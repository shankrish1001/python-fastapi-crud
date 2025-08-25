from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    product_name: Optional[str] = None
    product_info: Optional[str] = None
    product_price: Optional[float] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

