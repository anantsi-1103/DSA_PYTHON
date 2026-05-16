class Deque:

    def __init__(self):
        self.deque = []

    # insert front
    def insertFront(self, data):
        # index -> 0 , element
        self.deque.insert(0, data)
        print(data, "inserted at front")

    # insert rear
    def insertRear(self, data):
        # add at the end
        self.deque.append(data)
        print(data, "inserted at rear")

    # delete front
    def deleteFront(self):

        if len(self.deque) == 0:
            print("Deque is empty")
            return

        removed = self.deque.pop(0)
        print(removed, "removed from front")

    # delete rear
    def deleteRear(self):

        if len(self.deque) == 0:
            print("Deque is empty")
            return
            # last element
        removed = self.deque.pop()
        print(removed, "removed from rear")

    # front element
    def getFront(self):

        if len(self.deque) == 0:
            print("Deque is empty")
            return

        print("Front:", self.deque[0])

    # rear element
    def getRear(self):

        if len(self.deque) == 0:
            print("Deque is empty")
            return

        print("Rear:", self.deque[-1])

    # display
    def display(self):
        print(self.deque)


dq = Deque()

dq.insertRear(10)
dq.insertRear(20)

dq.insertFront(5)

dq.display()

dq.deleteRear()

dq.display()

dq.deleteFront()

dq.display()