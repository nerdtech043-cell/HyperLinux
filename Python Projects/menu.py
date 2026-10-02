print("\n" + "*" * 21) 
print("")
print("MENU".center(21, " ")) 
print("")
print("*" * 21 + "\n")
print("1. Burger...........$5.69")
print("2. Fries............$1.49")
print("3. Soda.............$1.29")
total = 0 
cost1 = 0
cost2 = 0
cost3 = 0
order_count = 0
while True: 
    choice = input("Which item would you like to order? \n\nYour Order: ")  
    if choice == "1" or choice in ["burger", "Burger"]:
        print("You ordered a Burger")
        quantity = input("How many would you like? \nQuantity: ")
        cost1 = 5.69 * int(quantity)
        order_count += 1
    elif choice == "2" or choice in ["fries", "Fries"]:
        print("You ordered Fries")
        quantity = input("How many would you like? \nQuantity: ")
        cost2 = 1.49 * int(quantity)
        order_count += 1
    elif choice == "3" or choice in ["soda", "Soda"]:
        print("You ordered a Soda")
        quantity = input("How many would you like? \nQuantity: ")
        cost3 = 1.29 * int(quantity)
        order_count += 1
    else:
        print("Invalid choice")
        cost = 0 
        continue 
    
    total = cost1 + cost2 + cost3  
    average = total / order_count 

    query = input("Would you like to order anything else? (y/n): ")
    if query == "n" or query in ["no", "No"]:
        break

print(f"The cost of your order is ${total:.2f}") 
print(f"The average cost per item is ${average:.2f}")