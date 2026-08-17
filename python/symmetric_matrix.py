a= int(input("Enter the number of rows of Matrix:-"))
b= int(input("Enter the number of columns of Matrix:-"))
c=[]
for i in range(a):
    row=[]
    for j in range(b):
        d=int(input("Enter the number:-"))
        row.append(d)
    c.append(row)
if a!=b:
    print ("It is not a square matrix.")
else:
    count=0
    for i in range(a):
        for j in range(b):
            if (c[i][j]!=c[j][i]):
                count=1
                break
    if(count==1):
        print("This is not a symmetric matrix.")
    else:
        print("This is a symmetric matrix.")
for i in range(a):
    for j in range(b):
        print(c[i][j],end="\t")
    print("")
