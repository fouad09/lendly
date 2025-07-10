from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
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
    data = data.model_dump()
    return {
        'input': data,
    }