
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100

    print("Profit =", profit)
    print("Profit Percentage =", profit_percentage, "%")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100

    print("Loss =", loss)
    print("Loss Percentage =", loss_percentage, "%")

# Taken cost prise input to the user 
cost_price = float(input("Enter Cost Price: "))

# Taken selling prise input 
selling_price = float(input("Enter Selling Price: "))

# checking if selling price is greater than cost price
if selling_price > cost_price:

   # calculated profit
    profit = selling_price - cost_price

    # profit percentage formula 
    profit_percentage = (profit / cost_price) * 100

    # result print
    print("Profit =", profit)
    print("Profit Percentage =", profit_percentage,"%")

# checking whether there is a loss or not
elif cost_price > selling_price:

    # loss nikala
    loss = cost_price - selling_price

    # calculated loss percentage
    loss_percentage = (loss / cost_price) * 100

    # result
    print("Loss =", loss)
    print("Loss Percentage =", loss_percentage,"%")

# if both are equal 
# >>>>>>> 859d2bf5147e51ce45ddc0e9ca1f365c187b3347
else:
    print("No Profit No Loss")