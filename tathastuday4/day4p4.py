d={1:"r",2:"p",3:"a",4:"r"}
duplicate={}
for key, value in d.items():
    if value not in duplicate.values():
        duplicate[key]=value
print(duplicate)
        
    