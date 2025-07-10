import numpy_financial as npf
import numpy as np
income_dict =  {
    "monthly_salary":0,
    "rental_income_salary":0,
    "education_salary":0,
    "variable_pay":0
}

liabilities_dict =  {
    "credit_card_1":0,
    "credit_card_2":0,
    "credit_card_3":0,
    "credit_card_4":0,
    "auto_loan":0,
    "personal_loan":0,
}

def calculate_monthly_payment(
    purchase_price: float,
    down_payment: float,
    interest_rate: float,
    number_of_months: int,
):
    """
    This function calculate the expected monthly payment
    """

    principal_borrowed = purchase_price - down_payment
    monthly_payment = npf.pmt(interest_rate, number_of_months, principal_borrowed)
    return monthly_payment


def calculate_dbr(
    monthly_payment: float,
    cumulative_income: dict,
    cumulative_liabilities: dict,
):
    """
    This function calculate the client dbr    
    """
    total_income = sum([v for k,v in cumulative_income.items()])
    total_liabilities = sum([v for k,v in cumulative_liabilities.items()])
    dbr = np.round(100 * total_income / (total_liabilities + monthly_payment),2)
    return dbr

