# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost_price = float(input("Enter Cost Price (Rs): "))
selling_price = float(input("Enter Selling Price (Rs): "))

#calculate difference
difference = round(abs(selling_price - cost_price),2)

if selling_price >= cost_price :
    print(f"profit : Rs{difference}")
elif selling_price < cost_price:
    print(f"Loss : Rs{difference}")
else:
    print("No Profit, No Loss.")   

