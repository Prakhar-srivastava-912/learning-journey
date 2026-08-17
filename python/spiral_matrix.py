a= int(input("Enter the number of rows of Matrix:-"))
b= int(input("Enter the number of columns of Matrix:-"))
c=[]
for i in range(a):
    row=[]
    for j in range(b):
        d=int(input("Enter the number:-"))
        row.append(d)
    c.append(row)
for i in range(a):
        for j in range(b):
            print(c[i][j],end="\t")
        print("")
top = 0
bottom = a - 1
left = 0
right = b - 1
print("Spiral order:")
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        print(c[top][j], end=" ")
    top += 1
    for i in range(top, bottom + 1):
        print(c[i][right], end=" ")
    right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(c[bottom][j], end=" ")
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(c[i][left], end=" ")
        left += 1
