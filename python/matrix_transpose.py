a= int(input("Enter the number of rows of Matrix:-"))
b= int(input("Enter the number of columns of Matrix:-"))
c=[]
for i in range(a):
    row=[]
    for j in range(b):
        d=int(input("Enter the number:-"))
        row.append(d)
    c.append(row)
print("The Transpose of the matrix is:-")
for i in range(b):
    for j in range(a):
        print(c[j][i],end="\t")
    print("")
