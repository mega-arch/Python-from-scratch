import random # is a module that is a single file having functn and logic (a collection of module is a package)

def compare_float():
    a: int = float(input("enter float:"))
    b: int = float(input("enter float:"))
    print("the greatest among 2 is {:.3f}".format(max(a,b))) #:.3f used when we need 3 decimal places to right , .format() used to assign the result into the print statement

def sum_of_naturals():
    a: int = int(input("enter range:"))
    sum = 0
    for i in range(a+1):
        sum += i #the value if i will get stored in sum eg: i=1 then sum=0+1=1 for first iteration now sum=1
    print("sum of n naturals is:", sum)

def age_classify():
    a=int(input("enter age:"))
    if a>60:                       # going by the [0,60)method
        print("senior")   
    elif a>=13:
        print("teen")
    elif a>=20:
        print("adult") 
    elif a>=0:
        print("Child") 
    else:
        print("Invalid age!")

def rand_num():
    a = random.randint(1,100) #from random module we use randint() which generates random integer value in given range
    b = random.randint(1,100)
    print("sum of random is:", a + b)

def input_validation():
    try: #use for exception handling (to handle runtime error)
        a = float(input("enter a:"))
        b = float(input("enter b:"))
        print("sum is:", a+b)
    except ValueError: #ValueError is an built in exception class (occurs when invalid datatype is given as input)
        print("Invalid input. Ur input should be digits")

#menu driven program to access specific function 
print("choice: 1. compare float \n 2.sum of natural no. \n 3. age classify \n 4.sum of 2 random no. \n 5. Input validate")

match int(input("Choice[1,5]:")):
    case 1:
        compare_float()
    case 2:
        sum_of_naturals()
    case 3:
        age_classify()
    case 4:
        rand_num()
    case 5:
        input_validation()
    case _:
        print("invalid choice")
