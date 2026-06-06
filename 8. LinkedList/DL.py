class Node:
    # oops -> Constructor
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    # Insert at begining -> 

    def insert_begin(self,data):

        # new node ka creation krdiya
        newNode = Node(data)


        # LL empty -> head  -> new node ko hi head bana dena 

        if self.head is None:
            self.head = newNode
            return
        

        # Data Exist

        # newnode ne head node ko point kra
        newNode.next = self.head
        # head ke prev n jo uske piche hai - newnode ko point kra 
        self.head.prev = newNode
        # head ab newnode ko refer krdo
        self.head = newNode

    def insert_end(self,data):

  # new node ka creation krdiya
        newNode = Node(data)


        # LL empty -> head  -> new node ko hi head bana dena 

        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head


        while temp.next:
            temp = temp.next


        temp.next = newNode
        newNode.prev = temp


    def insert_position(self,position, data):


        # position -> 1 
        if position == 1:
            self.insert_begin(data)
            return
        
        # more than 1
        newNode = Node(data)
        temp = self.head
        count = 1

        # 2 - 1 -> 1
        while temp and count < position - 1:
            temp = temp.next
            count +=1

        if temp is None:
            print("Out of Range")
            return
        
        newNode.next = temp.next
        newNode.prev = temp


        if temp.next:
            temp.next.prev = newNode
        

        temp.next = newNode


    def delete_begining(self):

        if self.head is None:
            print("list is empty")
            return
        
        self.head = self.head.next

        if self.head:
            self.head.prev = None



    def delete_end(self):

        if self.head is None:
            print("list is empty")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None


    def search(self,key):

        temp = self.head
        count = 1

        while temp:

            if temp.data == key:
                print(f"Element found at Position : {count}")
                return

            temp = temp.next
            count +=1

        print("Element Not found")


    def displayForward(self):
        
        if self.head is None:
         print("list is empty")
         return
           

        temp  = self.head

        while temp:

            print(temp.data ,end =  " <-> ")
            temp = temp.next

        print("None")


    def displayBackward(self):
        
        if self.head is None:
         print("list is empty")
         return
           

        temp  = self.head

        # to find the end
        while temp.next:
            temp = temp.next

        
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")

        

dl = DoublyLinkedList()


dl.insert_begin(20)
dl.insert_begin(46)
dl.insert_begin(65)
dl.insert_end(12)
dl.insert_begin(99)
dl.insert_end(43)

dl.displayForward()
dl.displayBackward()