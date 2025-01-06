
#Break Statement
for i  in range(14):
    if(i==10):
        print("Exited the loop ")
        break
    print("5 x ",i+1 ," = ",(i+1)*5)
  


#Continue Statement
for i in range(12):
    if(i==10):
        print("skipped the iteration ")
        continue
    print("5 x ",i+1 ," = ",(i+1)*5)


#Do_While loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):         #Emulation of Do-While loop
     break



a=int(input("Enter  a number = "))

while True:
    print(a)
    a=a+1
    if(a<1):
        print("Number less than 0")
        break
