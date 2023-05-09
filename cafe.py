menu = ["tea", "coffee", "juice", "water"]

stock = {menu[0]: 100, menu[1]: 100, menu[2]: 50, menu[3]:50}   # set each menu item a key value pair with
price = {menu[0]: 2, menu[1]: 3, menu[2]: 3, menu[3]:2}         # stock and price

total_stock_value = 0               # declare total as 0 

for i in stock:
    total_stock_value += stock[i]*price[i]      # loop through each menu item

print(f"The total value of all stock is £{total_stock_value}.")

