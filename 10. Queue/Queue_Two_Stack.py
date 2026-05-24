class QueueUsingStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    # insert
    def enqueue(self,data):
        self.stack1.append(data)
        print(data ," - Inserted")

    # remove
    def dequeue(self):
        if not self.stack1 and not self.stack2:
            print("Queue is Empty")
            return
        
        # move element only if stack2 empty
        # 2 stack se 1 queue
        if not self.stack2:
            while self.stack1:
             self.stack2.append(self.stack1.pop())

        removed = self.stack2.pop()
        print(removed, "- Removed")


    # front
    def front(self):

        if not self.stack1 and not self.stack2:
            print("Queue is Empty")
            return
        

        # 2 stack -> 1 Queue
        if not self.stack2:
            while self.stack1:
             self.stack2.append(self.stack1.pop())

        print("Front: ", self.stack2[-1])


q = QueueUsingStack()

q.enqueue(10) #
q.enqueue(20) #
q.enqueue(30)
q.enqueue(40)

q.front()

q.dequeue()

q.front()