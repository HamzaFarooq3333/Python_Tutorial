#f-string

letter ="Hello ,My name is {} and I live in {}"
name="Hamza"
country="Pakistan"
print(letter.format(name,country))

#if it is given in this order
print(letter.format(country,name))

#To fix above mistake we used to do formatting like this 
letter ="Hello ,My name is {1} and I live in {0}"
name="Hamza"
country="Pakistan"
print(letter.format(country,name))

#The above method is correct but it is not convinient to use.Therefore we use f-string method
print(f"Hello my name is {name} and I live in {country}")

#f-string allows us to populate the value of the varaiables directly in the string 


#Rounding off value using old method 

txt="The price of apple is {value:.2f} dollars"  #2f with the variable rounds of the value upto 2 decimal places
print(txt.format(value=2.42743847))       #Similar is done with 3f and 4f onward


#Rounding off value using f-string
price=2.34357
txt=f"The price of apple is {price:.2f} dollars"
print(txt)


#Single statement f-string
print(f"{2* 30}")


#f-string to print a strig without populating values in the string
print(f"My name is {{name}} and I live in {{country}}") #We use double curly brackets to avoid population of values 

#This retains the f-string as an f-string


