
#Using list 
marks=[12,34,65,87,9,33,4,27]
print('index value')
index=0
for mark in marks:
    print(index,'   ',mark)
    if(index==3):
        print("This is the 4th mark")
    index=index+1

print('\n')
print("-> Using enumerate for list ")

#Using emurate function 
print('index value')
for index,mark in enumerate(marks,start=3):
    print(index,'   ',mark)
    if(index==3):
        print("This is the 4th mark")



#Using string 
print('\n')
string="Hamza_Farooq"
print("-> Using enumerate for string ")
#Using emurate function
print('index value')
for index,character in enumerate(string):
    print(index,"   ",character)
    if(index==3):
        print("This is the 4th character")





#Using Tuples
print('\n')
#Using emurate function
print("-> Using enumerate for Tuples ")
marks=(12,34,65,87,9,33,4,27)
print('index value')
for index,mark in enumerate(marks):
    print(index,"   ",mark)
    if(index==3):
        print("This is the 4th mark")









