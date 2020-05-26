#knapsack problem
def knapsack(weight, List):
    if weight == 0 or len(List)==0:
        return 0
    if len(List)==1:
        if (List[0][0] > weight):
            return 0
        return List[0][1]
    if List[0][0]> weight:
        return knapsack((weight, List[1:]))
    return max (List[0][1]+ knapsack(weight - List[0][0], List[1:]), knapsack(weight, List[1:]))
size = int(input("enter the number of items you want to enter:"))
List=[]
for i in range(size):
    weight = int(input("enter the weight of item number"+ str(i+1)))
    value = int(input("enter the value of item number"+ str(i+1)))
    List.append((weight, value))
weight = int(input("enter the  value of weight capacity:"))
print("the maximum value for given weight value pair is ",knapsack(weight, List))

    
    
    
