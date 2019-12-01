# Read user input and split it
nums = input().split()
# Assign each integer value from input to R1 and S
R1 = int(nums[0])
S = int(nums[1])
# Calculate the output
R2 = S * 2 - R1
# Print answer
print(R2)