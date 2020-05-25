#occurence of elements in tuple
print("enter the numbers you want to print separated by commmas:")
t1 = tuple ([int(e) for e in input ().split(',')])
i=0
for e in t1:
    if (i == t1.index(e)):
        print(e , ' - ',t1.count(e))
    i+=1