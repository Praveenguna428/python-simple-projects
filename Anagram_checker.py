a = input("Enter word 1: ").lower()
b = input("Enter word 2: ").lower()
a1 = sorted(a)
b1 = sorted(b)
if a1 == b1:
    print("The words {} and {} are  ANAGRAM....".format(a,b))
else:
    print("The word {} and {} are  NOT ANAGRAM....".format(a,b))
