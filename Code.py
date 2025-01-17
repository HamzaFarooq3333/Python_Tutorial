#For loops 
#Iterating string 
name="Hamza Farooq"

for i in name:
    print(i)
    if(i=="q"):
        print("This is something special")



#Iterating lists 
color=["Green","Red","Yellow","Purple"]
for colors in color:
    print(colors)
    for i in colors:    #Nested for loops
        print(i)


for k in range(7):  #k will go from 0 to 6
    print(k+1)


for k in range(3,8): #k will go from 3 to 7
    print(k)

for i in range(2,11,2): #Will print even numbers only
    print(i)

#While loops

while i<4:
    print(i)
    i+=1

print("Done with the loop")


i=0
while i<38:
    i=int(input("Input the number = "))
    print(i)

print("Done with loop")


#Decrementing while loop
#While loop with else statement
i=10
while i>0:
    print(i)
    i-=1
else:
    print("Done with loop")




#Emulation of do while loop 
a=int(input("Enter the number = "))
print(a)     #This execution happens once 
while a>12:
    print(a)
    a=a-1
else:
    print("Number is less than 12")


print('\n')
#For loop using else condition 
for i in range(5):
    print(i)
else:
 print("Loop is done")


print('\n')
for i in []:
    print(i)
else:
    print('no i ')


print('\n')
for i in range(6):
    print(i)
    if(i==4):
        break
else:    #Else is not executed because the loop was broken before the last iteration was printed 
    print("No i")



print('\n')
i=0
while i<7:
    print(i)
    i=i+1
    if(i==4):
        break
else:    #Else is not executed because the loop was broken before the last iteration was printed
    print("Else block in loop ")
print('Out of loop')

print('\n')


for i in range(5):
    print('Iteration no {} in for loop'.format(i+1))
    if(i==3):
        break
    else:
        print('Else block in for loop')
print('out of loop')




print('\n')
print("-> For loop using if,elif ,else ")


for i in range(5):
    print('Iteration no {} in for loop'.format(i+1))
    if(i==3):
        break
    elif(i<2):
        print('Elif 1 block in for loop')
    elif(i<3):
        print('Elif 2 block in for loop')
    if(i<3):
        print('If  2 block in for loop')
    else:
        print('Else block in for loop')




print('\n')
print("-> While loop using if,elif ,else ")

i=0
while i<7:
    print('Iteration no {} in while loop'.format(i+1))
    i=i+1
    if(i==5):
        break
    elif(i<2):
        print('Elif 1 block in while loop')
    elif(i<3):
      print('Elif 2 block in while loop')
    if(i<3):
          print('If  2 block in while loop')
    else:
         print('Else block in while loop')

    