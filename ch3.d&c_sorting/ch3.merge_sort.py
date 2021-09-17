def merge(lst, temp, low, mid, high):
        i = low
        j = mid+1
        for k in range(low, high+1): 
            if i > mid:             
                temp[k] = lst[j] 
                j += 1
            elif j > high:
                temp[k] = lst[i] 
                i += 1
            elif lst[j] < lst[i]:
                temp[k] = lst[j] 
                j += 1
            else:
                temp[k] = lst[i] 
                i += 1
        for k in range(low, high+1):
            lst[k] = temp[k]     
                         
def merge_sort(lst, temp, low, high):
    if high <= low: 
        return None
    mid = low + (high - low) // 2
    merge_sort(lst, temp, low, mid) 
    merge_sort(lst, temp, mid + 1, high) 
    merge(lst, temp, low, mid, high) 

lst = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
temp = [None] * len(lst)
print('정렬 전:\t', end='')
print(lst)
merge_sort(lst, temp, 0, len(lst)-1)   
print('정렬 후:\t', end='')
print(lst)





