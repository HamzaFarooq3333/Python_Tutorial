#Tuples
tup=(1,4,6,8,"Ali",True)
print(type(tup))
print(tup)


#Tuple with a single item without a comma is considered an integer 
t=(1)
print(type(t))

#While using a single item in tuple a comma is needed in order to make it a tuple instead of an integer 
t=(1,)
print(type(t))

#Changing in tuple is not allowed 
#tup[0]=10
print(tup)  #This will give an error because tuples are immutable in Python


#Indexing in tuple
print(tup[0])  #This will print 1
print(tup[5])  #This will print True
print(tup[-2])  #Negative indexing





#Slicing in tuple
print(tup[1:4])  
print(tup[:])
print(tup[1:]) 
print(tup[:4]) 
print(tup[1:5:2])



#Searching for item
if 324 in tup:
    print("Item found")
else:
 print("Item not found")

 #Searching for item with index
 print(tup.index(8))

 #Methods of tuples
 #For making changes in a tuple 
 #We need to convert it into a list first and then make the changes
 countries=("Pakistan","Germany","Japan","China")
 temp=list(countries)
 temp[0]="USA"
 temp.pop()
 temp.append("Korea")
 countries=tuple(temp)
 print(countries)



 #Concatinaion  of 2 tuples to make a new tuple
 tup1=(1,2,3)
 tup2=(4,5,6)
 tup3=tup1+tup2
 print(tup3)


 #Count method tells the total number of occurances of an element in a tuple
 tup=(1,2,2,3,4,4,4,5,6)
 print(tup.count(4))


 #Index tells the first occurance of the element in the tuple and give value error if element is not present
 tup=(1,2,2,3,4,4,4,5,6)
 print(tup.index(4))


#tup.index(Element_to_search,starting_index,ending_index)
print(tup.index(5,4,8))  #The method finds the first occurance of the element while slicing the tuple





