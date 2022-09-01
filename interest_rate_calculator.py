# collect the necesary inputs: principal, apr, years
# calculate the monthly payment
# show results to user

def main():
    print("This Is A Monthly Loan Payment Calculator")
    print(" ")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input number of years: "))
    
    monthly_interest_rate = apr / 1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))
    
    print("The mnontly payment for this loan is: %.2f " % monthly_payment)
    
main()