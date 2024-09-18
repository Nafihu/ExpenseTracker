# welcome message 
print("hello this is an expense tracker created by Nafihu Lawal")
# initialise dict
data = {}

# Function to add an expense
def add_expense():
    # Prompt the user for inputs
    price = input("What is the price?: ")
    price = int(price)
    
    if price <= 0:
        new_price = input("That is not a valid number. Please input a number bigger than zero: ")
        data["price_of_item"] = int(new_price)
    else:
        data["price_of_item"] = price

    category = input("What subsection does this fall under?: ")
    data["category"] = category  

    descsr = input("Write a description: ")
    data["description"] = descsr  

add_expense()

#display results 
print(f"This is a summary of your expenses: {data}\nThank you for using this expense tracker.")


while True:
    next_step = input("If you'd like to add more items, type Y or N: ").upper()

# Check the user's response
    if next_step == "Y":
    # You can add the logic here for adding more items
        add_expense()
        print(f"This is a summary of your expenses: {data}")
    elif next_step == "N":
        print("Thank you, Goodbye!")
        break
    else:
        print("Invalid input. Please type Y or N.")