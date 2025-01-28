def WashingFuzzy():
    weight=int(input("Enter load weight: "))
    if weight==0:
        print("Time required to wash is 0")
    elif weight>7000:
        print("OVERLOADED")
    elif (weight>4000):
        print("Time estimated: 45 min")
    elif (weight>2000):
        print("Time estimated: 35 min")
    elif (weight>0):
        print("Time estimated: 25 min")
    else:
        print("Invalid input!")

def AddSub():
    a= int(input("Enter any integer:"))
    b= int(input("Enter any integer:"))

    if ((a+b)<0 ):
        print("Sum is:",-(a+b))
    else:
        print("Sum is:",a+b)
    if ((a-b)<0):
        print("Difference is:",-(a-b))
    else:
        print("Difference is:",a-b)
    

print("1. Washing machine fuzzy logic \n2. Add and Sub as absolute value\n")
choice=int(input("Enter choice[1:2]:"))
if choice==1:
    WashingFuzzy()
elif choice==2:
    AddSub()
else:
    print("Invalid choice!")



    
