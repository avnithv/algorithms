# Calculate maximum sum of a subarray given the array
arr = [] # Input
# O(n) solution - For each position k, calculate maximum
# subarray ending at that position

# Either the subarray only contains the element at point k
# or the subarray consists of a subarray that ends at 
# position k - 1

best = arr_sum = 0
for k in range(len(arr)):
  arr_sum = max(arr_sum, arr_sum + arr[k])
  best = max(best, arr_sum)
print(best)

# This algorithm is called Kadane's algorithm
