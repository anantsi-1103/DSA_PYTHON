class Queue:

    def __init__(self):
        self.queue = []


    # insert
    def enqueue(self,data):
        self.queue.append(data)
        print(data," - Inserted")


    # remove 
    def dequeue(self):

        if(len(self.queue)) == 0:
            print("Queue is Empty")
            return
        
        removed = self.queue.pop(0)
        print(removed, "- Removed")


    # front
    def front(self):

        if(len(self.queue)) == 0:
            print("Queue is Empty")
            return
        
        print("Front Element : ", self.queue[0])
    

    # Check Empty

    def isEmpty(self):
        if(len(self.queue) == 0):
            print("Queue is Empty")
        else:
            print("Queue is not Empty")


    def size(self):
        print("Size : ",len(self.queue))

    
    def display(self):
        print(self.queue)


    def removeByNumber(self, key):
        
        for i in range(len(self.queue)):
            if(self.queue[i] == key):
                self.queue.pop(i)
                return "Removed"
        return("Element not Found")


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

q.front()

q.dequeue()

q.front()


q.display()
print(q.removeByNumber(30))
q.display()