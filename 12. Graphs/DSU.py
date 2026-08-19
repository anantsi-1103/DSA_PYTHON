class DSU:

    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n


    def find(self,x):
        # Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)

        # Already in the same set
        if rootA == rootB:
            return

        # Union

        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            # Same Rank
             self.parent[rootB] = rootA
             self.rank[rootA]+= 1

    def display(self):
       print("Parent : ", self.parent)
       print("Rank : ", self.rank)


dsu = DSU(6)

dsu.display()

print()
dsu.union(0,2)
dsu.display()

print()
dsu.union(1,3)
dsu.display()

print()
dsu.union(2,5)
dsu.display()

print(dsu.find(2))
print()
dsu.union(0,3)
dsu.display()

print()
dsu.union(0,4)
dsu.display()

