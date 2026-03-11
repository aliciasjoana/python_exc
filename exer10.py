n1 = int(input())
n2 = int(input())
while (n1!=n2):
    if(n1<n2):
        n1+=1
        if (n1 == n2):
            break
        print(n1)
    elif (n2<n1):
         n2+=1
         if (n1 == n2):
            break
         print(n2)
