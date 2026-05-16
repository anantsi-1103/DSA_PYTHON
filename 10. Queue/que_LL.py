class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

    

class Queue:

    # constructor -> 
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue
    def enqueue(self,data):

        newNode = Node(data)

        if self.rear is None:
            self.front = self.rear = newNode
            return 

        self.rear.next = newNode
        self.rear = newNode


    def dequeue(self):
         
        if self.front is None:
            print("Queue is Empty")
            return 

        temp = self.front

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        
        print(temp.data , "- Removed")

    def display(self):

        temp = self.front

        while(temp):
            print(temp.data ,end= " -> ")
            temp = temp.next


        print("None")

        
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()


q.dequeue()

    
q.display()