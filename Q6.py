age = int(input("Enter your age: "))
income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
debt = int(input("Enter outstanding debt: "))

if (
    age >= 18 and
    age <= 60 and
    income >= 25000 and
    credit_score >= 700 and
    debt <= 10000
):
    print("Loan Approved")

else:
    print("Loan Rejected")