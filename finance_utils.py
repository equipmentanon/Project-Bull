import pandas as pd

def generate_amortization_schedule(cost, annual_rate, loan_term, emor, monthly_rent, salvage):
    """
    Generate a month-by-month amortization schedule for a piece of equipment.

    Parameters:
      cost         : Purchase price of the equipment.
      annual_rate  : Annual interest rate as a percentage (e.g., 5.95).
      loan_term    : Total loan term in months (e.g., 60).
      emor         : Rental period in months.
      monthly_rent : Monthly rental rate.
      salvage      : Salvage value of the equipment.

    Returns:
      schedule_df  : A DataFrame containing the monthly breakdown.
    """
    monthly_interest_rate = annual_rate / 100 / 12
    if monthly_interest_rate != 0:
        pmt = cost * monthly_interest_rate * (1 + monthly_interest_rate)**loan_term / ((1 + monthly_interest_rate)**loan_term - 1)
    else:
        pmt = cost / loan_term

    balance = cost
    schedule = []
    for month in range(1, loan_term + 1):
        interest = balance * monthly_interest_rate
        principal = pmt - interest
        new_balance = balance - principal
        # Rental income is received only during the EMOR period
        rent_income = monthly_rent if month <= emor else 0
        net_cash_flow = rent_income - pmt

        schedule.append({
            "Month": month,
            "Beginning Balance": balance,
            "Interest": interest,
            "Principal": principal,
            "Payment (PMT)": pmt,
            "Ending Balance": new_balance,
            "Rental Income": rent_income,
            "Net Cash Flow": net_cash_flow
        })
        balance = new_balance

    schedule_df = pd.DataFrame(schedule)
    return schedule_df
