#Sets
s={2,4,2,5,8,10,2,4,9}
print(s)



#Set does not guarantee order 
info={"Carla",19 ,False,19.34}
print(info)


a=set()  #Empty set otherwise in case of a={}  it is a dictionary 
print(type(a))

#Accessing items using for loop 
for i in info:
    print(i)


#Set Methods

#Joining sets 
# Union and update 

s1={1,2,3,4}
s2={5,6,7,8}
print(s1.union(s2))  #Union returns a new set not changing the original set 
print("Original s1 before union update :",s1)
s1.update(s2)  #Update changes the original set 
print("Updated s1 after union update :",s1)


#Intersection and Intersection update 
print(s.intersection(s1))
print("original s before intersection update :",s)
s.intersection_update(s1)  #It will update the s set with the vlaues that are common  in s and s1 and the other 
#values will be removed from s
print("Updated s after intersection update :",s)


#Symmetric difference and Symmetric difference update
#  (A unin B)-(A intersection B)

print(s.symmetric_difference(s1))
print("Original s before symmetric difference update :",s)
s.symmetric_difference_update(s1)
print("Updated s after symmetric difference update :",s)


#Difference and Difference Update 
# A-B
#Prints elements present in A and not in B
print(s.difference(s2))
print("Original s before s update :",s)
s.difference(s2)
print("Updated  s after difference update :",s)


#Isdisjoint 
# Checks if the items of first  set is present in the other set 
print("Is s disjoint of s1 :",s.isdisjoint(s1))


#Issuperset
#Are all the elements in the second set already present in the first set 
print("Are elemets in s2 present in s :",s.issuperset(s2))


#Issubset
#Are all the elements in the first set also  present in the second set 
print("Is s sebset  of s1 :",s.issubset(s1))


# Add (It adds a single item in the set )
print("Original s before adding :",s)
s.add(23)
print("Updated s after adding 23 :",s)

#Update (Adds multiple items in the set basically adds the second set in the first set )
print("Original s1 before updating it with s2 :",s1)
s1.update(s2)
print("Updated s1 after adding s2 :",s1)

#Remove (Removes item from set if the item is not present it will raise error)
print("s1 before removing 4 :",s1)
s1.remove(4)
print("s1 after removing 4 :",s1)

#Discard (Removes item from the set if the item is not present it will not raise error)
print("s1 before discarding  6 :",s1)
s1.discard(6)
print("s1 after discarding 6 :",s1)


#Pop (Removes the last item from the set but we do not know what the last item is because they are random in set)

print("s2 before poping :",s2)
item=s2.pop()
print("s2 after poping :",s2)
print("Item poped :",item)


#del (Deletes an entire set)
del s 
#print(s)    will get error because s does not exit anymore

#clear (Deletes all the items in the set )
print("s1 before clearing :",s1)
s1.clear()
print("s1 after clearing :",s1)

#If-else statements
info={"Hamza",20,True,33}
if "Hamza" in info:
    print("Present")
else:
    print("Not present")