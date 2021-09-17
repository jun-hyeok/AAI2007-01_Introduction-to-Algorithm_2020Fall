class BinaryHeap:          
    def __init__(self):  
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
        
    def enheap(self, item):
        self.items.append(item)
        self.upheap(self.size() - 1)
         
    def deheap(self): 
        if self.size() == 0:
            return None
        minimum = self.items[0]
        self.swap(0, -1)
        del self.items[-1]
        self.downheap(0)
        return minimum
    
    def downheap(self, i): 
        while 2*i + 1 <= self.size()-1:
            k = 2*i + 1  
            if k < self.size()-1 and self.items[k][0] > self.items[k+1][0]: 
                k += 1  
            if self.items[i][0] < self.items[k][0]:
                break
            self.swap(i, k)
            i = k
            
    def upheap(self, i): 
        while i > 0 and self.items[((i-1)//2)][0] > self.items[i][0]: 
            self.swap(i, (i-1)//2)
            i = (i-1)//2
      
def classroom_assignment(C):
    C.sort(key = lambda x: x[0])
    depth = 0
    solution_set = BinaryHeap()
    for c in C:
        if solution_set.size() == 0:
            room = [c[1], depth, [c]]
            solution_set.enheap(room)
        else: 
            current_room = solution_set.deheap()            
            if c[0] >= current_room[0]:
                current_room[2].append(c)
                current_room[0] = c[1]
                solution_set.enheap(current_room)
            else:
                depth += 1
                room = [c[1], depth, [c]]
                solution_set.enheap(room)
                solution_set.enheap(current_room)
    return solution_set
        
C =   [[900, 1030, 'a'],  [900, 1230,'b'], [900, 1030,'c'], 
       [1100,  1230,'d'], [1100, 1400, 'e'], [1300, 1430,'f'],
       [1300, 1430, 'g'], [1400, 1630,'h'], [1500, 1630, 'i'], 
       [ 1500, 1630, 'j']]

result = classroom_assignment(C)
for i in range(result.size()): 
    i = result.deheap()
    print(i[1], i[2])

