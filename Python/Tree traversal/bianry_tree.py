class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value) -> None:
        self.root = Node(value)

    def pre_order(self, start: int, traversal: list[int]):
        if start is None:
            return
        traversal.append(start.value)

        self.pre_order(start.left, traversal)
        self.pre_order(start.right, traversal)
        return traversal

    def inorder(self, start: int, traversal: list[int]):
        if start is None:
            return

        self.pre_order(start.left, traversal)
        traversal.append(start.value)
        self.pre_order(start.right, traversal)
        return traversal

    def postorder(self, start: int, traversal: list[int]):
        if start is None:
            return

        self.pre_order(start.left, traversal)
        self.pre_order(start.right, traversal)
        traversal.append(start.value)
        return traversal


tree = Tree(3)
tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right.left = Node(8)
tree.root.right.right = Node(9)

# print(tree.root.value)
# print(tree.root.left.value)
# print(tree.root.right)


print(tree.pre_order(tree.root, []))
