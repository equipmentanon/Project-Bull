import streamlit as st
import pandas as pd
import math
import altair as alt

st.title("Equipment Rental Financial Analysis")

# Full default equipment dataset
default_data = [
    {
        "Equipment Description": "FORKLIFT VARIABLE REACH 5000# 16-20'",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 65000,
        "Provided PMT": -1255,
        "ALPHA": 504,
        "Day": 341,
        "Week": 875,
        "Month": 1759,
        "Salvage": 46429
    },
    {
        "Equipment Description": "FORKLIFT VARIABLE REACH 6000# 30-36'",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 99960,
        "Provided PMT": -1930,
        "ALPHA": -68,
        "Day": 343,
        "Week": 887,
        "Month": 1862,
        "Salvage": 71400
    },
    {
        "Equipment Description": "FORKLIFT VARIABLE REACH 8000# 40-49'",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 108800,
        "Provided PMT": -2101,
        "ALPHA": 158,
        "Day": 323,
        "Week": 992,
        "Month": 2259,
        "Salvage": 77714
    },
    {
        "Equipment Description": "FORKLIFT VARIABLE REACH 10000# 50' & UP",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 138040,
        "Provided PMT": -2665,
        "ALPHA": 557,
        "Day": 571,
        "Week": 1466,
        "Month": 3222,
        "Salvage": 98600
    },
    {
        "Equipment Description": "FORKLIFT VARIABLE REACH 12000# 53'-69'",
        "Qty": 3,
        "EMOR": 15,
        "Cost": 161160,
        "Provided PMT": -3112,
        "ALPHA": 570,
        "Day": 639,
        "Week": 1683,
        "Month": 3682,
        "Salvage": 115114
    },
    {
        "Equipment Description": "SCISSOR LIFT 19' ELECTRIC",
        "Qty": 25,
        "EMOR": 15,
        "Cost": 12067,
        "Provided PMT": -233,
        "ALPHA": 141,
        "Day": 124,
        "Week": 235,
        "Month": 374,
        "Salvage": 8619
    },
    {
        "Equipment Description": "SCISSOR LIFT 24-26' ELECTRIC 30-36\" WIDE",
        "Qty": 25,
        "EMOR": 15,
        "Cost": 18154,
        "Provided PMT": -351,
        "ALPHA": 188,
        "Day": 157,
        "Week": 312,
        "Month": 539,
        "Salvage": 12967
    },
    {
        "Equipment Description": "SCISSOR LIFT 30-33' ELECTRIC 32\" WIDE",
        "Qty": 25,
        "EMOR": 15,
        "Cost": 27032,
        "Provided PMT": -522,
        "ALPHA": 231,
        "Day": 204,
        "Week": 419,
        "Month": 753,
        "Salvage": 19309
    },
    {
        "Equipment Description": "SCISSOR LIFT 30-35' ELECTRIC 46-48\" WIDE",
        "Qty": 25,
        "EMOR": 15,
        "Cost": 21964,
        "Provided PMT": -424,
        "ALPHA": 370,
        "Day": 191,
        "Week": 392,
        "Month": 794,
        "Salvage": 15689
    },
    {
        "Equipment Description": "SCISSOR LIFT 30-35' IC 4WD",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 42296,
        "Provided PMT": -817,
        "ALPHA": 420,
        "Day": 271,
        "Week": 653,
        "Month": 1237,
        "Salvage": 30211
    },
    {
        "Equipment Description": "SCISSOR LIFT 36-49' IC 4WD",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 50110,
        "Provided PMT": -968,
        "ALPHA": 597,
        "Day": 333,
        "Week": 760,
        "Month": 1565,
        "Salvage": 35793
    },
    {
        "Equipment Description": "SCISSOR LIFT 45' ELECTRIC 50-55\" WIDE",
        "Qty": 10,
        "EMOR": 15,
        "Cost": 37245,
        "Provided PMT": -719,
        "ALPHA": 853,
        "Day": 342,
        "Week": 700,
        "Month": 1572,
        "Salvage": 26604
    },
    {
        "Equipment Description": "BOOM 40-50' ARTICULATING",
        "Qty": 10,
        "EMOR": 15,
        "Cost": 69373,
        "Provided PMT": -1340,
        "ALPHA": 91,
        "Day": 315,
        "Week": 590,
        "Month": 1431,
        "Salvage": 49552
    },
    {
        "Equipment Description": "BOOM 45-50' TELESCOPIC 4WD",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 75947,
        "Provided PMT": -1466,
        "ALPHA": 100,
        "Day": 353,
        "Week": 799,
        "Month": 1566,
        "Salvage": 54248
    },
    {
        "Equipment Description": "BOOM 65-70' TELESCOPIC",
        "Qty": 10,
        "EMOR": 15,
        "Cost": 114722,
        "Provided PMT": -2215,
        "ALPHA": -12,
        "Day": 423,
        "Week": 1068,
        "Month": 2203,
        "Salvage": 81944
    },
    {
        "Equipment Description": "BOOM 84-86' TELESCOPIC 4WD",
        "Qty": 5,
        "EMOR": 15,
        "Cost": 156871,
        "Provided PMT": -3029,
        "ALPHA": 350,
        "Day": 699,
        "Week": 1664,
        "Month": 3379,
        "Salvage": 112051
    },
    {
        "Equipment Description": "UTV 4WD DSL 4SEAT ROPS",
        "Qty": 25,
        "EMOR": 30,
        "Cost": 16750,
        "Provided PMT": -323,
        "ALPHA": 252,
        "Day": 114,
        "Week": 270,
        "Month": 575,
        "Salvage": 11964
    }
]

st.subheader("Edit Equipment Data")
# Editable data table (requires Streamlit v1.18+)
df = st.data_editor(pd.DataFrame(default_data), num_rows="dynamic")

# Global inputs
annual_interest_rate = st.number_input("Enter Annual Interest Rate (%)", value=5.95, step=0.1)
loan_term = st.number_input("Enter Loan Term (months)", value=60, step=1)

# Define financial functions
def calculate_pmt(P, annual_rate, term):
    r = annual_rate / 100 / 12
    n = term
    return P * r * (1 + r)**n / ((1 + r)**n - 1)

def calculate_remaining_balance(P, annual_rate, m, pmt):
    r = annual_rate / 100 / 12
    return P * (1 + r)**m - pmt * ((1 + r)**m - 1) / r

if st.button("Run Analysis"):
    # Initialize lists for computed metrics
    aggregated_pmts = []             
    aggregated_debt_services = []      
    aggregated_remaining_balances = [] 
    aggregated_monthly_revenues = []   
    aggregated_rent_profits = []       
    aggregated_salvage_nets = []       
    aggregated_arbitrage_profits = []  
    
    # Calculate metrics for each row
    for index, row in df.iterrows():
        cost = row["Cost"]
        emor = row["EMOR"]
        quantity = row["Qty"]
        monthly_rate = row["Month"]
        salvage_value_per_unit = row["Salvage"]
        
        pmt_per_unit = calculate_pmt(cost, annual_interest_rate, loan_term)
        aggregated_pmt = pmt_per_unit * quantity
        aggregated_pmts.append(aggregated_pmt)
        
        total_debt_per_unit = pmt_per_unit * emor
        aggregated_debt_service = total_debt_per_unit * quantity
        aggregated_debt_services.append(aggregated_debt_service)
        
        remaining_balance_per_unit = calculate_remaining_balance(cost, annual_interest_rate, emor, pmt_per_unit)
        aggregated_remaining_balance = remaining_balance_per_unit * quantity
        aggregated_remaining_balances.append(aggregated_remaining_balance)
        
        monthly_revenue_aggregated = monthly_rate * emor * quantity
        aggregated_monthly_revenues.append(monthly_revenue_aggregated)
        
        rent_profit_aggregated = monthly_revenue_aggregated - aggregated_debt_service
        aggregated_rent_profits.append(rent_profit_aggregated)
        
        aggregated_salvage = salvage_value_per_unit * quantity
        salvage_net_aggregated = aggregated_salvage - aggregated_remaining_balance
        aggregated_salvage_nets.append(salvage_net_aggregated)
        
        arbitrage_profit_aggregated = rent_profit_aggregated + salvage_net_aggregated
        aggregated_arbitrage_profits.append(arbitrage_profit_aggregated)
    
    # Add new columns to the DataFrame
    df["Aggregated PMT"] = aggregated_pmts
    df["Aggregated Debt Service"] = aggregated_debt_services
    df["Aggregated Remaining Balance"] = aggregated_remaining_balances
    df["Aggregated Monthly Revenue"] = aggregated_monthly_revenues
    df["Aggregated Rent Profit"] = aggregated_rent_profits
    df["Aggregated Salvage Net"] = aggregated_salvage_nets
    df["Aggregated Arbitrage Profit"] = aggregated_arbitrage_profits
    
    st.subheader("Analysis Results")
    st.dataframe(df)
    
    st.subheader("Suggestions/Observations")
    for index, row in df.iterrows():
        equipment = row["Equipment Description"]
        arbitrage = row["Aggregated Arbitrage Profit"]
        if arbitrage < 0:
            st.write(f"- {equipment}: Negative arbitrage profit ({arbitrage:.2f}). Consider adjusting rates or financing terms.")
        else:
            st.write(f"- {equipment}: Positive arbitrage profit ({arbitrage:.2f}).")
    
    # Create charts using Altair
    st.subheader("Profitability Charts")
    
    # Bar chart for Aggregated Arbitrage Profit
    chart_data = df[["Equipment Description", "Aggregated Arbitrage Profit"]]
    chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X("Equipment Description:N", sort=None, title="Equipment"),
        y=alt.Y("Aggregated Arbitrage Profit:Q", title="Arbitrage Profit"),
        tooltip=["Equipment Description", "Aggregated Arbitrage Profit"]
    ).properties(width=700, height=400, title="Arbitrage Profit by Equipment")
    st.altair_chart(chart, use_container_width=True)
    
    # Bar chart for Aggregated Rent Profit
    rent_chart_data = df[["Equipment Description", "Aggregated Rent Profit"]]
    rent_chart = alt.Chart(rent_chart_data).mark_bar(color="orange").encode(
        x=alt.X("Equipment Description:N", sort=None, title="Equipment"),
        y=alt.Y("Aggregated Rent Profit:Q", title="Rent Profit"),
        tooltip=["Equipment Description", "Aggregated Rent Profit"]
    ).properties(width=700, height=400, title="Rent Profit by Equipment")
    st.altair_chart(rent_chart, use_container_width=True)
