"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr, constr
from typing import Optional
from datetime import date, time

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Restaurant app schemas

class Booking(BaseModel):
    """
    Table bookings collection schema
    Collection name: "booking"
    """
    name: constr(strip_whitespace=True, min_length=2) = Field(..., description="Guest full name")
    email: EmailStr = Field(..., description="Guest email")
    phone: constr(strip_whitespace=True, min_length=6) = Field(..., description="Contact phone number")
    date: date = Field(..., description="Reservation date")
    time: time = Field(..., description="Reservation time")
    guests: int = Field(..., ge=1, le=20, description="Number of guests")
    message: Optional[str] = Field(None, description="Optional note or request")

class ContactMessage(BaseModel):
    """
    Contact messages collection schema
    Collection name: "contactmessage"
    """
    name: constr(strip_whitespace=True, min_length=2) = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    phone: Optional[constr(strip_whitespace=True, min_length=6)] = Field(None, description="Phone number")
    subject: Optional[str] = Field(None, description="Subject of the message")
    message: str = Field(..., min_length=5, description="Message body")

# Add your own schemas here:
# --------------------------------------------------

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
