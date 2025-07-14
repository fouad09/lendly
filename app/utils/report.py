import numpy_financial as npf
import numpy as np
from app.utils.gcp import read_rates
from app.utils.loan_requirements import generate_requirements

def calculate_monthly_payment(
    principal_borrowed: float,
    interest_rate: float,
    mortgage_number_of_months: int,
):
    """
    This function calculate the expected monthly payment
    """
    # monthly rate
    monthly_interest_rate = (interest_rate * 0.01) / 12
    monthly_interest_rate = np.round(monthly_interest_rate, 6)
    
    # monthly payment
    monthly_payment = -npf.pmt(monthly_interest_rate, mortgage_number_of_months, principal_borrowed)
    monthly_payment = np.round(monthly_payment,0)
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
    
    credit_cards = cumulative_liabilities.pop('credit_cards')
    total_liabilities = sum([v for v in cumulative_liabilities.values()])
    cumulative_liabilities['credit_cards'] = credit_cards
    total_debt = total_liabilities + monthly_payment

    if (total_income == 0):
        dbr = 100
    else:
        dbr = total_debt / total_income
        dbr = np.round(100 * dbr, 2)
    return dbr

def generate_report(
    project_info:dict,
    personal_info:dict,
    income_info:dict,
    liabilities_info:dict,
    mortgage_info:dict,
    dbr_threshold: float= 50,
):
    """
    This function calculate the expected monthly payment
    """
    # read rate table
    rate_df = read_rates()

    # filter residency status
    residency_status = personal_info.get('residency_status')
    rate_df = rate_df[rate_df['citizen_state'] == residency_status.upper()]
    
    # filter employment status
    employment_status = personal_info.get('employment_status')
    if employment_status == 'Salaried':
        rate_df = rate_df[rate_df['type_of_employment'] == 'SALARY']    
    elif employment_status == 'Self employed':
        rate_df = rate_df[rate_df['type_of_employment'] == 'SELF EMPLOYMENT']    

    # filter transaction type
    transaction_type = project_info.get('transaction_type')

    if transaction_type.upper() == 'Primary purchase':
        rate_df = rate_df[rate_df['type_of_transaction'] == 'PRIMARY PURCHASE']
    elif transaction_type.upper() == "Resale handover":
        rate_df = rate_df[rate_df['type_of_transaction'] == 'BUY A PROPERTY']
    elif transaction_type.upper() == 'Buyout + Equity':
        rate_df = rate_df[rate_df['type_of_transaction'] == 'BUYOUT + EQUITY']
    elif transaction_type.upper() == "Equity":
        rate_df = rate_df[rate_df['type_of_transaction'] == 'CASH OUT PROPERTY']
    elif transaction_type.upper() ==  "Buyout":
        rate_df = rate_df[rate_df['type_of_transaction'] == 'TRANSFER OF EXISTING MORTGAGE']

    # filter salary transfer
    salary_transfer = mortgage_info.get('salary_transfer')
    if salary_transfer == "Yes":
        rate_df = rate_df[rate_df['type_of_account'] == 'STL']
    else:
        rate_df = rate_df[rate_df['type_of_account'] != 'STL']

    # filter mortgage type
    mortgage_type = mortgage_info.get('mortgage_type')
    if mortgage_type in ['Conventional','Islamic']:
        rate_df = rate_df[rate_df['type_of_mortgage'] == mortgage_type.upper()]    

    # filter rate type
    rate_type = mortgage_info.get('rate_type')
    if rate_type == 'Fixed':
        rate_df = rate_df[rate_df['interest_rate_type'] == rate_type.lower()]
        rate_df['best_rate'] = rate_df['fixed_rate']
    elif rate_type == 'Variable':
        rate_df = rate_df[rate_df['interest_rate_type'] == rate_type.lower()]
        rate_df['best_rate'] = rate_df['follow_on_rate']
    else:
        rate_df['best_rate'] = rate_df[['follow_on_rate','fixed_rate']].min(axis=1)
    
    rate_df['best_rate'] = rate_df['best_rate'].astype(float)
    rate_df = rate_df[rate_df['best_rate'] != 0]
    best_rates_idx = rate_df.groupby('bank_name')['best_rate'].idxmin()
    offers_df = rate_df.loc[best_rates_idx]
    offers_df = offers_df.sort_values(by='best_rate', ascending=True)
    number_of_offers = len(offers_df)
    offers_df = offers_df.iloc[:3]
    interest_rate = offers_df.iloc[0].best_rate
    bank_max_mortgage_year = offers_df.iloc[0].maximum_length_of_mortgage

    purchase_price = project_info.get('purchase_price')
    down_payment = project_info.get('down_payment')
    age = personal_info.get('age')

    # client max mortgage duration
    client_max_mortgage_year = max(65 - age, 0) 
    client_max_mortgage_month = float(client_max_mortgage_year) * 12
    
    # bank max mortgage duration
    bank_max_numer_of_months = float(bank_max_mortgage_year) * 12
    mortgage_number_of_months = min(bank_max_numer_of_months, client_max_mortgage_month)
    mortgage_number_of_years = np.floor(mortgage_number_of_months / 12)

    # principale borrowed
    principal_borrowed = purchase_price - down_payment  

    # loan to value
    loan_to_value =  np.round(down_payment / purchase_price,0)

    # down payment (%)
    try:
        down_payment_pct = np.round(100 * down_payment / purchase_price,2)
    except:
        down_payment_pct = 0

    # documents
    document_dict = generate_requirements(
        residency_status=residency_status,
        employment_status=employment_status,
    )

    documents_required = document_dict.get('requirements')
    eligibility = document_dict.get('eligibility')

    # offers
    offers_list = offers_df.to_dict('records')
    
    for offer in offers_list:
        best_rate = offer.get('best_rate')

        # monthly payments
        monthly_payments = calculate_monthly_payment(
            principal_borrowed, 
            best_rate,
            mortgage_number_of_months,
        )

        # dbr
        dbr = calculate_dbr(monthly_payments, income_info, liabilities_info)
        
        offer['monthly_payment'] = monthly_payments
        offer['dbr'] = dbr

    return {
        "number_of_offers":number_of_offers,
        "mortage_lenth_month":mortgage_number_of_months,
        "mortage_lenth_year":mortgage_number_of_years,
        "principal_borrowed":principal_borrowed,
        "loan_to_value":loan_to_value,
        "down_payment_pct":down_payment_pct,
        "documents_required":documents_required,
        "eligibility":eligibility,
        "offers_list":offers_list
    }