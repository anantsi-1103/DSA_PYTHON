class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
            


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # insert at begining -> 
    def insert_Begining(self,data):

        # list is empty

        # List have number
        # create a new Node
        newNode = Node(data)

        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            return

        # new node mera head wale node ko point kr rha hai
        newNode.next = self.head
        # head ko shift krdunga new node pr 
        self.head = newNode

    def insert_End(self,data):

        # create a new Node
        newNode = Node(data)
    #   check
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
            return
        # tail ke next ko none ki jagah new node ko ref krdiya
        self.tail.next = newNode
        # tail ko new node pr transfer krdiya 
        self.tail = newNode

    # node ka data -> 100
    def delete(self,key):
        temp = self.head
        
        # first index pr hi value mil jaaye
        if temp and temp.data == key:
            self.head = temp.next
            return
        
        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return "Not Found"
        
        prev.next = temp.next

    def print_list(self):

        temp = self.head

        while temp:
            print(temp.data , end = " -> ")
            temp = temp.next

        print("None")

    def reverseList(self):

        prev = None
        curr = self.head

        while(curr):

            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data


    def detectCycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next #+1
            fast = fast.next.next #+2

            if slow == fast:
                return True
        return False

    def removeCycle(self):
        slow = self.head
        fast = self.head

        # Detect Cycle
        while fast and fast.next:
            slow = slow.next #+1
            fast = fast.next.next #+2

            if slow == fast:
                break

        # No Cycle
        if fast is None or fast.next is None:
            return "Not Found"
        
        # Find start of the cycle
        slow = self.head
        prev = None

        while slow != fast:
            prev = fast
            slow = slow.next
            fast = fast.next

        prev.next = None
    
        

ll = LinkedList()

ll.insert_End(1)
ll.insert_End(2)
ll.insert_End(3)
ll.insert_End(4)
ll.insert_End(5)

# ll.print_list()

# print(ll.delete(400))
# ll.print_list()


# ll.reverseList()

# ll.print_list()


print(ll.detectCycle())
ll.head.next.next.next.next.next = ll.head.next.next
print(ll.detectCycle())

ll.removeCycle()
print(ll.detectCycle())

