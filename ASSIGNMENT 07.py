lst = []
print("Enter 3 nos:")
for i in range(3):
    ele = int(input())
    lst.append(ele)

max_val = lst[0]

for num in lst:
    if num > max_val:
        max_val = num

print("The maximum number is:", max_val)
