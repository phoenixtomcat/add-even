target = int(input("Enter an integer between 0 and 1000: "))
# the target is the stopping point for the activity

# chosen_number is initialized to the next odd number after the target
chosen_number = target + 1
# 2 actions in 1: define total, and set it to 0 to begin with
total = 0
# the loop starts with 0 and ends at the chosen number, in steps of 2, to stay even
for number in range(0, chosen_number, 2):
  # total is incremented by the current number in the loop
  total += number
# once the loop ends, the total number is printed as it is at the end
print(total)