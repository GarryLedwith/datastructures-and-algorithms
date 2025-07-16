# lists 
# find the lowest value in a list
# Algorithm:
# 1. Initialize a variable to hold the lowest value, starting with the first element of the list 
# 2. Loop through each element in the list 
# 3. If the current element is lower than the lowest value, update the lowest value
# 4. After the loop, return the lowest value

# Solution: 
numbers = [5, 3, 8, 1, 4] # List of numbers to find the lowest value from
lowest_value = numbers[0]  # Initialize with the first element

for n in numbers: # Loop through each number in the list
    if n < lowest_value: # Check if the current number is lower than the lowest value
        lowest_value = n  # Update the lowest value if the condition is met 
print("Lowest value in the list:", lowest_value)  # Output the lowest value found
