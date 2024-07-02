# Real Estate Helper

## To evaluate offers found on the internet, I am writing a simple Python app that calculates the relevant KPIs from a simple yml file. For the time being the process is supposed to look as follows:
1. Find an offer online.
2. Identify the data in the offer.
3. Fill the yml file with the according data.
4. Run the program and recieve an output file.

## The KPIs to be calculated are:
1. Factor: purchase_price/annual_net_rent
2. Gross Return: annual_net_rent/purchase_price
3. Net Return: (annual_net_rent - management cost)/purchase_price
4. Equity Return: net_profit/equity_invested
5. Cash Flow: rent - (finance_cost + maintenance_costs )


## Input data:
1. net_rent: Amount that the renter pays to you on a monthly basis. It is the income that the property generates for you before costs.
2. purchase_price: Total price of the property.
3. loan_interest_rate: approx. lending interest rate.
4. loan_term_years: duration until complete repayment.
5. gross_rental_income_per_month:
6. energy_efficiency_class:
7. initial_repayment:
8. property_management:
9. maintenance cost:
10. insurance:
11. property_taxes: Property tax is part of the running costs of your property. As a landlord, you can pass the property tax on to your tenant.
12. location:

## Features
### Repayment plan showing the development of the following accounts:
- property
- rent
- costs
- credit
- interest and finance_cost
- repayment
- liquidity before taxes
