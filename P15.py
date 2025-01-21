# leap year 
def leapyear(year):
    if (year%400==0 or (year%4==0 and year%100!=0)): #no.1 check year divisible both by 400 for centurian type then check not divisible by 100 but divisible by 4 for non century type year
        return "Yes"
    else:
        return "No"

print(leapyear(2004))  # Output: Yes
