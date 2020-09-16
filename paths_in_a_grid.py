value = [[]]
n = len(value)
path_sum = [[0 for x in range(n)] for y in range(n)]

for x in range(len(path_sum)):
  for y in range(len(path_sum[x])):
    if x == 0 and y == 0:
      path_sum[x][y] = value[x][y]
    elif x == 0: 
      path_sum[x][y] = path_sum[x][y - 1] + value[x][y]
    elif y == 0:
      path_sum[x][y] = path_sum[x - 1][y] + value[x][y]
    else:
      path_sum[x][y]=max(path_sum[x-1][y],path_sum[x][y-1])+value[x][y]
    
