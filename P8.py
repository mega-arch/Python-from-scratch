# n natural no. in reverse
def rev(n):
    while (n>=1): # executes until the n is not equal or less than 1
        print(n,end=" ") #end used to seperate output in single line 
        n-=1 # decreament
rev(10)  # Output: 10 9 8 7 6 5 4 3 2 1 
