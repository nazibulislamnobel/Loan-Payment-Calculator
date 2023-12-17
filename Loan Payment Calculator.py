loan_amount = float(input("Enter loan amount, for example 120000.95: "))
num_years = int(input("Enter number of years as an integer, for example 5: "))

monthly_interest_rate = 0.05  

print("{:<12} {:<15} {}".format("Interest Rate", "Monthly Payment", "Total Payment"))

while monthly_interest_rate <= 0.08:

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - 1 / (1 + monthly_interest_rate) ** (num_years * 12))

    total_payment = monthly_payment * num_years * 12

    print("{:.3%} {:<15.2f} {:.2f}".format(monthly_interest_rate, monthly_payment, total_payment))

    monthly_interest_rate += 1 / 800