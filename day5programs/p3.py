def House(List):
    if len(List)==2:
        return max(List)
    if len(List)==1:
        return List[0]
    if len(List)==3:
        return max(List[1],List[0]+House(List[2:]))
    return max(List[1] +House(List[3:]),List[0]+House(List[2:]))
size=int(input("enter the number of house in list"))
List = []
for i in range(size):
    List.append(int(input("enter the value of the house:"+str(i+1)+ "in the list")))
print("the  max stolen value from house", House(List))