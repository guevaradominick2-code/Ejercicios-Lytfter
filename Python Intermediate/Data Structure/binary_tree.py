class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def set_root(self, data):
        if self.root is not None:
            raise Exception("Tree already has a root")

        self.root = Node(data)
        return self.root

    def add_left(self, parent_node, data):
        if parent_node.left is not None:
            raise Exception("Left child already exists")

        parent_node.left = Node(data)
        return parent_node.left

    def add_right(self, parent_node, data):
        if parent_node.right is not None:
            raise Exception("Right child already exists")

        parent_node.right = Node(data)
        return parent_node.right

    def print_tree(self):
        self._print_node(self.root)

    def _print_node(self, node):
        if node is None:
            return

        print(node.data)
        self._print_node(node.left)
        self._print_node(node.right)


tree = BinaryTree()

root = tree.set_root("A")

node_b = tree.add_left(root, "B")
node_c = tree.add_right(root, "C")

tree.add_left(node_b, "D")
tree.add_right(node_b, "E")

tree.print_tree()