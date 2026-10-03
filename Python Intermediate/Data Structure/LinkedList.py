class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)

        # Si la lista está vacía
        if self.head is None:
            self.head = new_node
            return

        # Recorremos hasta encontrar el último nodo
        current = self.head

        while current.next is not None:
            current = current.next

        # Conectamos el último nodo con el nuevo
        current.next = new_node

    def delete(self, data):
        # Si la lista está vacía
        if self.head is None:
            return

        # Si el nodo que queremos borrar es el primero
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        # Buscamos el nodo anterior al que queremos eliminar
        while current.next is not None:

            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def print_all(self):
        current = self.head

        if current is None:
            print("Lista vacía")
            return

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()

ll = LinkedList()

ll.insert_front(10)
ll.insert_front(20)
ll.insert_front(13)

ll.print_all()

ll.insert_back(30)

ll.print_all()

ll.delete(10)

ll.print_all()