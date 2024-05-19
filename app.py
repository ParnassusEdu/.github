# arr = [[True, True, False, False, True], [True, True, False, False, True], [True, True, False, False, True]]

# counter = 0
# changed_locations = []

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if counter != 3:
#             if arr[i][j] == False:
#                 arr[i][j] = True
#                 changed_locations.append((i, j))
#                 counter += 1

# print("Counter:", counter)
# print("Modified Array:", arr)
# print("Changed Locations:", changed_locations)


# arr = [[54, 29,86,31], [22, 25,8, 29]]

# for i in range(len(arr)):
#   for j in range(len(arr[i])):
#     if arr[i][j] == 8:
#       print((i+1,j+1))


# Sample temperature readings for each hour of the day for a week
temperatures = [
    [22, 23, 21, 20, 19, 18, 17, 18, 20, 22, 24, 26, 28, 29, 30, 29, 27, 25, 23, 21, 20, 19, 18, 17],  # Monday
    [21, 22, 20, 19, 18, 17, 16, 17, 19, 21, 23, 25, 27, 28, 29, 28, 26, 24, 22, 20, 19, 18, 17, 16],  # Tuesday
    [20, 21, 19, 18, 17, 16, 15, 16, 18, 20, 22, 24, 26, 27, 28, 27, 25, 23, 21, 19, 18, 17, 16, 15],  # Wednesday
    [19, 20, 18, 17, 16, 15, 14, 15, 17, 19, 21, 23, 25, 26, 27, 26, 24, 22, 20, 18, 17, 16, 15, 14],  # Thursday
    [18, 19, 17, 16, 15, 14, 13, 14, 16, 18, 20, 22, 24, 25, 26, 25, 23, 21, 19, 17, 16, 15, 14, 13],  # Friday
    [17, 18, 16, 15, 14, 13, 12, 13, 15, 17, 19, 21, 23, 24, 25, 24, 22, 20, 18, 16, 15, 14, 13, 12],  # Saturday
    [16, 17, 15, 14, 13, 12, 11, 12, 14, 16, 18, 20, 22, 23, 24, 23, 21, 19, 17, 15, 14, 13, 12, 11]   # Sunday
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Variables to store the maximum, minimum, and average temperatures for the week
MaxWeek = -1000
MinWeek = 1000
TotalWeek = 0

# Loop through each day
for day in range(len(temperatures)):
    # Initialize variables for each day
    MaxDay = -1000
    MinDay = 1000
    TotalDay = 0

    # Loop through each temperature of the day
    for temp in temperatures[day]:
        if temp > MaxDay:
            MaxDay = temp
        if temp < MinDay:
            MinDay = temp
        TotalDay += temp

    # Calculate average temperature for the day
    AvDay = TotalDay / 24

    # Print the results for the day
    print(f"{days[day]} - Max Temp: {MaxDay}°C, Min Temp: {MinDay}°C, Avg Temp: {AvDay:.2f}°C")

    # Update weekly values
    if MaxDay > MaxWeek:
        MaxWeek = MaxDay
    if MinDay < MinWeek:
        MinWeek = MinDay
    TotalWeek += TotalDay

# Calculate average temperature for the week
AvWeek = TotalWeek / (len(temperatures) * len(temperatures[0]))

# Print the results for the week
print(f"Max temperature for the week: {MaxWeek}°C")
print(f"Min temperature for the week: {MinWeek}°C")
print(f"Avg temperature for the week: {AvWeek:.2f}°C")

      
      

