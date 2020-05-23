n=int(input("enter a value:"))
for i in range(n):
    print((str(n-i) + "*") * (n-1-i) + str(n-i))
for j in range(2,n+1):
    print((str(j) + "*") * (j-1) + str(j))
