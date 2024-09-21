
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# question 1 task 1

restaurant_menu["Beverages"] = {"Soda": 3.59, "Beer": 7.99}

print(restaurant_menu)

# question 1 task 2

steak_price_update = {"Steak": 17.99}
restaurant_menu["Main Course"].update(steak_price_update)

print(restaurant_menu)

# question 1 task 3

item_not_in_stock = restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)