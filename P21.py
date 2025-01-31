#vowel=["a","e","i","o","u"]
#abc=[]

#match "hello".split() :
#    for i in range(6):
#        if a[i] in vowel:
#            print(a[i])

#        case "a":

#infinite looping
#import random
#def random_gen():
#    return random.randint(1,5)
def infinite_for(): 
    for i in iter(int,1): #int func always returns 0 thus iter() keeps iterating till it meets the given condition (1).Here int always give 0 as we haven't given any no. to turn that into int hence by default it takes as 0, thus forms infinite loop.
        print("Hi")

#for _ in itertools.count() is another approach where count() by default takes start=0 and increament=1.

def infinite_while():
    i=1
    while(True): #while executes infinite as long as the condition is satisfied.If any condition is not satisfied it will exit from the loop
        print(i)
        i+=1

def perfect_num():
    num=int(input("Enter the no.:"))
    sum=0
    for i in range(1,num): #range from 1 to given num when we sum there factors if the value is equal to the orginal num then it is a perfect num
        if num%i==0: #to get the factors 
            sum=sum+i #adding them to sum 
    print("The sum is:",sum)
    if sum==num:
        print("It is a perfect no.")
    else:
        print("Not a perfect no.")

from collections import Counter #collections module used to deal with collection datatypes like set,list,dict,tuple
def count_arr_element():
    num=input("Enter array elements:")
    arr= list(map(int,num.split())) #takes the input as list easy to iterate #map()used to convert the value into int ,split() used to seperate each value into single element, list() used to store these individual into list
    count=Counter(arr) #Counter() is used to count the number of elements in list
    for i in range(len(arr)+1):
        if count[i]==1:
            print(i,"is the single time present element in array")

def sentence_palindrome():
    sentence=input("Enter sentence: ")
    sen= "" #empty string so that we can append the char
    for i in sentence:
        if i.isalnum(): #checks if the char is alphanumeric 
            sen=sen+i.lower() #gets that char and converts into lowercase for case ignorance
    print("Cleaned sentence:",sen)
    rev= sen[::-1] #reverses the char collected in sen 
    print("rev is:",rev)
    if rev==sen:
        print(sentence,"is a palindrom")
    else:
        print("not a palindrome")

def fizz_buzz():
    n=int(input("Enter num:"))
    for i in range(n+1): #including the input itself
        if i%3==0 and i%5==0: #checks if div both by 3 & 5 (better to write first as python is an interpreted lang.)
            print("FizzBuzz")
        elif i%5==0: #checks if div only by 5
            print("Buzz")
        elif i%3==0: #checks if div only by 3
            print("Fizz")
        else:
            print(i) #none condition satisfied it prints the num

from datetime import datetime #built in module we import class
def date_day():
    inp= input("Enter the day:")
    formatted_inp=datetime.strptime(inp,"%Y-%m-%d") #strptime is a function in datetime class used to format or convert the input string nto datetime format. %Y for year, %m for month,%M for minutes, %d for date
    print(formatted_inp.day) #.day function is used to extract and print only the %d part 


print("1.Infinite for loop\n2.Infinite while loop\n3.perfect num\n4.count arr\n5.sentence palindrome\n6.Fizz buzz\n7.Date format\n")
match int(input("Enter choice[1:]: \n")):
    case 1:
        infinite_for()
    case 2:
        infinite_while()
    case 3:
        perfect_num()
    case 4:
        count_arr_element()
    case 5:
        sentence_palindrome()
    case 6:
        fizz_buzz()
    case 7:
        date_day()










