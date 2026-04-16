from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None
    is_subscribed: Optional[bool] = None

class Product(BaseModel):
    product_id: int
    name: str
    category: str
    price: float

sample_products: List[Product] = [
    Product(product_id=1, name="Smartphone", category="Electronics", price=599.99),
    Product(product_id=2, name="Phone Case", category="Accessories", price=19.99),
    Product(product_id=3, name="Iphone", category="Electronics", price=1299.99),
    Product(product_id=4, name="Headphones", category="Accessories", price=99.99),
    Product(product_id=5, name="Smartwatch", category="Electronics", price=299.99),
]
