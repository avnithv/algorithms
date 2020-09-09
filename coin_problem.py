# Given a list of coin values and a target sum of money
# n, this program forms the sum while using as few coins
# as possible

coins = []
n = 0

values = [0]

for x in range(1, n + 1):
  values[x] = float('inf')
  for coin in coins:
    if x - coin < 0: continue
    values[x] = min(values[x], values[x-coin])


