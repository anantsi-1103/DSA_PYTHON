class Stack:


    def __init__(self):
        self.stack = []

    
    # Push

    def push(self,data):

        self.stack.append(data)
        print(f'{data} : Data pushed into a Stack')


    def pop(self):

        if(self.is_Empty()):
            print("Stack Underflow")
            return
        
        removed = self.stack.pop()
        print(f'{removed} : Data remove from a Stack')


    
    def peek(self):

        if(self.is_Empty()):
            print("Stack is Empty")
            return
        
        
        print("Top Element is ", self.stack[-1])


    def is_Empty(self):

        return len(self.stack) == 0
    

    def size(self):
        return len(self.stack)
    


    def display(self):

        if self.is_Empty():
            print("Stack is Empty")
            return
        
        print("Stack Elements :")

        for i in reversed(self.stack):
            print(i)


    def reverse_String(string): #hello
        stack = [] # h,e,l,l,o

        for ch in string: # h
            stack.append(ch)

        reverse = ""

        while stack:
            # reverse += stack.pop()
            reverse = reverse + stack.pop()
                    # o + l
                    # ol + l
                    # oll + e
                    # olle + h
                    # olleh
        return reverse
    
  

# s = Stack()


# s.push(20)
# s.push(45)
# s.push(76)
# s.push(2)
# s.push(87)

# s.display()

# s.pop()

# s.display()

# s.peek()