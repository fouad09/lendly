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

    project_info = input_data.get('project_info')
    personal_info = input_data.get('personal_info')
    income_info = input_data.get('income_info')
    liabilities_info = input_data.get('liabilities_info')
    mortgage_info = input_data.get('mortgage_info')

    # generate report
    output_data = generate_report(
        project_info=project_info,
        personal_info=personal_info,
        income_info=income_info,
        liabilities_info=liabilities_info,
        mortgage_info=mortgage_info,
    )

    return {
        'input_data': input_data,
        'output_data':output_data,
    }