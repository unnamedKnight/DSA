class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


'''
Implementation of DFS
'''

class Tree:
    def __init__(self, value) -> None:
        self.root = Node(value)




tree = Tree(3)
tree.root.left = Node(4)
tree.root.right = Node(5)

tree.root.left.left = Node(6)
tree.root.left.right = Node(7)

tree.root.right.left = Node(8)
tree.root.right.right = Node(9)
