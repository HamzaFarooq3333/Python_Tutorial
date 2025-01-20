
try:
 a=[32,6,2,7,1,9]
 i=int(input("Enter the index for the list = "))
 print(a[i])
except IndexError:
 print("Index out of range")
finally:
 print("Program ended")






try:
 a=[32,6,2,7,1,9]
 i=int(input("Enter the index for the list = "))
 print(a[i])
except IndexError:
 print("Index out of range")

print("Program ended ")






#In this case when finally keyword is not used then the line of code in the function after the return statement is
# not executed becasue the function has returned the value back 
def func():
 
 try:
  a=[32,6,2,7,1,9]
  i=int(input("Enter the index for the list = "))
  print(a[i])
  return 1
 except IndexError:
  print("Index out of range")
  return 0
 print("Program ended")


x=func()
print(x)



#In this case while using finally keyword the function executes the code within finally before returning 
def func():
 
 try:
  a=[32,6,2,7,1,9]
  i=int(input("Enter the index for the list = "))
  print(a[i])
  return 1
 except IndexError:
  print("Index out of range")
  return 0
 finally:
  print("Program ended")


x=func()
print(x)