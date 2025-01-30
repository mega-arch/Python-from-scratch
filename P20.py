
#boolean way of determining a no. as prime or not
def is_prime(n):
    for i in range(2,int(n**0.5)+1): #root of a no. is enough to check prime no. since after that we cannot fully divide the no.Intial vslue is 2 as 0,1 are not prime. +1 to include the last value too.
        if n%i==0: #checks in each iteration whether the entered num is divible by i in each iterartion
            return False #if divides then its not a prime as a prime can have 2 factors only 
    return True #if no value in this range div the no. then it has exactly 2 factors thus its a prime no.


#to check palindrome of a string
def palindrom():
    rev=""
    for i in range(len(n)):
        rev=n[::-1] #string cannot support i-=1 thus we need slicing to append the last value into fresh string rev
    if rev.casefold()==n.casefold(): #checks by ignoring case 
        print( "Palindrome")
    else:
        print("not a palindrom")


#divisible by 27 evenly or not
def Evenly_divisible():
    num=int(input("enter num: "))
    if num%27==0: #while dividing a no. with 27 leaves no reminder then it is divisible
        print("is evenly divisble by 27")
    else:
        print("not divisible")


#to do proper arithmetic operation when theres no rule how to sub a no.
def sum_diff_without_negative_value():
    num1=int(input("Enter num 1:"))
    num2=int(input("Enter num 2:"))
    if (num1<num2): #if a<b then a-b will give -ve value 
        print("Addition is:",num2+num1)
        print("Subtraction is:",num2-num1)
    else:
        print("Addition is:",num1+num2)
        print("Subtraction is:",num1-num2)


#You have four secret numbers and your challenge is to write a program that figures 
#out which one is the largest and which one is the smallest. Use your trusty if-else 
#statements to solve this number mystery. Can you determine the highest and lowest 
#numbers among them?
def big_among_4_num():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    n3=int(input("Enter n3:"))
    n4=int(input("Enter n4:"))
    if (n1>n2 and n1>n3 and n1>n4): #can check multiple conditions using logical operators if all condition is satisfied it will print the true statement
        print(n1,"is big")
    elif (n2>n1 and n2>n3 and n2>n4):
        print(n2,"is big")
    elif (n3>n1 and n3>n2 and n3>n4):
        print(n3,"is big")
    elif (n4>n1 and n4>n3 and n4>n2):
        print(n4,"is big")
    else:
        print("All are equal")

print("1. Boolean logic to check prime or not\n2. Check palindrome of a string\n3. divisible by 27 evenly or not\n4. Subtraction of no. that returns non -ve\n5. Greatest among 4 num\n")
choice=int(input("Enter choice[1:5]:"))
if choice==1:
    n=int(input("enter no: "))
    print(n,"is prime:",is_prime(n))
elif choice==2:
    n=input("enter string: ")
    palindrom()
elif choice==3:
    Evenly_divisible()
elif choice==4:
    sum_diff_without_negative_value()
elif choice==5:
    sum_diff_without_negative_value()
else:
    print("Invalid choice!")


