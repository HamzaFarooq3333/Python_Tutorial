#List
marks=[3,5,6,"Hamza",True,7,2,1,8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(marks[-3])  #Negative  indexing  same as the one below 
print(marks[len(marks)-3])


#Searching for an element in lsit

if 6 in marks:    
    print("yes")
else:
 print("no")


if "6" in marks:   #If we search 6 as a string we will get no because 6 is as an integer in our list not as a string
    print("yes")
else:
 print("no")


#Same searching  applies in strings as well 

if "am" in "Hamza":
   print("yes")
else:
   print("no")

if "az" in "Hamza":
   print("yes")
else:
   print("no")


#Printing all elements of list
print(marks)
print(marks[:])

#Printing using inndexing
print(marks[1:3])
print(marks[3:-2])
print(marks[1:6:2]) #This expression can also be written as marks[Start:End:Steps]



#List comprehension 
lst=[i for i in range(5)]
print(lst)

lst=[i for i in range(10) if(i%2==0)]
print(lst)


#List Methods
#append() method adds an element at the end of the list
lst=[3,1,6,2,8]
print(lst)
lst.append(7)
print(lst)



#sort() method sorts the list in ascending order
lst.sort()
print(lst)



#sort() method with reverse= true sorts the list in ascending order
lst.sort(reverse=True)
print(lst)



#reverse() method reverses the list
lst.reverse()
print(lst)




#returns the index of the first occurrence of the element
print(lst.index(2))



#Tells the number of occurances of a number in a list 
lst.count(2)
print(lst.count(2))




#removes the first occurrence of the element
lst.remove(2)
print(lst)




#removes the last occurrence of the element
lst.pop()
print(lst)



#This method directly changes the content in the list because m acts as a pointer towards the list l 
# any changes in m will directly affect l so we should use copy function instead of doing this 
l=[2,4,6,2,8]
m=l
m[0]=0
print(l)

#Copy function copies the content of one list into another list 
m=l.copy()
m.append(3)
m[0]=0
print(l)
print(m)


#Insert function inserts an element at a specific index in a list 
l.insert(1,23)   #insert(index,element)
print(l)


#Extend takes a list and appends it at the end to the other list 
m=[900,1000,1100]
l.extend(m)
print(l)  #l chnages in this 



#Concatinate 2 lists 
l=[1,2,3]
m=[4,5,6]
k=l+m
print(l)  #We get  a new list in this case and l does not change 
print(k)










