class HashTable:

    def __init__(self,size):
        self.size = size
        self.table = [None] * size


    def hashFunction(self,key):
        return key % self.size


    def insert(self,key):
        index = self.hashFunction(key)
        self.table[index] = key


    def search(self,key):
        index = self.hashFunction(key)

        if self.table[index] == key:
            return True
        return False

    def delete(self,key):
        index = self.hashFunction(key)
        if self.table[index] == key:
            self.table[index] = None
            return True
        return False


h = HashTable(10)


h.insert(10)
h.insert(25)
h.insert(36)
h.insert(41)
h.insert(49)
h.insert(88)
h.insert(55)


print(h.table)

print(h.search(25))
print(h.search(49))

print(h.delete(25))
print(h.search(25))
print(h.table)