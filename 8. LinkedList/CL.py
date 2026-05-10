class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




class CircularLinkedList:

    def __init__(self):
        self.head= None

    
    def insert_begin(self,data):
        
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        newNode.next = self.head
        temp.next = newNode
        self.head = newNode


    def insert_end(self,data):
        
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        
        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = newNode
        newNode.next = self.head


    def deletefromBegin(self):

        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        

        temp = self.head


        while temp.next != self.head:
            temp = temp.next


        temp.next = self.head.next
        self.head = self.head.next

    def deletefromEnd(self):

        if self.head is None:
            print("List is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        

        temp = self.head


        while temp.next != self.head:
            temp = temp.next


        temp.next = self.head


    def display(self):
        # self empty 
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head

        while True:

            print(temp.data , end= " <-> ")
            temp = temp.next

            if temp == self.head:
                break
        print("(Head)")
    

        
cl = CircularLinkedList()

cl.insert_begin(20)
cl.insert_begin(30)
cl.insert_begin(40)
cl.insert_begin(60)
cl.insert_begin(80)

cl.display()
