from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum

class ResidencyStatus(str, Enum):
    uae_resident = "UAE Resident"
    non_resident = "NON Resident"
    uae_national = "UAE National"

class EmploymentStatus(str, Enum):
    salaried = "Salary"
    self_employed = "Self employment"

class EmiratesList(str, Enum):
    abu_dhabi = 'Abu Dhabi'
    dubai = 'Dubai'
    sharja = 'Sharja'
    ras_al_khaima = 'Ras Al Khaima'

class TransactionType(str, Enum):
    first_time = 'First time'
    already_have_a_mortgage = 'Already have a mortgage'
    buy_out = 'Buy out'
    cash_out ='Cash out'
    mortgage_transfer = 'Mortgage transfer'

class RateType(str, Enum):
    fixed = 'Fixed'
    variable = 'Variable'
    any = 'Any'

class MortgageType(str, Enum):
    conventional = 'Conventional'
    islamic = 'Islamic'
    any = 'Any'

class ProjectStatus(str, Enum):
    property_found = 'Found a property'
    still_looking = 'Still looking'


class PersonalInfo(BaseModel):

    residency_status: ResidencyStatus
    employment_status: EmploymentStatus
    applying_alone: bool
    age: int = Field(..., ge=21, le=65, description="Age") 

class IncomeInfo(BaseModel):

    monthly_salary: float = Field(..., ge=10000, description="Monthly salary") 
    rental_income_salary: float = Field(..., ge=0, description="Rental revenue from properties") 
    education_salary: float = Field(..., ge=0, description="Paid amount for kids Education ") 
    variable_pay:float = Field(..., ge=0, description="Yearly bonus") 

class LiabilitiesInfo(BaseModel):

    credit_cards: int = Field(..., ge=0, description="Number of Credit cards")
    credit_cards_limit: float = Field(..., ge=0, description="Credit cards amount limit")
    auto_loan: float = Field(..., ge=0, description="Auto loan remaining amount")
    personal_loan: float = Field(..., ge=0, description="Personal loan remaining amount")

class ProjectInfo(BaseModel):

    property_location_emirates: EmiratesList
    project_status: ProjectStatus
    transaction_type: TransactionType
    purchase_price: float = Field(..., ge=400000, le=20000000, description="Property value") 
    down_payment: float = Field(..., ge=100000, description="Down payment") 


class MortgageInfo(BaseModel):

    mortgage_type: MortgageType
    rate_type: RateType 
    salary_transfer: bool


class OnboardingForm(BaseModel):

    personal_info: PersonalInfo
    project_info: ProjectInfo
    income_info: IncomeInfo
    liabilities_info: LiabilitiesInfo
    mortgage_info: MortgageInfo


class OboardingResponse(BaseModel):
    
    input_data: OnboardingForm
    output_data: dict