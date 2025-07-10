from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PersonalInfo(BaseModel):
    residency_status: str
    employment_status: str
    applying_alone: bool
    age: int

class IncomeInfo(BaseModel):

    monthly_salary: float = 0
    rental_income_salary: float = 0
    education_salary: float = 0
    variable_pay:float = 0

class LiabilitiesInfo(BaseModel):

    credit_card_1: float = 0
    credit_card_2: float = 0
    credit_card_3: float = 0
    credit_card_4: float = 0
    auto_loan: float = 0
    personal_loan: float = 0

class ProjectInfo(BaseModel):

    purchase_price: float
    down_payment: float
    purchase_type: str
    property_status: str
    property_location_emirates: str

class OnboardingForm(BaseModel):

    personal_info: PersonalInfo
    project_info: ProjectInfo
    income_info: IncomeInfo
    liabilities_info: LiabilitiesInfo


class OboardingResponse(BaseModel):
    input_data: OnboardingForm
    output_data: dict