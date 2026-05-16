from collections import deque

def pallin(word):

    dp = deque(word)


    while len(dp) > 1:

        if dp.popleft() != dp.pop():
         return False
    
    return True

# remove all element 
# stack
# again queue

def reverse_queue(q):
    stack = []

    # q se nikal ke stack
    while q: 
       stack.append(q.popleft())

    # stack se nikal ke queue return
    while stack:
       q.append(stack.pop())

    return q


def generate(n):
   
    q = deque() 
    # 1

    q.append("1")

    for i in range(n):
       
        front = q.popleft()

        print(front)

        q.append(front+"0")
        q.append(front+"1")
      



generate(5)





# q = deque([1,2,3,4,5])

# print(q)
# print(reverse_queue(q))
# print(pallin("madam"))
# print(pallin("demo"))

# implement queue using stack
# sliding Window maximum
# stack using queue
# tree