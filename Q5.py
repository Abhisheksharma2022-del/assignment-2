base_salary = 50000
bonus = 5000
other_charges = 2000
tax_rate = 10

gross_salary = base_salary + bonus

tax = (gross_salary * tax_rate) / 100

net_salary = gross_salary - tax - other_charges

print("Gross Salary =", gross_salary)
print("Tax =", tax)
print("Net Salary =", net_salary)