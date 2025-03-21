# ### `Problem 4`: Write a menu-driven program - 
# 1. cm to ft 
# 2. km to miles 
# 3. USD to INR 
# 4. exit


def cm_to_ft(cm):
    return cm/30.48  #1 cm = 0.0328 ft
 
def km_to_miles(km):
    return km*0.621371  #1 km = 0.621371 miles

def usd_to_inr(usd):
    exchange_rate = 83.0
    return usd*exchange_rate

while True:
    print("\nMenue: ")
    print("1. Convert cm to ft")
    print("2. Convert km to miles")
    print("3. Convert usd to inr")
    print("4. Exit")

    choice = int(input("ENter your choice (1-4): "))

    if choice ==1:
        cm = float(input("Enter length in cm"))
        print(f"{cm} cm = {cm_to_ft(cm):.2f}")
        # {cm_to_ft(cm):.2f} → Calls the function cm_to_ft(cm) and formats the result to 2 decimal places using .2f.

    elif  choice == 2:
        usd = float(input("ENter amount in usd: "))
        print(f"{usd} USD = Rs{usd_to_inr(usd):.2f} INR")

    elif choice == 3:
        usd = float(input("Enter amount in USD: "))
        print(f"{usd} USD = ₹{usd_to_inr(usd):.2f} INR")

    elif choice == 4:
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 4.") 
