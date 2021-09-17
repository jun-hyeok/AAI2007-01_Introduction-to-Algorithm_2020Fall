cache = {}
def fib_memoized(n):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        result = n
        cache[n] = result
        return cache[n]
    result = fib_memoized(n - 1) + fib_memoized(n - 2)
    cache[n] = result
    return result

print(fib_memoized(7))
print(cache)







