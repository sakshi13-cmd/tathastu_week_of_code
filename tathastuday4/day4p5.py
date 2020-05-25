noofvotes = int(input("enter the number of votes:"))
votes= []
for i in range(noofvotes):
    votes.append(input("enter the names of the candidates:"))
vote =[]
for name in votes:
    vote.append((name,votes.count(name)))
vote.sort(key = lambda x: x[0],reverse=True)
vote.sort(key = lambda x: x[1])
print("the name of candidates who won the election is" ,vote[-1][0])
    
    