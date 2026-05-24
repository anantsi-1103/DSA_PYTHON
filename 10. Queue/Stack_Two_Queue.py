from collections import deque

class StackUsingQueue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    
    # push
    def push(self,data):

        # append

        self.q2.append(data)

        # 
        while self.q1:
           self.q2.append(self.q1.popleft())

        
        self.q1, self.q2 = self.q2 , self.q1

        print(data, "- Inserted")


    def pop(self):

        if not self.q1:
            print("Stack is Empty")
            return
        

        removed = self.q1.popleft()
        print(removed , "- Removed")


    def top(self):

        if not self.q1:
            print("Stack is Empty")
            return
        
        print("Top: ",self.q1[0])


    def display(self):
        print("Stack: ", list(self.q1))


s = StackUsingQueue()


s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()

s.top()

s.pop()

s.top()