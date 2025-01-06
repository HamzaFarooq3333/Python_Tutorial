a=int(input("Enter the value of number = "))


match a:
    case 0:
        print("The number is zero")
    case 1:
        print("The number is 1")
    case 2:
        print("The number is 2")
    case _ if(a<10 and a>0):
        print("The number is less than ten")
    case _ if(a>10 and a<20):
        print("The number is less than twenty and greater than ten ")
    case _ if(a>=20 ) :    
        print("The number is greater than or equal to twenty")
    case _:
        print("The number is less than zero")
#We have set 3 default cases using if statement but elif and else cannot be used in this case 

a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))


print("Choose one of the following numbers for the action ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

option=int(input("Enter the command you want to perform = "))

match option:
    case 1:
        print("The sum of the two numbers is ", a+b)
    case 2:
        print("The difference of the two numbers is ", a-b)
    case 3:
        print("The product of the two numbers is ", a*b)
    case 4:
        print("The quotient of the two numbers is ", a/b)
    case _:
        print("Invalid option")