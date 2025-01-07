# def calculateMean(a,b):
#   mean=(a*b)/(a+b)
#   print("The mean is = ",mean)


# def isGreater(a,b):
#   if(a>b):
#     print("First number is greater than the other ")
#   else:
#     print("Second number is greater than the other ")


# def isLess(a,b):
#   pass   #Ignore this and pass on the next code we will write this later it helps avoiding error 
#          # in case we did not define the function 

# c=int(input("Enter first number = "))
# d=int(input("Enter second number = "))
# calculateMean(c,d)
# isGreater(c,d)
# isLess(c,d)


#Methods to pass arguments to a function 

#Required arguments
def Average(a,b):
  print("The average is = ",(a+b)/2)
  
Average(2,5)

#Default Arguments
def defaultAverage(a=3,b=5):
  print("The average is = ",(a+b)/2)

defaultAverage()

#Keyword Arguments
def greeting(greeting ="Hello ",fname="Hamza",lname="Faroooq"):
  print(greeting+" "+fname+" "+lname)


greeting(lname="Ahmad",fname="Ali",greeting=
         "Assalamu Alaikum")



#Variable Arguments

#Arbitary Argument 
def arbitaryAverage(*numbers):
 print(type(numbers))
 sum =0
 for i in numbers:
   sum = sum + i
   print("The average is = ",sum/len(numbers))
  

arbitaryAverage(4,2,4,6,6,7)

#Arbitary keyword argument
def name(**names):
  print(type(names))
  print("Hello",names["fname"],names["lname"])


name(fname="Hamza",lname="farooq")