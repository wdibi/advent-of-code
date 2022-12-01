# Read the sea floor depths from the input
# depths = [int(x) for x in input().strip().split('\n')]

# Replace above suggested code with a different way to read the input
with open("input_sample.txt") as file:
    depths = [int(x.rstrip()) for x in file]

# Initialize a counter for the number of times the depth increases
num_increases = 0

# Iterate through the depths starting at the second element
for i in range(1, len(depths)):
    # If the current depth is greater than the previous depth, increment the counter
    if depths[i] > depths[i - 1]:
        num_increases += 1

# Print the number of times the depth increased
print(num_increases)
