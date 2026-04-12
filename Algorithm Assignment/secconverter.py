seconds = int(input("Enter your seconds: "))

hour = seconds // 3600

minutes = (seconds // 3600) % 60

seconds = seconds % 60

print("The time is ", hour, "Hours", minutes, "Minutes", seconds, "Seconds")
