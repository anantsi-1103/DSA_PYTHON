# size = 10

# table = [None] * size

# key = 25

# index = key % size


# table[index] = key

# print(table)



size = 10


table = [[] for _ in range(size)]

keys = [25,45,35, 47]

for k in keys:
    index = k % size
    table[index].append(k)


print(table)


def search(key):
    index = key % size

    return key in table[index]

# return 25 in table[5]
print(search(36))