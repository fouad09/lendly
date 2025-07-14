
salaried = "Salaried"
self_employed = "Self employed"

uae_resident = "UAE resident"
non_resident = "Non resident"
uae_national = "UAE national"


def generate_requirements(residency_status: str, employment_status:str , lvt=60):
    if (residency_status == 'UAE resident') and (employment_status == 'Salaried'):
        document_dict = {
            "requirements":[
                            "Passport",
                            "Visa",
                            "Emirates ID",
                            "Salary certificate (Less than 1 month old)",
                            "Bank statements (For the past 6 months)",
                            "Pay slips (For the past 6 months)",
                        ],
            "eligibility":[
                            "10,000 AED / Month",
                            "Min of 3 to 6 months working in the same company",
                            ]
        }
    elif (residency_status == 'UAE resident') and (employment_status == 'Self employed') and (lvt == 60):
        document_dict = {
            "requirements":[
                        "Passport",
                        "Visa",
                        "Emirates ID",
                        "Utility bill (Dewa, Gas, Internet)",
                        "Trade license",
                        "Memorundum of article of association (MOA)",
                        "Shareholders' certificate",
                        "Tenancy contract for the office",
                        "Personal bank statements (For the past 6 months)",
                        "Company profile as PDF file - if available",
                        "Website - if available",
                        "AECB Credit report with personal score. The full report costs 85 AED and can obtained through: https://ethihadbureau.ae",
                          ],
            "eligibility":[
                            "Average 40,000 AED / Month",
                            "Landline number",
                            "Office address",
                            "Min of 6 months of activity for the business",
                        ]
        }   
    elif (residency_status == 'UAE resident') and (employment_status == 'Self employed') and (lvt == 80):
        document_dict = {
            "requirements":[
                            "Passport",
                            "Visa",
                            "Emirates ID",
                            "Utility bill (Dewa, Gas, Internet)",
                            "Trade license",
                            "Memorundum of article of association (MOA)",
                            "Shareholders' certificate",
                            "Certificate of incorporation to confirm ownership %"
                            "Tenancy contract for the office",
                            "Personal bank statements (For the past 6 months)",
                            "Company profile as PDF file - if available",
                            "Website - if available",
                            "AECB Credit report with personal score. The full report costs 85 AED and can obtained through: https://ethihadbureau.ae",
                            "Financial audits (For the past 2 years)",
                            "Company bank statements (For the past 12 months)",
                            "VAT returns (For the past 1 year)",
                            "Purchase invoices (5 Latest)",
                            "Sales invoices (5 Latest)",
                        ],
            "eligibility":[
                            "Average 40,000 AED / Month",
                            "Landline number",
                            "Office address",
                            "Min of 6 months of activity for the business",
                        ]
        }                
    elif (residency_status == 'Non resident') and (employment_status == 'Salaried'):
        document_dict = {
            "requirements":[
                            "Passport",
                            "National ID",
                            "Utility Bill",
                            "Salary certificate (Less than 1 month old)",
                            "Bank statements (For the past 6 months)",
                            "Pay slips (For the past 6 months)",
                            "Credit bureau report",
                        ],
            "eligibility":[
                           "Avergage of 25,000 AED / Month for the past 3 months",
                        ]
        }           
    elif (residency_status == 'Non resident') and (employment_status == 'Self employed'):        
        document_dict = {
            "requirements":[
                            "Passport",
                            "National ID",
                            "Utility Bill",
                            "Trade license",
                            "Memorundum of article of association (MOA)",
                            "Certificate of incorporation to confirm ownership %",
                            "Shareholders' certificate",
                            "Salary certificate (Less than 1 month old)",
                            "Personal bank statements (For the past 6 months)",
                            "Perosnal credit bureau report",
                        ],
            "eligibility":[
                            "Avergage of 25,000 AED & 40,000 AED / Month for the past 3 months",
                            "Min of 3 years of activity for the business",
                        ]
        }        
    return document_dict