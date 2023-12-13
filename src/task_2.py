class Node:
    def __init__(self, data):
        self.data = data
        self.color = Color.RED
        self.left = None
        self.right = None
        self.parent = None


class Color:
    RED = "RED"
    BLACK = "BLACK"


class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert(self, data):
        node = Node(data)
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

        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent is not None and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.left_rotate(node.parent.parent)
        self.root.color = Color.BLACK

    def print_tree(self):
        self.print_tree_helper(self.root)

    def print_tree_helper(self, node):
        if node is not None:
            print(f"({node.data}({node.color}) ", end="")
            self.print_tree_helper(node.left)
            self.print_tree_helper(node.right)
            print(")", end="")


tree = RedBlackTree()
if __name__ == "__main__":
    # Sample input
    values = list(map(int, input().split()))
    for value in values:
        tree.insert(value)

    # Print the tree
    tree.print_tree()