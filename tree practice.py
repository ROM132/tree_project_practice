class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def sum_value(root):
    if root is None:
        return 0
    return root.data + sum_value(root.left) + sum_value(root.right)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)


node1.right = node2
node1.left = node4
node2.right = node3
node4.right = node6
node4.left = node5

print(sum_value(node1))
