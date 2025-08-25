from sqlalchemy import Column, Integer, String, Text, Numeric, TIMESTAMP, func
from database import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(100), nullable=True)
    product_info = Column(Text, nullable=True)
    product_price = Column(Numeric, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=True)

