n=int(input("Enter Integer:"))
flag=0
for i in range(2,n,1):
    if(n%i==0):
        flag=1
if(flag==1):
    print("NOT A PRIME!!")
else:
    print("PRIME!!")