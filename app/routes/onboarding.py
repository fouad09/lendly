from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.utils.report import generate_report
from app.schemas.onboarding import OnboardingForm, OboardingResponse

router = APIRouter(prefix="/onboarding", tags=["Onboarding"])


@router.post(
    "/report",
    response_model=OboardingResponse,
    status_code=status.HTTP_201_CREATED,
)
def get_report(
    data: OnboardingForm,
):
    input_data = data.model_dump()

    interest_rate = 0.07

    # project info
    project_info = input_data.get('project_info')
    purchase_price =  project_info.get('purchase_price')
    down_payment = project_info.get('down_payment')

    # personal info
    personal_info = input_data.get('personal_info')
    age = personal_info.get('age')
    number_of_months = max(65 - age, 0)
    cumulative_income = input_data.get('income_info')
    cumulative_liabilities = input_data.get('liabilities_info')

    # generate report
    output_data = generate_report(
        purchase_price, down_payment,
        interest_rate, number_of_months,
        cumulative_income, cumulative_liabilities
    )

    return {
        'input_data': input_data,
        'output_data':output_data,
    }