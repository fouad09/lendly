import numpy_financial as npf
import numpy as np


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

