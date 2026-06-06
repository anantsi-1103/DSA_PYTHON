class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




class Stack:

    def __init__(self):
        self.top = None

    # push

    def push(self,data):

        # create Node
        newNode = Node(data)

        newNode.next = self.top
        self.top = newNode

        print(f"{data} Pushed")


    
    def pop(self):

        if self.top is None:
            print("Stack is Underflow")
            return

        removed = self.top.data
        self.top = self.top.next

        print(f"Removed :  {removed} popped" )

    
    def peek(self):


        if self.top is None:
            print("Stack is Empty")
            return
        
        print("Top Element : ", self.top.data)



    # Check Empty

    def isEmpty(self):
        return self.top is None
    

    def display(self):

        if self.top is None:
            print("Stack is Empty")
            return
         
        temp = self.top

        print("Stack Elements : ")

        while temp:

            print(temp.data)

            temp = temp.next



s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(50)
s.push(60)

s.display()

s.peek()

s.pop()

s.peek()


# HELLO
# OLLEH