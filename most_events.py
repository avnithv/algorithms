# The greedy algorithm is to choose the event that ends
# as early as possible

# Each event has an array for starting and ending time, as well as name of the event
events = [[]] 

# Sort by end time
events.sort(key = lambda event : event[2])

# Create schedule to include most events
schedule = [0]
end = events[0][2]
event = 1

while True:
  if event > len(events) - 1: break
  if events[event][1] > end:
    schedule.append(event)
    end = events[event][2]
  event += 1

schedule = [event[0] for event in schedule]