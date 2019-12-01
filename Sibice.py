# import the math class for reference for square roots
import math
# Assign the first three input number split them into
# the variables: n,w,h n = number of matches,
# w = width of match, h = height of the match
n, w, h = [int(x) for x in input().split()]
# Create a formula to determine if the match will fit
formula = math.sqrt(w**2 + h**2)+ 0.01
# Take the input cases from n and
# compare them to the formula
# input < formula = print Da: Yes
#input > formula = print Ne: No
for _ in range(n):
    if int(input()) < formula:
        print("DA")
    else:
        print("NE")
