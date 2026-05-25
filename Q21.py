age = int(input("Enter age: "))
graduate = input("Are you graduate? (yes/no): ")
nationality = input("Enter nationality: ")

if 21 <= age <= 32 and graduate == "yes" and nationality == "Indian":
    print("Eligible for UPSC")

    prelims = int(input("Prelims score: "))
    if prelims >= 100:
        print("Passed Prelims")

        mains = int(input("Mains score: "))
        if mains >= 100:
            print("Passed Mains")

            interview = int(input("Interview score: "))
            if interview >= 100:
                print("UPSC Cleared")
            else:
                print("Failed Interview")
        else:
            print("Failed Mains")
    else:
        print("Failed Prelims")
else:
    print("Not eligible")