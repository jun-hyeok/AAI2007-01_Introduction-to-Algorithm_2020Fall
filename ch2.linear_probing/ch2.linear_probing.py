class LinearProbing: 
    def __init__(self, size): 
        self.m = size
        self.k = [None for _ in range(size+1)]  
        self.d = [None for _ in range(size+1)]  

    def hash(self, key):
        return key % self.m  
    
    def insert(self, key, data): 
        initial_position = self.hash(key)  
        i = initial_position
        j = 0
        while True:  
            if self.k[i] == None or self.k[i] == '$': 
                self.k[i] = key   
                self.d[i] = data   
                return None         
            if self.k[i] == key:  
                self.d[i] = data  
                return None  
            j += 1                      
            i = (initial_position + j) % self.m   
            if i == initial_position: 
                break         
           
    def search(self, key): 
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None: 
            if self.k[i] == key:
                return self.d[i] 
            j += 1
            i = (initial_position + j) % self.m  
            if i == initial_position: 
                break                 
        return None 

    def delete(self, key): 
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.k[i] != None: 
            if self.k[i] == key:
                self.k[i] = '$' 
                self.d[i] = None
                return None
            j += 1
            i = (initial_position + j) % self.m  
            if i == initial_position: 
                break             
        return None  

    def print_table(self):
        for i in range(self.m):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.m):
            print('{:4}'.format(str(self.k[i])), ' ', end='')
        print()
        for i in range(self.m):
            print('{:4}'.format(str(self.d[i])), ' ', end='')
        print()
        
if __name__ == '__main__':
    ht = LinearProbing(13)
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
    print()
    print('key 값이 46인 data 검색 결과:')
    print('key 값이 46인 data = ', ht.search(46))
    print()
    ht.delete(60)
    ht.delete(46)
    print('key 값이 60인 F 삭제 후 키 값이 46인 G를 삭제한 해시 테이블:')
    ht.print_table()         
        


