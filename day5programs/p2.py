def gretestinteger(List):
    for i in range(size-1):
        List[i] = max(List[i+1:])
    return List
size=int(input("enter the size of the list:"))
List = []
for i in range(size):
    List.append(int(input("enter the element number:"+str(i+1)+ "in the list")))
print("the list after replacing is:", gretestinteger(List))