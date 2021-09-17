def partition(lst, low, high): 
    x = lst[high] 
    i = low
    for j in range(low, high): 
        if lst[j] <= x: 
            lst[i], lst[j] = lst[j], lst[i] 
            i += 1
    lst[i], lst[high] = lst[high], lst[i] 
    return i

def qselect(lst, low, high, k):
    pi = partition(lst,low,high) 
    if pi == k - 1:
        return lst[pi] 
    elif pi < k - 1:
        return qselect(lst, pi+1, high, k)
    else:
        return qselect(lst, low, pi-1, k)







