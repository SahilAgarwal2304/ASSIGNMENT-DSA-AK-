sum = 0
temp = 0
n = int(input("Enter the number of subjects: "))
for i in range(n):
    marks = int(input(f"Enter marks for subject {i + 1}: "))
    if marks > 100 or marks < 0:
        print("Enter valid marks!")
        i -= 1
        continue
    if marks < 40:
        temp = 1
    sum += marks
if temp == 0:
    percent = sum / n
    print("Your Percentage =", percent)
    if percent < 40:
        print("FAIL")
    elif percent < 60:
        print("PASS - III Div.")
    elif percent < 80:
        print("PASS - II Div.")
    elif percent <= 100:
        print("PASS - I Div.")
else:
    print("FAIL")
