def sum(lst, n):
    result = 0
    for i in range(n):
        result = result + lst[i]
    return result

lst = [10, 7, 11, 5, 13, 8]
n = len(lst)
print(sum(lst, n))
    
    