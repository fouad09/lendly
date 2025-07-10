from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OnboardingForm(BaseModel):
    residency_status: str
    employment_status: str
    applying_alone: bool
    age: int
    monthly_income: float
    purchase_type: str
    mortgage_status: str
    property_status: str
    property_location_emirates: str
    property_value: float



class OboardingResponse(BaseModel):
    input: OnboardingForm