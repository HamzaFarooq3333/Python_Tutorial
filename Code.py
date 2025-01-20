

a=300
b=3005

#Short hand if-else 
print('A') if a>b else  print('=') if a==b else print("B")

print('\n')

#We can make a new variable by using conditions on the previous result output 
#The syntax is      Result = value_if_true  if condition else value_if_false

c=4 if a>b else 7
print('Printing value of C determined by value of a and b : ',c)




print('\n')
def fun1(a):
    return a*a

def fun2(a):
    return a+a

print("A") if a>b else print(fun1(a)) if a==b else print(fun2(a)) 