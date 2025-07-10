from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.session import create_tables
from app.routes import onboarding

app = FastAPI(title="Lendly API")

app.include_router(onboarding.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_tables()
