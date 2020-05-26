def sortEvenOdd(List):
    odd=[]
    even=[]
    for x in List:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return sorted(odd,reverse=True)
size = int(input("enter the number of elements :"))
List = []
for i in range(size):
    List.append(int(input("enter the element number" +str(i+1) + "in the list:")))
print("the list of numbers after sorting is", str(sortEvenOdd(List))[1:-1])