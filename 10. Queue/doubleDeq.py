from collections import deque



dp = deque()

# insert at rear

dp.append(10)
dp.append(20)

# insert at front

dp.appendleft(50)

print(dp)


# delete from rear

# dp.pop()

print(dp)

# remove fron front

# dp.popleft()

print(dp)

# front element

print(dp[0])
print(dp[-1])