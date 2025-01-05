

budget=int(input("Enter the budget = "))
price=int(input("Enter the price of the food item = "))

if(budget>price):
    print("You can buy the food item")
    print("Enter a number from the given choices ")
    print("Do you want to buy this item?")
    print("1-Yes       2-No")
    a=int(input("Enter option number = "))
    if(a==1):
        print("You have bought the food item")
        print("Balance = ",budget-price)
    elif(a==2):
        print("You have not bought the food item")
    else:
         print("Invalid option")
    
elif(budget==price):
    print("You can buy the food item if necessary")
    print("Enter a number from the given choices ")
    print("Do you want to buy this item?")
    print("1-Yes       2-No")
    a=input("Enter option number = ")
    if(a==1):
        print("You have bought the food item")
        print("Balance = ",budget-price)
    elif(a==2):
        print("You have not bought the food item")
    else:
         print("Invalid option")
else:
    print("You cannot buy the food item")



