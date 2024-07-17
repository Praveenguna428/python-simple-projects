 a=input("Enter Your Password:")

sm,up,dg,sp=0,0,0,0

if(len(a)>7):

    for i in a:

        if(i.isupper()):

            up=up+1

        elif(i.islower()):

            sm=sm+1

        elif(i.isdigit()):

            dg=dg+1

        else:

            sp=sp+1

    if(up>0 and sm>0  and dg>0 and sp>0):

        print("Your Password is Storng")

    else:

        print("Your Password is Weak")

else:

    print("your Password must be contain atleast 8 characters")
