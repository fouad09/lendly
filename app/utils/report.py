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
    total_debt = total_liabilities + monthly_payment
    if (total_income == 0):
        dbr = 100
    else:
        dbr = total_debt / total_income
        dbr = np.round(100 * dbr, 2)
    return dbr


def generate_report(
    purchase_price: float,
    down_payment: float,
    interest_rate: float,
    number_of_months: int,        
    cumulative_income: dict,
    cumulative_liabilities: dict,
    dbr_threshold: float =50,
):
    """
    This function calculate the expected monthly payment
    """
    
    monthly_payments = calculate_monthly_payment(
        purchase_price, 
        down_payment, 
        interest_rate,
        number_of_months
    )
    
    dbr = calculate_dbr(monthly_payments, cumulative_income, cumulative_liabilities)
        
    if dbr < dbr_threshold:
        status = "OK"
    else:
        status = "NOT APPROVED"
    try:
        down_payment_pct = np.round(100 * down_payment / purchase_price,2)
    except:
        down_payment_pct = 0

    return {
        "monthly_payments": monthly_payments,
        "dbr": dbr,
        "down_payment_pct":down_payment_pct,
        "status": status,
    }


