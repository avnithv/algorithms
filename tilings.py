

n = m = 0

grid = [[None for a in range(m)] for b in range(n)]

def count(x, k, last = False):
  for a in range(m):
    if grid[k - 1][m] == 'U':
      grid[k][m] = 'D' 
    if m != 0:
      if grid[k][m - 1] == "L":
        grid[k][m] = 'R'





