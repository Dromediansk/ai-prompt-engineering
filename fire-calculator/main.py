# Step 1: Prompt the user for their current age
current_age = int(input("Enter your current age: "))

# Step 2: Prompt the user for their average annual expenses
monthly_expenses = float(input("Enter your average monthly expenses (in €): "))
annual_expenses = monthly_expenses * 12

# Step 3: Calculate the FIRE number (source: Playing with FIRE by Scott Rieckens)
fire_number = annual_expenses * 25

# Step 4: Prompt the user for their net monthly income
monthly_income = float(input("Enter your net monthly income (in €): "))

# Step 5: Calculate the annual savings
annual_savings = (monthly_income * 12) - annual_expenses

# New Step: Prompt the user for their current net worth
current_net_worth = float(input("Enter your current net worth: "))

# Initialize variables with current net worth considered
total_savings = current_net_worth
annual_interest_rate = 0.08
years = 0

# Step 6: Calculate the years to retirement considering a 7% annual interest rate and current net worth
while total_savings < fire_number:
  total_savings += annual_savings + (total_savings * annual_interest_rate)
  years += 1

# Step 7: Calculate the retirement age considering the interest and current net worth
retirement_age = current_age + years

# Step 8: Display the updated FIRE number and potential retirement age with interest considered
print(f"To achieve financial independence and retire early, you need a savings of: €{fire_number}")
print(f"Considering your current net worth and an annual interest rate of {annual_interest_rate * 100:.2f}%, you could potentially retire at age: {retirement_age}")