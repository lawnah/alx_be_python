monthly_income = int(input("Enter your monthly income: "))

monthly_expenses = int(input("Enter your total monthly expenses"))

<<<<<<< HEAD
monthly_savings = income - expenses
=======
monthly_savings = monthly_income - monthly_expenses
>>>>>>> origin/main

projected_savings = (monthly_savings * 12) + (monthly_savings *12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")


print(f"Projected savings after one year, with interest, is: ${projected_savings}")
