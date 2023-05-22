'''
Additional Challenge
'''   

def mrt_fare(num_stations):
        
    if num_stations <= 5:
        amount = 0.7
    else:
        amount = 0.7 + (num_stations - 5) * 0.3
    
    return amount

# Main program code
stations = int(input("Enter the number of stations:- "))
amount = float(input("Enter the amount in your ezlink card:- "))

tot_fare = mrt_fare(stations)

print("You have to pay $" + str(tot_fare) + " for your MRT ride.")
if amount >= tot_fare:
    print("You have sufficient funds in your card.")
else:
    print("Please top up your card.")