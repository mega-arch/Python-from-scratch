#to check each no. in a list is even or not
mylist=[1,2,3,4,5]
def evenornot(mylist):
    flag=False
    for i in range(len(mylist)):
        if mylist[i]%2==0:
            flag=True
            print(mylist[i],"is even")
        else:
            print(mylist[i],"is odd")

#to check entered num is prime or not
def primeornot(num):
    flag=False
    for i in range(1,num):
        if num%i==0:
            flag=True
    if flag:
         print("is prime")
    else:
            print("is not prime")

print("choice: 1.Check even or odd \n 2. Check prime or not")
match (int(input("Choice[1:2]:"))):
    case 1:
        evenornot(mylist)
    case 2:
        num=int(input("enter no.:"))
        primeornot(num)
    case _:
        print("try again")
