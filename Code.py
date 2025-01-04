name="hamza"
print(name)




#Double quote inside string 
#Using escape sequence characters
a="He said ,\"I want to eat an apple"
print(a)

#Using double quote in a single quote
a='He said ,"I wants to eat an apple"'
print(a)


#Printing multiple lines in a single string using triple single or double quotes
b='''Hello
My name is  hamza
I am a CS  student'''
print(b)


####Indexing in strings 
print(b[3])
print(b[7])

#Displaying all characters in a string using for loop
print("Displaying all characters in a string using for loop")
for i in b:
    print(i)


#String slicing
name="Hamza Farooq"
print(name[0:5])
print(name[6:18])


fruit='mango'
print(len(fruit))

#This includes 0 but not 3
print(fruit[:3]) #Python automatically sets the initial index to zero 

print(fruit[3:]) #Python automatically sets the end index to the last index of the string
#Above print is also equal to print(fruit[3:len(fruit))
print(fruit[:]) #Python automatically sets the first and last index of the string accordingly


#String slicing using negative indexing 
print(fruit[0:-3]) 
#Equivalent to
print(fruit[0:len(fruit)-3])


#print(fruit[-1,-3])
#Equal to print(fruit[len(fruit)-1,len(fruit)-3])
#Which is 4:2 therefore nothing is printed begin should be smaller then end

#print(fruit[-3,-1])


#####String Methods (Functions built-in in strings)
fruit="!!ManGo!!"


#1. lower() - converts all characters in a string to lowercase
print("--> lower() - converts all characters in a string to lowercase")
print(fruit.lower())


#2. upper() - converts all characters in a string to uppercase
print("--> upper() - converts all characters in a string to uppercase")
print(fruit.upper())


#3. title() - converts the first character of each word to uppercase and the rest to lowercas
print("--> title() - converts the first character of each word to uppercase and the rest to lowercase")
print(fruit.title())



#4. capitalize() - converts the first character of a string to uppercase and the rest to lowercas
print("--> capitalize() - converts the first character of a string to uppercase and the rest to lowercase")
print(fruit.capitalize())


#4. swapcase() - swaps the case of a string (i.e. upper case becomes lower and lower becomes upper
print("--> swapcase() - swaps the case of a string (i.e. upper case becomes lower and lower becomesupper")
print(fruit.swapcase())


#5. count() - returns the number of occurrences of a substring in a string
print("--> count() - returns the number of occurrences of a substring in a string")
print(fruit.count('a'))


#6. find() - returns the index of the first occurrence of a substring in a string
print("--> find() - returns the index of the first occurrence of a substring in a string -1 if not present")
print(fruit.find('i'))


#7. rfind() - returns the index of the last occurrence of a substring in a string
print("--> rfind() - returns the index of the last occurrence of a substring in a string -1 if not found")
print(fruit.rfind('i'))


#8. index() - returns the index of the first occurrence of a substring in a string
print('''-->  index() - returns the index of the first occurrence of a substring in a string 
     throws error if substring is not present in the string  ''')
print(fruit.index('o'))


fruit.isalnum
#9. isalnum() - returns True if all characters in a string are alphanumeric, otherwise Fals
print("--> isalnum() - returns True if all characters in a string are alphanumeric(A-Z or a-z or 0-9), otherwise False")
print(fruit.isalnum())


fruit.isalpha
#10. isalpha() - returns True if all characters in a string are alphabets,
print("--> isalpha() - returns True if all characters in a string are alphabets(A-Z or a-z), otherwise retruns false")
print(fruit.isalpha())


#11. isdigit() - returns True if all characters in a string are digits, otherwise Fals
print("--> isdigit() - returns True if all characters in a string are digits(0-9)")
print(fruit.isdigit())



#12. islower() - returns True if all characters in a string are lower case, otherwis
print("--> islower() - returns True if all characters in a string are lower case")
print(fruit.islower())


#13. isupper() - returns True if all characters in a string are upper case, otherwis
print("-->  isupper() - returns True if all characters in a string are upper case")
print(fruit.isupper())



#14. isspace() - returns True if all characters in a string are spaces, otherwise F
print("--> isspace() - returns True if all characters in a string are spaces")
print(fruit.isspace())



#15. istitle() - returns True if a string is a title, i.e. th
print("""--> istitle() - returns True if a string is a title, i.e. the first
      character of each word is upper case and the rest are lower case""")
print(fruit.istitle())



#16. isprintable() - returns True if all characters in a string are printable, otherwis
print("-->  isprintable() - returns True if all characters in a string are printable (/n) is not a printable character")
print(fruit.isprintable())



#17. isnumeric() - returns True if all characters in a string are numeric, otherwise F
print("-->  isnumeric() - returns True if all characters in a string are numeric")
print(fruit.isnumeric())



#18. startswith() - returns True if a string starts with a specified value, otherwise Fals
print("-->  startswith() - returns True if a string starts with a specified value, otherwise False")
print(fruit.startswith('M'))



#19. endswith() - returns True if a string ends with a specified value, otherwise Fals
print("-->  endswith() - returns True if a string ends with a specified value, otherwise False")
print(fruit.endswith('o'))
print("""Can also be used by slicing  end_with("word",starting_index,ending_index)""")
print(fruit.endswith("o",2,4))



#20. replace() - returns a string where all occurrences of a substring are replaced with another substring
print("--> replace() - returns a string where all occurrences of a substring are replaced with another substring")
print(fruit.replace('a','b'))



#21. split() - splits a string into a list where each word is a list item
print("-->  split() - splits a string into a list where each word is a list item")
print(fruit.split('o'))



#22. join() - joins all items in a list into a string
print("-->  join() - joins all items in a list into a string")
print(' '.join(['apple','banana','cherry']))



#23. strip() - removes leading and trailing characters from a string
print("-->  strip() - removes leading and trailing characters from a string")
print(fruit.strip('!'))



#24. lstrip() - removes leading characters from a string
print("--> lstrip() - removes leading characters from a string")
print(fruit.lstrip('!'))



#25. rstrip() - removes trailing characters from a string
print("--> rstrip() - removes trailing characters from a string")
print(fruit.rstrip('!'))



#26. center() - returns a string centered in a specified width, padding with a specified fill
print("--> () - returns a string centered in a specified width, padding with a specified fill")
print(fruit.center(20))
print(fruit.center(20,"-"))
print(len(fruit.center(20)))























