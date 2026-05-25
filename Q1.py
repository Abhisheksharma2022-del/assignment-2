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

else:
    print("No Profit No Loss")