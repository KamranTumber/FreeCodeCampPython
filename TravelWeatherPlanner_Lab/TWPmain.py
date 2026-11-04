# 1. Define the required variables
distance_mi = 10        # Change this number to test different distances
is_raining = False       # True if raining, False otherwise
has_bike = False          # True if you have a bike, False otherwise
has_car = True          # True if you have a car, False otherwise
has_ride_share_app = True # True if you have a ride-share app, False otherwise

# 2-8. Conditional statements evaluating distance categories in ascending order
if not distance_mi:
    print(False)
elif distance_mi <= 1:
    print(not is_raining)
elif distance_mi <= 6:
    print(has_bike and not is_raining)
else:
    print(has_car or has_ride_share_app)