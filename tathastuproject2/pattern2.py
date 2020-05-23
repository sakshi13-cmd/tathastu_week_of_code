n=int(input("enter the value:"))
for i in range(n,0,-1):
    print("*"*i +"  "*(n-i) +i * "*")
for j in range(2,n+1):
    print("*"*j + "  "*(n-j) +j * "*")
