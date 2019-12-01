# Take the user's input of expected wake up time (hour, minute)
def alarm(hour, minute):
    # subtract the expected wake up time minute by 45
    # to make the alarm 45 minutes earlier
    # Set the constraints so that hours are in 24hours
    # minutes are set to 60
    new_minutes = (minute - 45)
    if new_minutes < 0:
        hour-=1
    return hour%24, new_minutes%60

# Take the user input and establish it as (hour, minute)
# and split the input into two separate integers in a list
hour, minute = map(int,input().split())

# Print out the new wake up time and minute as "answer"
# as (hour, minute) from the list of the input
answer = alarm(hour, minute)
print(answer[0], answer [1])
