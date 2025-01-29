
#Importing math library
import math

print(math.sqrt(9))



#Importing only sqrt function and pi of math library 
from math import sqrt,pi


print("Square root of 25 is :" ,sqrt(25))



#Importing everyhing from a library
from math import *  #All functions of the math library have been made available in the script as public
                    #This method is not recommended becasue it can lead to confusion in the program 



#Using as keyword 
import pandas as pd   #Now we can use functions of pandas by simply writing pd instead of pandas
print("The details of the array is : ",pd.array([3,5]))
print('\n')


#Using dir
import pandas
print('Printing functions in pandas module')
print(dir(pandas))

print('\n')
print("The type of the function is : ",type(pandas.array([4,5])))
print('\n')


#Importing functions from other python file
import demo as dm
dm.welcome()
print(dm.greeing)
