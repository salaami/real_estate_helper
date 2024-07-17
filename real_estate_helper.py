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
        self.purchase_price = property_data['purchase_details']['price']
        self.absolute_property_transfer_tax =  property_data['purchase_details']['price'] *  property_data['taxes']['property_transfer']
        self.investment_cost = sum(property_data['purchase_details'].values()) + self.absolute_property_transfer_tax
        self.down_payment = property_data['loan_details']['down_payment']
        self.loan_interest_rate = property_data['loan_details']['loan_interest_rate']
        self.loan_term_years = property_data['loan_details']['loan_term_years']
        self.gross_rental_income_per_month = property_data['gross_rental_income_per_month']
        self.operating_expenses_per_year = sum(property_data['operating_expenses_per_month'].values()) * 12
        self.gross_rental_income_per_year = self.gross_rental_income_per_month * 12


    def calculate_gross_return(self):
        return self.gross_rental_income_per_year / self.purchase_price * 100

    def calculate_net_return(self):
        net_rental_income_per_year = self.gross_rental_income_per_year - self.operating_expenses_per_year
        return net_rental_income_per_year / self.investment_cost * 100

    def evaluate(self):
        gross_return = self.calculate_gross_return()
        net_return = self.calculate_net_return()

        results = {
            "Gross Return": f"{gross_return:.2f}%",
            "Net Return": f"{net_return:.2f}%",
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

