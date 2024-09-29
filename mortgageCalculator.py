def mortgage_calculator(principal, annual_interest_rate, years, monthly_hoa_fees, annual_property_tax):
    # Convert annual interest rate to a monthly rate
    monthly_interest_rate = annual_interest_rate / 100 / 12
    
    # Convert the loan term in years to the number of monthly payments
    number_of_payments = years * 12
    
    # Calculate the monthly payment using the formula for the loan
    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    
    # Convert annual property tax to a monthly amount
    monthly_property_tax = annual_property_tax / 12
    
    # Total monthly payment including HOA fees and property tax
    total_monthly_payment = monthly_payment + monthly_hoa_fees + monthly_property_tax
    
    return total_monthly_payment

# Example usage:
saleprice = float(input("what is the price of the property ")) #750000  
downpayment = float(input("what is the downpayment amount "))
principal_amount = saleprice - downpayment # The loan amount
print("The loan amount is "+ str(principal_amount))
interest_rate = float(input("what is the interest rate "))  # Annual interest rate as a percentage
loan_term = float(30)  # Term of the loan in years
hoa_fees = float(input("HOA if any? "))  # Monthly HOA fees
property_tax_rate = float(input("what is the property tax rate? 0.88% for old folsom, 1.33% for new folsom "))  # Annual property tax
property_tax = saleprice * property_tax_rate / 100
total_monthly_payment = mortgage_calculator(principal_amount, interest_rate, loan_term, hoa_fees, property_tax)
print(f"The total monthly mortgage payment, including HOA fees and property tax, is: ${total_monthly_payment:.2f}")