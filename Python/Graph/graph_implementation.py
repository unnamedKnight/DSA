class Node():

    def __init__(self, value):
        self.value = value
        self.adjacentlist = []
        self.visited = False

class Graph():
    def BFS(self, node):

        queue = [node]
        node.visited = True

        traversal_list = []

        while queue:
            actual_node = queue.pop(0)
            traversal_list.append(actual_node.value)

            for element in actual_node.adjacentlist:
                if element.visited is False:
                    queue.append(element)
                    element.visited = True

        return traversal_list



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjacentlist.append(node2)
node1.adjacentlist.append(node3)
node1.adjacentlist.append(node4)
node2.adjacentlist.append(node5)
node2.adjacentlist.append(node6)
node4.adjacentlist.append(node7)

graph = Graph()
print(graph.BFS(node1))