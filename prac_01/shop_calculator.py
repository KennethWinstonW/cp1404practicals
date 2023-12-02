"""
Pseudocode
set total_price to 0
set discount_rate to 0.1
while num_items != 0:
    if num_items < 0 then
        print "invalid number of items"
    else
        set total_price to 0  # reset the total price for the current calculation
        for i in range num_items
            input item_price
            add item_price to total_price
        end for
        if total_price > 100 then
            calculate discount as total_price times discount_rate
            calculate discount_price as total_price minus discount
            print "total price for", num_items, "items is $", discount_price formatted to 2 decimal places
        else
            print "total price for", num_items, "items is $", total_price formatted to 2 decimal places
        end if
        exit loop
    input item_price
    end if
"""

total_price = 0
DISCOUNT_RATE = 0.1
num_items = int(input("Number of items: "))
while num_items != 0:
    if num_items < 0:
        print("Invalid number of items")
    else:
        for i in range(num_items):
            item_price = float(input(f"Number of items {i + 1}: $"))
            total_price += item_price
        if total_price > 100:
            discount = total_price * DISCOUNT_RATE
            discount_price = total_price - discount
            print(f"Total price for {num_items} items is ${discount_price:.2f}")
        else:
            print(f"Total price for {num_items} items is ${total_price:.2f}")
        break

    num_items = int(input("Number of items: "))