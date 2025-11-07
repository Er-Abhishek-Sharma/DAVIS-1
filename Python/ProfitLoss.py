cost_price = float(input("Enter the cost price of item : "))
selling_price = float(input("Enter the selling price of item : "))
total = abs(round(selling_price - cost_price, 2))
if cost_price < selling_price:
    print("There is profit of ", total, " rupees.")
elif cost_price > selling_price:
    print("There is loss of ", total, " rupees.")
else:
    print("There is neither profit nor loss")