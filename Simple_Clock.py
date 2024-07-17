import time

h,m,s=0,0,0

while(1):

    print(h,m,s)

    time.sleep(1)

    s=s+1

    if(s==60):

        m=m+1

        s=0

    elif(m==60):

        h=h+1

        m=0

        s=0

    elif(h==12):

        h,m,s=0,0,0
