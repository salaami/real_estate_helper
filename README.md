# Real Estate Helper

## To evaluate offers found on the internet, I am writing a simple Python app that calculates the relevant KPIs from a simple yml file. For the time being the process is supposed to look as follows:
1. Find an offer online.
2. Identify the data in the offer.
3. Fill the yaml file with the according data.
4. Run the program.

## The KPIs to be calculated are:
1. Gross Return: annual_net_rent/purchase_price
2. Net Return: (annual_net_rent - management cost)/purchase_price
3. Equity Return: net_profit/equity_invested
4. Cash Flow: rent - (finance_cost + maintenance_costs )

## Input data:
1. purchase_price: Total price of the property in €.
2. gross_rental_income_per_month: Amount that the renter pays to you on a monthly basis in €.
3. energy_efficiency_class: Ranges from A - G.
4. last_renovated: date of last renovation or modernization in format YYYY-MM-DD.
5. location: City and district of the object as text.
6. loan_term_years: duration until complete repayment in years.
7. down_payment: initial repayment as share of purchase_price.
8. loan_interest_rate: approx. lending interest rate.
9. property_management: costs for tenant management, rent collection, and other costs for the management etc. in €.
10. maintenance cost: cost for upkeep and repair of the property in €.
11. insurance: building or loss-of-rent insurance cost in €.
12. property_taxes: Property tax is part of the running costs of your property. As a landlord, you can pass the property tax on to your tenant in €.

## Features
### Repayment plan showing the development of the following accounts:
- property
- rent
- costs
- credit
- interest and finance_cost
- repayment
- liquidity before taxes
### Improve data input
- Introduce a configuration that checks the data inputs on plausibility.
### Better output format then stdout
- Export to a file
- Visualize in a files
- Visualize in an app like flask
