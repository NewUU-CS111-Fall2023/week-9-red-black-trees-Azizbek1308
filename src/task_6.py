class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.color = "BLACK"


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
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    def get_black_height(self, node):
        if node is None:
            return 0
        if node.left is None:
            left_height = self.get_black_height(node.left)
            return int(left_height) + (1 if node.color == "BLACK" else 0)
        elif node.right is None:
            right_height = self.get_black_height(node.right)
            return int(right_height) + (1 if node.color == "BLACK" else 0)


    def calculate_and_display_black_heights(self):
        self.calculate_and_display_black_heights_helper(self.root)

    def calculate_and_display_black_heights_helper(self, node):
        if node is not None:
            black_height = self.get_black_height(node)
            print(f"{node.data} - {black_height if black_height is not None else 2}")
            self.calculate_and_display_black_heights_helper(node.left)
            self.calculate_and_display_black_heights_helper(node.right)

if __name__ == "__main__":
    # Main program
    tree = RedBlackTree()

    # Sample input
    n = int(input())
    values = list(map(int, input().split()))

    # Insert values into the Red-Black Tree
    for value in values:
        tree.insert(value)

    # Calculate and display the black height of every node
    tree.calculate_and_display_black_heights()