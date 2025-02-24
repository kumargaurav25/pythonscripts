def calculate_mortgage(principal, annual_interest_rate, years):
    """
    Calculate the monthly mortgage payment (principal & interest only).

    :param principal: Loan amount (in dollars)
    :param annual_interest_rate: Annual interest rate (as a percentage, e.g., 5 for 5%)
    :param years: Loan term (in years)
    :return: Monthly mortgage payment
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    num_payments = years * 12

    if monthly_interest_rate == 0:
        return principal / num_payments  # Handle zero interest rate case

    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_payment


def calculate_property_tax(home_value, tax_rate):
    """
    Calculate monthly property tax.

    :param home_value: Total home value
    :param tax_rate: Property tax rate (as a percentage, e.g., 1.25 for 1.25%)
    :return: Monthly property tax amount
    """
    annual_tax = (tax_rate / 100) * home_value
    return annual_tax / 12  # Convert to monthly


def calculate_pmi(loan_amount, sale_price):
    """
    Calculate Private Mortgage Insurance (PMI).

    :param loan_amount: Amount borrowed
    :param sale_price: Total home purchase price
    :return: Monthly PMI cost
    """
    down_payment_percent = ((sale_price - loan_amount) / sale_price) * 100
    if down_payment_percent >= 20:
        return 0  # No PMI if down payment is 20% or more

    pmi_rate = 0.005  # Typical PMI rate (0.5% annually)
    annual_pmi = pmi_rate * loan_amount
    return annual_pmi / 12  # Convert to monthly


# Example usage:
if __name__ == "__main__":
    sale_price = float(input("Enter the home sale price: "))
    down_payment = float(input("Enter your down payment amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term (in years): "))
    property_tax_rate = float(input("Enter the annual property tax rate (in %): "))
    mello_roos = float(input("Enter the monthly Mello-Roos tax amount: "))
    hoa_fee = float(input("Enter the monthly HOA fee: "))

    # Calculate loan amount
    loan_amount = sale_price - down_payment

    # Calculate costs
    monthly_mortgage = calculate_mortgage(loan_amount, annual_interest_rate, years)
    monthly_property_tax = calculate_property_tax(sale_price, property_tax_rate)
    monthly_pmi = calculate_pmi(loan_amount, sale_price)

    total_monthly_payment = monthly_mortgage + monthly_property_tax + mello_roos + hoa_fee + monthly_pmi

    print("\n==== Mortgage Payment Breakdown ====")
    print(f"Sale Price: ${sale_price:,.2f}")
    print(f"Down Payment: ${down_payment:,.2f}")
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Monthly Mortgage Payment (Principal & Interest): ${monthly_mortgage:.2f}")
    print(f"Monthly Property Tax: ${monthly_property_tax:.2f}")
    print(f"Monthly Mello-Roos Tax: ${mello_roos:.2f}")
    print(f"Monthly HOA Fee: ${hoa_fee:.2f}")
    print(f"Monthly PMI (if applicable): ${monthly_pmi:.2f}")
    print(f"Total Monthly Payment: ${total_monthly_payment:.2f}")