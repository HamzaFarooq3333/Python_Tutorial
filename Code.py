

#Error handling

a=input('enter a number : ')
print(f"Multilpication table of {a} is : ")


#I will get the exception and the other lines of code keep on executing 
try:
   for i in range(1,11):
     print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as exception:
   print('The program could not be run becasue of following error')
   print(str(exception))


print('Some line of code')
print('End of code')



#Handling a specific type of error a number  error and index error we  can handle different types of errors 
# in a single python code 
print('\n')
print('Handling value error ')

try:
   num=int(input("Enter a number = "))
   a=[4,6]
   print(a[num])

except ValueError:
   print('Number entered is not an integer')
except IndexError:
   print('Index out of range')
except IsADirectoryError:
   print('The path specified is a directory')