class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        self._insert_helper(node)

    def _insert_helper(self, node):
        # Perform a standard BST insertion
        parent = None
        current = self.root

        while current is not None:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        # Make the root black
        if node.parent is None:
            node.color = "BLACK"
        else:
            node.color = "RED"

    def printTree(self):
        self._print_helper(self.root)

    def _print_helper(self, node):
        if node is not None:
            print("(", end="")
            print(str(node.data) + "(" + node.color + ")", end="")
            self._print_helper(node.left)
            self._print_helper(node.right)
            print(")", end="")


# Main program
if __name__ == "__main__":
    tree = RedBlackTree()

    # Sample input
    values = list(map(int, input().split()))

    for value in values:
        tree.insert(value)

    # Print the tree
    tree.printTree()