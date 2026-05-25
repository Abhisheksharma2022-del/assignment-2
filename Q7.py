academic_score = float(input("Enter academic score: "))
attendance = float(input("Enter attendance percentage: "))
extracurricular = input("Participated in extracurricular activities? (Yes/No): ")

if (
    academic_score >= 60 and
    attendance >= 75 and
    extracurricular.lower() == "yes"
):
    print("Eligible for Interview")

else:
    print("Not Eligible for Interview")