

# LENDLY 

This is the complete backend for LENDLY mortgage platform built with FastAPI. It includes:
- Auth & role-based access
- Client onboarding
- Application monitoring
- Alembic migrations
- Heroku deployment support

## To run the app localy

1. create a virtual environment

'''
python -m venv lendly
source lendly/bin/activate
'''

2. install all the project requirements

'''shell
pip install -r requirements.txt
'''

3. lunch the app

'''
uvicorn app.main:app --reload
'''

4. to run all the tests

'''
python -m pytest
'''

5. to format the python code to PEP8

'''
python -m black app
'''

6. to migrate db

'''

alembic revision --autogenerate -m "Update my migration"

alembic upgrade head

'''
