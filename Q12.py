exp = int(input("Enter years of experience: "))

if exp >= 10:
    print("Senior employee")
    salary = 80000

    if exp > 15:
        print("Experience exceeds 15 years. Bonus added.")
        salary += 5000

elif exp >= 5:
    print("Mid-level employee")
    salary = 50000

else:
    print("Junior employee")
    salary = 30000

print("Salary:", salary)