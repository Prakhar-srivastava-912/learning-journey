a= int(input("Enter the number of rows of Matrix1:-"))
b= int(input("Enter the number of columns of Matrix1:-"))
c=[]
for i in range(a):
    row=[]
    for j in range(b):
        d=int(input("Enter the number:-"))
        row.append(d)
    c.append(row)
l= int(input("Enter the number of rows of Matrix2:-"))
e= int(input("Enter the number of columns of Matrix2:-"))
f=[]
for i in range(l):
    row=[]
    for j in range(e):
        d=int(input("Enter the number:-"))
        row.append(d)
    f.append(row)
new = []
if b != l:
    print("Multiplication is not possible")
else:
    for i in range(a):
        row = []
        for j in range(e):
            k = 0
            for m in range(b):
                k += c[i][m] * f[m][j]
            row.append(k)
        new.append(row)
    for i in range(a):
        for j in range(e):
            print(new[i][j],end="\t")
        print("")
