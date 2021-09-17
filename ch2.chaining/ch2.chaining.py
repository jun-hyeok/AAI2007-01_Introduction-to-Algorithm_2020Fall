class Node:    
        def __init__(self, key, data, link): 
            self.key   = key
            self.data  = data
            self.next  = link

class Chaining:
    def __init__(self, size):
        self.m = size           
        self.table = [None for x in range(size+1)] 
        
    def hash(self, key):
        return key % self.m

    def insert(self, key, data): 
        i = self.hash(key)
        p = self.table[i]
        while p != None:
            if key == p.key:   
                p.data = data  
                return None
            p = p.next 
        self.table[i] = Node(key, data, self.table[i])
    
    def search(self, key): 
        i = self.hash(key)
        p = self.table[i]
        while p != None:
            if key == p.key:  
                return p.data 
            p = p.next 
        return None  
    
    def delete(self, key):
        i = self.hash(key)
        p = self.table[i]
        previous = None 
        while p != None:
            if key == p.key:
                if previous == None: 
                    self.table[i] = p.next
                else:
                    previous.next = p.next
                return None
            previous = p
            p = p.next
                    
    def print_table(self): 
        for i in range(self.m):
            print('%2d' % (i), end='')
            p = self.table[i]
            while p != None:
                print('-->[', p.key,',', p.data, ']', end='')
                p = p.next;
            print()

if __name__ == '__main__':
    ht = Chaining(13)
    ht.insert(45, 'A') 
    ht.insert(27, 'B')   
    ht.insert(88, 'C')
    ht.insert(9, 'D')
    ht.insert(71, 'E')   
    ht.insert(60, 'F')      
    ht.insert(46, 'G')
    ht.insert(38, 'H')
    ht.insert(24, 'I') 
    print('해시 테이블:')
    ht.print_table()
    ht.delete(45)
    print('key 값이 45인 A를 삭제한 해시 테이블:')
    ht.print_table()