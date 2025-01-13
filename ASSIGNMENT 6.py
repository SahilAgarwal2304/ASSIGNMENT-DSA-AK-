flag="y"
while flag=="y":
    n1=int(input("Enter first no:"))
    n2=int(input("Enter second no:"))
    choice=int(input("Input 1.for adding 2. for subtraction 3.for Multiplication 4.for div"))
    if choice<5 and choice>0:
        if choice==1:
            print(n1+n2)
        elif choice==2:
            print(n1-n2)
        elif choice==3:
            print(n1*n2)
        else:
            if n2==0:
                print ("can't divde by zero")
            else:
                print(n1/n2)
    else:
        print("Please enter a valid choice")
    flag=input("Enter 'y' to continue or enter any other key to temrinate")
