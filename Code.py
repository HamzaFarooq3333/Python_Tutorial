#Dictionary 

info={
  "Name":"Hamza Farooq",
  "Age":20,
  "City":"Lahore",
  "Country":"Pakistan"

}

#Accessing single value
#We can acces the name which is Hamza Farooq using the key name  
print(info["Name"])   #This will throw error in case the key is not present
print(info.get("Name"))  #This will print none in case the key is not present
print('\n')



#Acessing multiple values
#We can access multiple values using the .items() method which returns a list of tuples
for key, value in info.items():
    print(f" The value corresponding to the key  {key}  is : {value}")  #This will print all the key value pairs

print('\n')

#Priting the key value pairs
print(info.items())

print('\n')
for key,value in info.items():
   print(f" The value corresponding to the key  {key}  is : {value}")  #This will print all the key value pairs


print('\n')


#Creating empty dictionary 
#We can create an empty dictionary using the {} syntax
empty_dict={}  #This is an empty dictionary
print("Printing empty dictionary : ",empty_dict)
print('\n')



#Dictionary Methods
#1-Update (Used to update the items in the dictionary)
ep1={122:45,123:89,145:67,324:76}
ep2={666:32,324:36,124:46}
print("ep1 before update : ",ep1)
ep1.update(ep2)
print("ep1 after update : ",ep1)
print('\n')



#2-Clear (Removes all the items from the dictionary)
ep1.clear()
print("ep1 after clearing : ",ep1)
ep1={122:45,123:89,145:67,324:76}
print('\n')



#3-Pop (Removes the required key value pair from the dictionary )
print('\n')
print('ep2 before using pop function ',ep2)
ep2.pop(324)
print('ep2 after using pop to remove key value pair with key 324',ep2)
print('\n')





#4-PopItem (Removes the last key value pair from the dictionary)
print('\n')
print('ep1 before using popitem ', ep1)
ep1.popitem()
print('ep1 after using popitem to delete the last key value pair',ep1)
print('\n')




#5-del (Deletes the dictionary )
print('\n')
print('Before deleting key in ep1',ep1)
del ep1[123]  #Write the key as an integer you will get error if you write it as a string 
print('Deleting key value pair having key 123 using del keyword',ep1)
del ep1  #Del keyword will delete the entire doctionary if the key value is  not given 
print("deleted ep1 using del keyword")
print('\n')




#6-Copy (Copies the keys and values of a dctionary and places it in another dictionary)
print('\n')
a={2:32,3:45,4:54}
b={7:32}
b=a.copy()
print("a : ",a)
print("b : ",b)
print('\n')




#7-Set Default (Adds  a key in the dictionary without a value)
print('\n')
a.setdefault(9)
print(a)
print('\n')




#8-FromKey    (Returns a new dictionary with the specified keys and values.
# You will get a new dictionary having all the keys in the input dictionary having the same input value)
print('Printing b using fromkeys : ',a.fromkeys(b,53))
print('\n')




#9-Values (Returns all the values of the dictionary )
print("Printing values of a : ",a.values())
print('\n')






#10-Keys  (Returns all the keys of the dictionary)
print("Printing keys of a : ",a.keys())
print('\n')



#11-Items (Returns all the items(key-value pair) in the dictionary)
print("Printing items in a",a.items())





































