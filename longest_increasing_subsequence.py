arr = []

length = [1]

for k in range(1, len(arr)):
  length[k] = 1
  for i in range(k):
    if arr[k] > arr[i]:
      length[k] = max(length[k], length[i] + 1)