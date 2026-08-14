class Node:
    data : str

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise Exception ("Stack is empty")
        
        data = self.top.data
        self.top = self.top.next
        return data

    def print_stack(self):
        current = self.top

        while current is not None:
            print(current.data)
            current = current.next

stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")

stack.print_stack()

stack.pop()

stack.print_stack()

