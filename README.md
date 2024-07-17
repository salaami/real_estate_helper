# Real Estate Helpe# Real Estate Helper

## To evaluate offers found on the internet, I am writing a simple Python app that calculates the relevant KPIs from a simple YAML file. For the time being, the process is supposed to look as follows:
1. Find an offer online.
2. Identify the data in the offer.
3. Fill the YAML file with the according data.
4. Run the program.

## The KPIs to be calculated are:
1. Gross Return: Jahresnettokaltmiete / Kaufpreis des Objekts * 100
2. Net Return: Jahresreinertrag / Investitionskosten x 100

## Input data:
1. gross_rental_income_per_month: Amount that the renter pays to you on a monthly basis in €.
2. energy_efficiency_class: Ranges from A - G.
3. build_at: Date when the property was built in format YYYY-MM-DD.
4. last_renovated: Date of last renovation or modernization in format YYYY-MM-DD.
5. location: City and district of the object as text.
6. Purchase details:
   1. price: Total price of the property in €. Doesn't include additional purchase costs.
   2. agent_costs: Cost claimed by real estate agents.
   3. notary_costs: Costs claimed by the notary for paperwork.
   4. property_registry_costs: Cost for entering a new record into the property registry.
7. taxes:
   1. property_transfer: Property tax is part of the running costs of your property. As a landlord, you can pass the property tax on to your tenant in €.
8. operating_expenses:
   1. property_management: Costs for tenant management, rent collection, and other costs for management, etc., in €.
   2. maintenance_cost: Cost for upkeep and repair of the property in €.
   3. insurance: e.g., property and landowner liability insurance cost in €.
9. loan_term_years: Duration until complete repayment in years.
10. down_payment: Initial repayment as a share of purchase_price.
11. loan_interest_rate: Approx. lending interest rate.

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
- Introduce configuration checks for input plausibility.
### Better output format than stdout
- Export to a file
- Visualize in a file
- Visualize in an app like Flask
