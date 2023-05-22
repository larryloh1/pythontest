def meet_minimum(total_price, minimum):
    if total_price >= minimum:
        return True
    else:
        return False

# Main program code
total = 0
for i in range(5):
    price = float(input("Enter a price: "))
    total = total + price
min_value = float(input("Enter minimum limit: "))
if meet_minimum(total, min_value):
    print("Total price meets the minimum")
else:
     print("Total price does not meet the minimum")
