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
i=10
while i>0:
    print(i)
    i-=1

print("Done with loop")

