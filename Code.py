
#Recursion
def fac(n):
    if(n==1):
        return 1
    if(n==0):
        return 1
    else:
     return  n*fac(n-1)



print(fac(3))
print(fac(4))
print(fac(5))
print(fac(6))
    
def fabonaci(n):
   if(n==0 or n==1):
      return 1
   else:
      return fabonaci(n-1)+fabonaci(n-2)

print(fabonaci(1))
print(fabonaci(2))
print(fabonaci(3))
print(fabonaci(4))
print(fabonaci(5))
