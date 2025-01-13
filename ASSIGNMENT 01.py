cp=int(input("Enter Cost Price:"))
sp=int(input("Enter Selling Price:"))
if(sp-cp>0):
    print("Your Profit is:",sp-cp)
elif(sp==cp):
    print("You dont have any pofit or loss(0)")
else:
    print("Your Loss is:",cp-sp)
