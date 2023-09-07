def isLeapYear(year):  
  
  if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):  
    return True
  else:
    return False
    
year=2020
if isLeapYear(year):
    print("{} is a leap Year". format (year))  
else:  
    print ("{} is not a leap Year". format (year))