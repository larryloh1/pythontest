'''
Lecturer's Demo
'''
# Define the function to calculate the taxi fare
def calc_taxi_fare(distance):
    fare = 3.4
    remaining_distance = distance - 1
    
    if remaining_distance > 0:  
        if remaining_distance % 0.4 == 0:
            fare = fare + (remaining_distance // 0.4)*0.22
        else:
            fare = fare + ((remaining_distance // 0.4) + 1)*0.22
                
    return fare

#main program
distance = float(input("Enter the distance travelled in km: "))
fare = calc_taxi_fare(distance)
print("The fare is $" + str(fare) + ".")

