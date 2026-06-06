from collections import deque

d = deque()

# insert
d.append(20)
d.append(40)
d.append(60)
d.append(80)

print(d)

# delete
d.popleft()
print(d)

# front
print("front :",d[0])


# size
print("Size : ",len(d))