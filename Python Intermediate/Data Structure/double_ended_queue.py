class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def push_right(self, data):

        new_node = Node(data)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node

        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise Exception ("Que is empty")

        data = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next
            self.head.previous = None

        return data

    def pop_right(self):
        if self.tail is None:
            raise Exception ("Que is empty")
    
        data = self.tail.data
    
        if self.head == self.tail:
            self.head = None
            self.tail = None
    
        else:
            self.tail = self.tail.previous
            self.tail.next = None
    
        return data

    def print_queue(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next




queue = DoubleEndedQueue()

queue.push_right("B")
queue.push_left("A")
queue.push_right("C")

queue.print_queue()

queue.pop_left()
queue.pop_right()
queue.print_queue()