# Find n power of a number
def power(base,exp):
    i=1 #used to keep the while loop going 
    res=1
    while i<=exp: #until i is less or equal to exp value the condition is true and loop executes 
        res=res*base # base is constant but for each power increment the value changes 
        i+=1
    return res

print(power(2,3))  # Output: 8
