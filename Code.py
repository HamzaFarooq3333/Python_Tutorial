#Doc-string

def square(a):    #The docstring should be defined before function body otherwise we will get nothing 
    '''Takes in a number and returns the square of that number '''
    print(a*a)
  

square(5)
print(square.__doc__) #Displays the docstring we wrote in a function in  python 

import this  #Pep 8 (Python Enhancement Proposal)