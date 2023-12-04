# User information
income = float(input("Enter your monthly income (₹): "))
expenses = float(input("Enter your monthly expenses (₹): "))
savings = income - expenses

# Investment rules
if savings > 500:
    print(f"\nYou have some savings to consider investing! (₹{savings:.2f})")
    investment_amount = float(input("How much would you like to invest (₹)? "))
    investment_formatted = f"{investment_amount:.2f}"

    # Risk tolerance options
    risk_tolerance = input(
        "Do you consider yourself risk-averse, neutral, or risk-tolerant? (a/n/r) "
    )

    if risk_tolerance == "a":
        print(
            "Low-risk options like government bonds or index funds might be suitable."
        )
    elif risk_tolerance == "n":
        print(
            "Balanced portfolios with moderate risk and potential for higher returns could be a good fit."
        )
    elif risk_tolerance == "r":
        print(
            "Individual stocks or high-growth investment opportunities might be appealing, but be mindful of potential losses."
        )

# Debt management rules
if expenses > income:
    print(
        f"\nYou're spending more than you earn! Consider debt management strategies:\n"
    )
    debt_amount = float(input("Enter your total debt amount (₹): "))
    debt_formatted = f"{debt_amount:.2f}"
    debt_interest_rate = float(input("Enter your average debt interest rate (%): "))
    debt_payment = float(input("How much can you allocate towards debt repayment each month (₹)? "))
    debt_payment_formatted = f"{debt_payment:.2f}"

    # Calculate and display payoff time
    payoff_time = debt_amount / debt_payment
    payoff_time_formatted = f"{payoff_time:.2f} months"
    print(f"Estimated debt payoff time with current payment: {payoff_time_formatted}")

    # Display debt pyramid chart
    print("Here's a visualization of your debt breakdown:")
    # Generate a simple debt pyramid chart using Python libraries like matplotlib or Plotly
    # ...

# Retirement planning rules
age = int(input("\nEnter your current age: "))
retirement_age = int(input("Enter your desired retirement age: "))

if age < retirement_age:
    print("Start saving for retirement early! Consider a pension plan or PPF.")
    retirement_goal = float(input("Enter your desired retirement savings goal (₹ in lakhs): "))
    years_to_save = retirement_age - age
    monthly_savings = (retirement_goal * 100000) / (years_to_save * 12)
    monthly_savings_formatted = f"{monthly_savings:.2f}"
    print(
        f"Estimated monthly savings needed: ₹{monthly_savings_formatted} to reach your goal."
    )

# Disclaimer
print(
    "\nThis is a simplified example. Always consult with a financial advisor for personalized guidance."
)

# Case 1
# Income (₹): 50,000
# Expenses (₹): 42,000
# Savings (₹): 8,000
# Investment amount (₹): 2,000
# Risk tolerance: "n" (Neutral)
# Debt amount (₹): 35,000
# Debt interest rate (%): 10.5%
# Debt payment (₹): 4,000
# Age: 30
# Desired retirement age: 65
# Retirement savings goal (₹ in lakhs): 75

# Case 2
# Income (₹): 38,000
# Expenses (₹): 45,000
# Savings (₹): -7,000 (Negative, indicating deficit)
# Investment amount (₹): 0 (Can't invest due to deficit)
# Risk tolerance: "n" (Neutral, but open to options to improve financial situation)
# Debt amount (₹): 15,000
# Debt interest rate (%): 8%
# Debt payment (₹): 2,000 (Struggling to make full payments)
# Age: 40
# Desired retirement age: 62
# Retirement savings goal (₹ in lakhs): 40 (Concerned about shortfall)
