sum=0
temp=0
for i in range (5):
    marks=int(input("Enter marks:"))
    if marks>100 or marks<0:
        print("Enter valid marks!")
        i-=1
    if marks<40:
        temp=1
    sum+=marks
if temp==0:
    percent=sum/5
    print("Your Percentage=",percent)
    if percent<40:
        print("FAIL")
    elif percent<60:
        print("PASS-iii.Div")
    elif percent<80:
        print("PASS-ii.Div")
    elif percent<100:
        print("PASS-i.Div")
    else:
        print("Enter Valid Marks")
else:
    print("FAIL")