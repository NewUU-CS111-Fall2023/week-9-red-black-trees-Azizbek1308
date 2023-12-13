class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insert_helper(node.left, data)
        elif data > node.data:
            node.right = self.insert_helper(node.right, data)
        return node

    def get_num_children(self, data):
        node = self.search(data)
        if node is not None:
            return self.count_children(node)
        return None

    def count_children(self, node):
        if node is None:
            return 0
        return self.count_children(node.left) + self.count_children(node.right) + 1

    def search(self, data):
        return self.search_helper(self.root, data)

    def search_helper(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search_helper(node.left, data)
        return self.search_helper(node.right, data)

    def print_children_counts(self):
        self.print_children_counts_helper(self.root)

    def print_children_counts_helper(self, node):
        if node is not None:
            self.print_children_counts_helper(node.left)
            print(node.data, "-", self.count_children(node) - 1)
            self.print_children_counts_helper(node.right)

if __name__ == "__main__":
    # Main program
    tree = BinaryTree()

    # Input
    values = list(map(int, input().split()))
    for value in values:
        tree.insert(value)

    # Display the number of children for each node
    tree.print_children_counts()