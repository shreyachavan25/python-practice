 # Initialize the menu dictionary with items and prices
menu = {
     "espresso": 3.00,
     "croissant": 3.50,
     "muffin": 2.75,
     "tea": 2.50
 }

 # Track the customer's total order
total_bill = 0.0
order = []

 # Prompt the customer for their order
print("Welcome to the Coffee Shop!")
print("What would you like to order?")

 # Display the menu items and prices
for item, price in menu.items():
     print(f"{item.capitalize()}: ${price:.2f}")

 # Loop to take the customer's order
while True:
     # Get the customer's choice
     choice = input("Enter an item (or type 'done' to finish): ").lower()

     # Check if the customer is done ordering
     if choice == 'done':
         break

     # Check if the choice is valid
     if choice in menu:
         order.append(choice)
         print(f"Added {choice} to your order.")
     else:
         print("Sorry, we don't have that item. Please choose from the menu.")


print("\nThank you for your order! Here is your receipt:")
print("--- Receipt ---")

 # Add each item in the order to the receipt and calculate the total
for item in order:
     price = menu[item]
     print(f"Item: {item.capitalize()} - ${price:.2f}")
     total_bill += price

print("---------------")

 # Display the final calculated total
print(f"Total Bill: ${total_bill:.2f}")