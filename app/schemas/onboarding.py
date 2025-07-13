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
    sharjah = 'Sharjah'
    ras_al_khaima = 'Ras Al Khaima'

class TransactionType(str, Enum):
    resale_handover = "Resale handover"
    buyout = "Buyout"
    buyout_equity = "Buyout + Equity"
    equity = "Equity"
    primary_purchase = "Primary purchase"

class RateType(str, Enum):
    fixed = 'Fixed'
    variable = 'Variable'
    best_rate = 'Best rate'

class MortgageType(str, Enum):
    conventional = 'Conventional'
    islamic = 'Islamic'
    best_rate = 'Best rate'

class ProjectStatus(str, Enum):
    signed_the_mou = "Signed the MoU"
    made_an_offer = "Made an offer"
    viewing_properties = "Viewing properties"
    still_looking = 'Still looking'    

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