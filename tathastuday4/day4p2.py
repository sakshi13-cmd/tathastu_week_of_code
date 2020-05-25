size_list =int(input("enter the number of tuples:"))
size_tuple =int(input("enter the number of elements you want to add in the tupple:"))
List=[]
for i in range (size_list):
    print("enter the elements in tuple", i+1)
    Tuple=[]
    for j in range (size_tuple):
        Tuple.append(int(input("enter the elements" +str(j+1) + ":")))
    List.append(tuple(Tuple))
n= int(input("enter the nth index about which you want to sort in list:"))
List.sort(key = lambda x: x[n])
print("after sorting :", List)