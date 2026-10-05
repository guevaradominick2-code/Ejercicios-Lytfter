class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        # Si la cola está vacía
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            # El último nodo apunta al nuevo nodo
            self.rear.next = new_node

            # El nuevo nodo pasa a ser el último
            self.rear = new_node

    def dequeue(self):
        # Si la cola está vacía
        if self.front is None:
            return None

        # Guardamos el dato del primer nodo
        data = self.front.data

        # El segundo nodo pasa a ser el primero
        self.front = self.front.next

        # Si después de eliminar no quedan nodos
        if self.front is None:
            self.rear = None

        return data

    def print_all(self):
        current = self.front

        if current is None:
            print("Cola vacía")
            return

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()

q = Queue()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")

q.print_all()

print(q.dequeue())

q.print_all()