class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            p = self.items.pop()
            print(f"pop: {p.value}" )
            return p
    
    def peek(self):
        if not self.is_empty():
            pe = self.items[-1].value
            print(f"peak: {pe}" )
            return pe
    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)

        else:
            message = f"Traversal_type {traversal_type} is not supported"
            return message


    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print((start.left, traversal))
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right)

        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left)
            traversal = self.postorder_print(start.right)
            traversal += (str(start.value) + "-")

        return traversal

    def levelorder_print(self, start):
        if start is None:
            return None

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

print(tree.print_tree("levelorder"))

def test_append():
    items = []
    for i in range(1, 8):
        items.append(i)
    print("append list:", items)
    print("###############################")
    for i in range(1, 8):
        print(items.pop())

    print("###############################")
    print(items)

def test_insert():
    items = []
    for i in range(1, 8):
        items.insert(0, i)

    print(items)

f1 = test_append()
f2 = test_insert()

