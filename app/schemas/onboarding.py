from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum

class ApplicationStatus(str, Enum):
    alone = "Alone"
    joint = "Joint"

class ResidencyStatus(str, Enum):
    uae_resident = "UAE resident"
    non_resident = "Non resident"
    uae_national = "UAE national"

class EmploymentStatus(str, Enum):
    salaried = "Salaried"
    self_employed = "Self employed"

class EmiratesList(str, Enum):
    abu_dhabi = 'Abu Dhabi'
    dubai = 'Dubai'
    others = 'Others'

class TransactionType(str, Enum):
    resale_handover = "Resale/Resale handover"
    buyout = "Buyout"
    buyout_equity = "Buyout + Equity"
    equity = "Equity"

class RateType(str, Enum):
    fixed = 'Fixed'
    variable = 'Variable'
    best_rate = 'Best rate'

class MortgageType(str, Enum):
    conventional = 'Conventional'
    islamic = 'Islamic'
    best_rate = 'Best rate'

class ProjectStatus(str, Enum):
    mou_signed = "MoU signed"
    made_an_offer = "Made an offer"
    shopping = "Shopping"

class SalaryTransfer(str, Enum):
    yes = "Yes"
    no = "No"

class PersonalInfo(BaseModel):

    residency_status: ResidencyStatus
    employment_status: EmploymentStatus
    application_status: ApplicationStatus
    age: int = Field(..., ge=21, le=65, description="Age") 

class IncomeInfo(BaseModel):

    monthly_salary: float = Field(..., ge=10000, description="Monthly salary") 
    rental_income_salary: float = Field(..., ge=0, description="Rental revenue from properties") 
    education_salary: float = Field(..., ge=0, description="Paid amount for kids Education ") 
    variable_pay:float = Field(..., ge=0, description="Yearly bonus") 

class LiabilitiesInfo(BaseModel):

    credit_cards: int = Field(..., ge=0, description="Number of Credit cards")
    credit_cards_limit: float = Field(..., ge=0, description="Credit cards amount limit")
    auto_loan: float = Field(..., ge=0, description="Auto loan monthly payment")
    personal_loan: float = Field(..., ge=0, description="Personal loan monthly payment")
    existing_mortgage: float = Field(..., ge=0, description="Existing mortgage monthly payment")

class ProjectInfo(BaseModel):

    property_location_emirates: EmiratesList
    project_status: ProjectStatus
    transaction_type: TransactionType
    purchase_price: float = Field(..., ge=400000, le=20000000, description="Property value") 
    down_payment: float = Field(..., ge=100000, description="Down payment") 


class MortgageInfo(BaseModel):

    mortgage_type: MortgageType
    rate_type: RateType 
    mortgage_duration: float = Field(..., ge=1,le=25, description="Down payment") 
    salary_transfer: SalaryTransfer


class OnboardingForm(BaseModel):

    personal_info: PersonalInfo
    project_info: ProjectInfo
    income_info: IncomeInfo
    liabilities_info: LiabilitiesInfo
    mortgage_info: MortgageInfo


class OboardingResponse(BaseModel):
    
    input_data: OnboardingForm
    output_data: dict