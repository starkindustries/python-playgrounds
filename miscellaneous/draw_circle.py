# Define the radius of the circle
radius = 10

# Loop through each row and column
for y in range(-radius, radius+1):
    for x in range(-radius, radius + 1):
        
        # Calculate the distance from the center
        distance = (y**2 + x**2) ** 0.5
        
        # If the distance is within the radius, print an asterisk, otherwise print a space
        if distance <= radius:
            print("█", end="")
        else:
            print(" ", end="")
    
    # Move to the next line after each row
    print()
