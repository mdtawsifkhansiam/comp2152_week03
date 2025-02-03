"""
Author: MD Tawsif Siam
Assignment: #1
"""

# Define variables with data type comments
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# Define a dictionary for workout statistics
# Dictionary: keys (str) -> values (tuple of 3 ints)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 30),
    "Taylor": (40, 30, 25)
}

# Create a new dictionary to store total workout minutes
total_minutes_dict = {f"{friend}_Total": sum(minutes) for friend, minutes in workout_stats.items()}

# Update workout_stats after iteration is complete
workout_stats.update(total_minutes_dict)

# Create a 2D list of workout minutes
# List of lists: each sublist represents a friend’s workout minutes
workout_list = [list(minutes) for minutes in workout_stats.values() if isinstance(minutes, tuple)]

# Slice workout_list
# Extract yoga and running minutes for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and running minutes for all friends:", yoga_running)

# Extract weightlifting minutes for last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)

# Check if any friend has total workout minutes >= 120
for friend, total in total_minutes_dict.items():
    if total >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

# User input to check workout stats
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    if isinstance(workout_stats[friend_name], tuple):
        yoga, running, weightlifting = workout_stats[friend_name]
        total = workout_stats.get(f"{friend_name}_Total", 0)
        print(f"{friend_name}'s workout stats: Yoga: {yoga} min, Running: {running} min, Weightlifting: {weightlifting} min, Total: {total} min")
    else:
        print(f"{friend_name}'s total workout time: {workout_stats[friend_name]} min")
else:
    print(f"Friend {friend_name} not found in the records.")

# Find friend with highest and lowest workout minutes
highest_friend = max(total_minutes_dict, key=total_minutes_dict.get).replace('_Total', '')
lowest_friend = min(total_minutes_dict, key=total_minutes_dict.get).replace('_Total', '')

print(f"Friend with highest workout minutes: {highest_friend}")
print(f"Friend with lowest workout minutes: {lowest_friend}")
