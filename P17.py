#to check each no. in a list is even or not
mylist=[1,2,3,4,5]
def evenornot(mylist):
    flag=False #keeps the initial state of flag indicator as false(boolean value 0)
    for i in range(len(mylist)):
        if mylist[i]%2==0: #if the element from list in ith index is divisible by 2
            flag=True #indicator is turned on detecting even num
            print(mylist[i],"is even")
        else:
            print(mylist[i],"is odd")

#to check entered num is prime or not
def primeornot(num):
    flag=False
    for i in range(1,num):
        if num%i==0: #input no. is checked in each iteration which divides previous of it as digits> input value can't divide and will be less than 0
            flag=True #if any natural no. be4 the num divides it flag is on
    if flag: # executes when flag is true (conditional if statement execute when it is true)
         print("is prime")
    else:
            print("is not prime")

print("choice: 1.Check even or odd \n 2. Check prime or not")
match (int(input("Choice[1:2]:"))): #like switch case
    case 1:
        evenornot(mylist)
    case 2:
        num=int(input("enter no.:"))
        primeornot(num)
    case _:
        print("try again")
