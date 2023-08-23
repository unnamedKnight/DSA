"""
Implementation of DFS
"""


class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def deque(self):
        if len(self.items):
            return self.items.pop(0)

    def peek(self):
        if len(self.items):
            return self.items[0].value

    def __len__(self):
        return len(self.items)


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value) -> None:
        self.root = Node(value)

    def level_order(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = []

        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.deque()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return traversal



tree = Tree(3)
tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

print(tree.level_order(tree.root))