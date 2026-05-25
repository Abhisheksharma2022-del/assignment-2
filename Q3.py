age = int(input("Enter your age: "))

retirement_age = 65

if age < retirement_age:
    years_left = retirement_age - age
    print("Years left for retirement =", years_left)

else:
    print("You have already reached retirement age.")