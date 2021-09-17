def partition(lst, low, high): 
    x = lst[high] 
    i = low 
    for j in range(low, high): 
        if lst[j] <= x: 
            lst[i], lst[j] = lst[j], lst[i] 
            i += 1
    lst[i], lst[high] = lst[high], lst[i] 
    return i 

def qsort(lst,low,high): 
    if low < high: 
        pi = partition(lst,low,high) 
        qsort(lst, low, pi-1) 
        qsort(lst, pi+1, high) 

lst = [10, 80, 30, 90, 40, 50, 70, 60]
print('정렬 전:\t', end='')
print(lst)
qsort(lst, 0, len(lst)-1)  
print('정렬 후:\t', end='')
print(lst)




