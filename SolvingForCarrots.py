# Take the user input and split it into two separate
# integers and assign it to "carrots"
carrots = input().split()
# Assign the first number as an integer from the input
# list "carrots" as "contestants"
contestants = int(carrots[0])
for i in range(0, contestants):
    input()
# Print the second integer in the list to show  the number of
# carrots received based on the number of problems solved.
print(carrots[1])