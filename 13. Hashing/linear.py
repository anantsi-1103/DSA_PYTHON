size = 10


table = [None] * size

def insert(key):

    index = key % size

    while table[index] is not None:
        index = (index + 1) % size

    table[index] = key


insert(25)
insert(35)
insert(45)

print(table)
