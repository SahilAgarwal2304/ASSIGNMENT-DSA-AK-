m = int(input("Enter the number of students: "))
n = int(input("Enter the number of subjects: "))
for s in range(1, m + 1):
    print("\nEntering marks for Student", s, ":")
    total = 0
    fails = 0
    for sub in range(1, n + 1):
        marks = int(input("Enter marks for Subject " + str(sub) + ": "))
        if marks > 100 or marks < 0:
            print("Enter valid marks!")
            sub -= 1
            continue
        if marks < 40:
            fails += 1
        total += marks
    if fails > 0:
        print("Student", s, "FAIL")
    else:
        percent = total / n
        print("Student", s, "Percentage =", percent, "%")
        if percent < 40:
            print("FAIL")
        elif percent < 60:
            print("PASS - III Div.")
        elif percent < 80:
            print("PASS - II Div.")
        else:
            print("PASS - I Div.")
