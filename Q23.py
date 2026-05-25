start = input("Do you want to start game? (yes/no): ")

if start == "yes":
    score = 0
    correct = 0
    wrong = 0
    skipped = 0

    q1 = input("Q1: Capital of India? A/B/C/D or skip: ")
    if q1 == "A":
        score += 1000; correct += 1
    elif q1 == "skip":
        skipped += 1
    else:
        wrong += 1

    q2 = input("Q2: 2+2=? A/B/C/D or skip: ")
    if q2 == "B":
        score += 2000; correct += 1
    elif q2 == "skip":
        skipped += 1
    else:
        wrong += 1

    q3 = input("Q3: JS stands for? A/B/C/D or skip: ")
    if q3 == "B":
        score += 3000; correct += 1
    elif q3 == "skip":
        skipped += 1
    else:
        wrong += 1

    q4 = input("Q4: Sun rises in? A/B/C/D or skip: ")
    if q4 == "A":
        score += 5000; correct += 1
    elif q4 == "skip":
        skipped += 1
    else:
        wrong += 1

    q5 = input("Q5: India is in? A/B/C/D or skip: ")
    if q5 == "B":
        score += 10000; correct += 1
    elif q5 == "skip":
        skipped += 1
    else:
        wrong += 1

    print("Score:", score)
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Skipped:", skipped)

else:
    print("Game not started")