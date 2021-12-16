# print welcome messsage
print('Welcome to the Miles Per Hour Conversion App\n')

# get input from user
speed_in_miles_per_hour = float(input('What is your speed in miles per hour: '))

# calculate the speed in meters per second
speed_in_meters_per_second = round(speed_in_miles_per_hour * 0.4474, 2)
print(f'Your speed in meters per second is {speed_in_meters_per_second}.')
