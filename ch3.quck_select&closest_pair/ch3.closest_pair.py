import math 
import copy 
  
def dist(p1, p2): 
    return math.sqrt((p1[0] - p2[0]) * 
                     (p1[0] - p2[0]) +
                     (p1[1] - p2[1]) * 
                     (p1[1] - p2[1]))  

def compute_closest_pair(P, n): 
    P.sort(key = lambda x: x[0]) 
    Q = copy.deepcopy(P) 
    Q.sort(key = lambda x: x[1])     
    return closest_pair(P, Q, n) 

def closest_pair(P, Q, n): 
    if n <= 3:  
        return brute_force(P, n)
    d = float('inf')
    cp = ()
    mid = n // 2
    midpoint = P[mid] 
    dl,cpl = closest_pair(P[:mid], Q, mid) 
    dr,cpr = closest_pair(P[mid:], Q, n - mid)   
    if dl <= dr:
        d = dl
        cp = cpl
    else:
        d = dr
        cp = cpr
    strip = []  
    for i in range(n):  
        if midpoint[0] - d  <= Q[i][0] <= midpoint[0] + d:  
            strip.append(Q[i]) 
    dmid, cpmid = strip_closest_pair(strip, len(strip), d, cp)
    if d <= dmid:
        return d, cp
    else:
        return dmid, cpmid

def brute_force(P, n): 
    min_val = float('inf')
    cp = ()
    for i in range(n): 
        for j in range(i + 1, n): 
            if dist(P[i], P[j]) < min_val: 
                min_val = dist(P[i], P[j])
                cp = (P[i], P[j])
                return min_val, cp
     
def strip_closest_pair(strip, size, d, cp):   
    dmid = d 
    cpmid = cp
    for i in range(size): 
        j = i + 1
        while j < size and (strip[j][1] - 
                            strip[i][1]) < dmid: 
            if dist(strip[i], strip[j]) <= dmid:
                dmid = dist(strip[i], strip[j])
                cpmid = (strip[i], strip[j])              
            j += 1
    return dmid, cpmid 
  
P = [(1, 1), (2, 2), (1, 3), (3, 6),  
     (9, 15), (8, 12), (4, 7), (9, 7),
     (4, 4), (5, 4), (3, 3), (6, 7), (8, 9), (9, 2)] 
n = len(P)
result = compute_closest_pair(P, n)  
print("The smallest distance and closest pair:", result)


P = [(1,11), (3,7), (5,3), (7,7), (9,6), (13,7), (15,11), (16,4)]
n = len(P)
result = compute_closest_pair(P, n)  
print("The smallest distance and closest pair:", result)


