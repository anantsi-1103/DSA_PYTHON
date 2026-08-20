class HashTable:

    def __init__(self,size):
            self.size = size
            self.table = [[] for _ in range(size)]

    def hashFunction(self,key):
            return key % self.size


    def insert(self,key):
            index = self.hashFunction(key)

            if key not in self.table[index]:
                self.table[index].append(key)

    def search(self,key):
            index = self.hashFunction(key)
            return key in self.table[index]
    
    def delete(self,key):
            index = self.hashFunction(key)

            if key in self.table[index]:
                   self.table[index].remove(key)
                   return True

            return False


h = HashTable(10)

h.insert(10)
h.insert(25)
h.insert(35)
h.insert(45)
h.insert(55)
h.insert(79)

print(h.table)

print(h.search(45))