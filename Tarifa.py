# Assign megabytes and months
megabytes = int(input())
months = int(input())
# print the number of megabytes in next month
# By multiplying megabytes by months to get the number of megabytes
# Subtract it by the sum of the number of megabytes used in
# the range of the amount of months entered
# add megabytes to represent each new amount of megabytes added for the new month
print((megabytes * months) - sum([int(input()) for _ in range(months)]) + megabytes)