a=input("Enter Your Passage:")

count=0

for i in range(len(a)):

    if(a[i]==' ' and a[i+1]!=' '):

        count=count+1

print("The Number of Word in the Sentence is ",count+1)

