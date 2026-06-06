jobs = [
    ("J1", 50, 2),
    ("J2", 15, 1),
    ("J3", 10, 2),
    ("J4", 25, 2)
]

# 50 , 25 ,  15 , 10 

# Sort by profit in descending 

jobs.sort(key = lambda x : x[1] , reverse=True)

max_deadline = max(job[2] for job in jobs)

slots = [None] * max_deadline
total_profit = 0

for j_id , profit , deadline in jobs:
    for j in range(deadline -1, -1, -1):

        if slots[j] is None:
            slots[j] = j_id
            total_profit += profit
            break

print("Selected Job id : ", slots)
print("Maximum Profit : ", total_profit)
