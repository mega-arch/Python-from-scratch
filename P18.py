name=input("enter name:").strip()
rev=[] #empty list
a=-1 #intial index is -1 (last element)
for i in range(len(name)):
    rev.append(name[a]) #appends last element to list
    a=a-1 #decrements value of a
print(''.join(rev)) #converts to string 