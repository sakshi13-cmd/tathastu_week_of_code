string=str(input("enter a string:"))
duplicate=[]
for i in string:
    if i not in duplicate:
        duplicate.append(i)
duplicate=(''.join(duplicate))
print(duplicate)