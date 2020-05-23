#armstrong  number
num=int(input("enter the number:"))
reverse=0
a=num
while (num>0):
    digit = num%10
    reverse = reverse + (digit**3)
    num=num//10
if(a==reverse):
    print('the number is armstrong:')
else:
    print('the number is not armstrong:')
    
    
    
    
