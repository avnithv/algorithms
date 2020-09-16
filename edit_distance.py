x = y = ''

distance = [[0 for a in range(len(x))] for b in range(len(y))]

for a in range(len(x)):
  for b in range(len(y)):
    cost = 0 if x[a] == y[b] else 1
    if x == 0 and y == 0:
      distance[x][y] = 0
    elif x == 0: 
      distance[x][y] = distance[x][y - 1] + 1
    elif y == 0:
      distance[x][y] = distance[x - 1][y] + 1
    else:
      distance[x][y]=min(distance[x-1][y]+1,distance[x][y-1]+1,distance[x-1][y-1]+cost) 
