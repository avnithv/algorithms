# Uses greedy algorithim to find best order to complete 
# tasks given name, duration, and deadline.
# Assumes points equals deadlime time minus time to finish
# and maximizes points

tasks = [[]] # Array of tasks with the information

tasks.sort(key = lambda task : task[1]) # Sorts array

order = [task[0] for task in tasks] # Gives order

# Finds points
time_sum = 0
points = 0
for task in tasks:
  time_sum += task[1]
  points += task[2] - time_sum