M = 3
N = 4

def get_min(a, b):
  return a if a < b else b

def min_cost_recursion(cost, i, j):
  if i == 0 and j == 0: 
    return mat[0][0]
  if i == 0:                
    return min_cost_recursion(mat, 0, j-1) + mat[0][j]
  if j == 0:                
    return min_cost_recursion(mat, i-1, 0) + mat[i][0]
  a = min_cost_recursion(mat, i - 1, j)
  b = min_cost_recursion(mat, i, j - 1)
  return get_min(a, b) + mat[i][j]

mat = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print(min_cost_recursion(mat, M - 1, N - 1))

