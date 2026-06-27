"""
This is my program for the Meal Price Calculator :))
Steven Santillan
here i added drinks and add-ons for the children and the adults to be more specific
with their orders, and they might order something else than just a meal.
"""

child_meal = float(input("What is the price of a child's meal? "))
child_drinks = float(input("What is the price of a child's drink? "))
child_addons = float(input("What is the price of a child's add-ons? "))
#just to avoid confusion between adult and child
adult_meal = float(input("What is the price of an adult's meal? "))
adult_drinks = float(input("What is the price of a adult's drink? "))
adult_addons = float(input("What is the price of a adult's add-ons? "))

child_quantity = int(input("How many children are there? "))
adult_quantity = int(input("How many adults are there? "))

print()
subtotal_child = (child_meal + child_drinks + child_addons) * child_quantity
subtotal_adult = (adult_meal + adult_drinks + adult_addons) * adult_quantity
subtotal = subtotal_child + subtotal_adult
print(f"Subtotal: ${subtotal:.2f}")

print()
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * tax_rate / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

print()
payment = float(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")