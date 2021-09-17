def factorial_iteration(n):
   result = 1
   for i in range(1, n+1):
       result *= i
   return result

def factorial_recursion(n):
   if n <= 1:
       return 1
   else:
       return n * factorial_recursion(n-1)

print(factorial_iteration(5))
print(factorial_recursion(5))

