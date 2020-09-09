# Permutations of an array calculated recusively
# n is the length of the array used to spot a permutation
# rem is the remaining elements of the array
# perm is the current permutation

def permutation(n, rem, perm = []):
  if len(perm) == n:
    pass # Process here
  else:
    for v in range(len(rem)):
      perm.append(rem[v])
      new_rem=rem[:v].append(rem[v+1 if v!=len(rem)-1 else None:])
      permutation(n, new_rem, perm)

