import yaml
import math
import os

class RealEstateEvaluator:
    def __init__(self, yaml_file='config/property_data.yaml'):
        self.data = self.read_yaml(yaml_file)
        self.extract_data()

    def read_yaml(self, file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def extract_data(self):
        property_data = self.data['property']
        self.purchase_price = property_data['purchase_price']
        self.down_payment = property_data['loan_details']['down_payment']
        self.loan_interest_rate = property_data['loan_details']['loan_interest_rate']
        self.loan_term_years = property_data['loan_details']['loan_term_years']
        self.gross_rental_income_per_month = property_data['gross_rental_income_per_month']
        self.operating_expenses_per_month = sum(property_data['operating_expenses_per_month'].values())

    def calculate_gross_return(self):
        gross_rental_income_per_year = (self.gross_rental_income_per_month ) * 12
        return gross_rental_income_per_year / self.purchase_price * 100

    def calculate_noi(self):
        gross_income_per_year = (self.gross_rental_income_per_month ) * 12
        operating_expenses_per_year = self.operating_expenses_per_month * 12
        return gross_income_per_year - operating_expenses_per_year

    def calculate_cash_flow(self, noi):
        loan_amount = self.purchase_price - self.down_payment
        monthly_interest_rate = self.loan_interest_rate / 12
        number_of_payments = self.loan_term_years * 12
        mortgage_payment = loan_amount * monthly_interest_rate / (1 - math.pow(1 + monthly_interest_rate, -number_of_payments))
        annual_debt_service = mortgage_payment * 12
        return noi - annual_debt_service

    def calculate_cap_rate(self, noi):
        return (noi / self.purchase_price) * 100

    def calculate_roi(self, cash_flow):
        total_investment = self.down_payment + (self.operating_expenses_per_month * 12 * self.loan_term_years)
        return (cash_flow / total_investment) * 100

    def calculate_grm(self):
        return self.purchase_price / (self.gross_rental_income_per_month * 12)

    def evaluate(self):
        gross_return = self.calculate_gross_return()
        noi = self.calculate_noi()
        cash_flow = self.calculate_cash_flow(noi)
        cap_rate = self.calculate_cap_rate(noi)
        roi = self.calculate_roi(cash_flow)
        grm = self.calculate_grm()

        results = {
            "Gross Return": f"{gross_return:.2f}%",
            "Net Operating Income": f"${noi:.2f}",
            "Cash Flow": f"${cash_flow:.2f}",
            "Cap Rate": f"{cap_rate:.2f}%",
            "Return on Investment": f"{roi:.2f}%",
            "Gross Rent Multiplier": f"{grm:.2f}"
        }

        return results

def main(yaml_file='config/property_data.yaml'):
    evaluator = RealEstateEvaluator(yaml_file)
    results = evaluator.evaluate()

    for kpi, value in results.items():
        print(f"{kpi}: {value}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Real Estate Evaluator")
    parser.add_argument('-c', '--config', type=str, default='config/property_data.yaml', help='Path to the YAML configuration file')
    args = parser.parse_args()
    main(args.config)

