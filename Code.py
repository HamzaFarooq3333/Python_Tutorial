#Using string
a="1"
b="2"
print(a+b)
#Type Casting
print(int(a)+int(b))


#Using integers
a=1
b=2
print(a+b)


#Implicit type casting
a=2
b=3.1
print(a+b)  
#The python automatically converts the answer into float 


#Explicit type casting 
string ="15"
a=3
sum=int(string)  #Throws an error if the string is not a valid number
print("The sum is = ",a+sum)   