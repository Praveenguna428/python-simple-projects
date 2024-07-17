a = int(input("Enter any Number:"))
count = 0
for i in range(2, a):
    if a % i == 0:
        count = count + 1
if count == 0:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")

