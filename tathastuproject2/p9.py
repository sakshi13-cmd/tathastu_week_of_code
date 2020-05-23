#palindrome number
num=int(input("enter the number:"))
rev=0
a=num
while (num>0):
    rev = (rev*10)+(num%10)
    num=num//10
if (rev==a):
    print("the number is palindrome:")
else:
    print("the number is  not palindrome:")