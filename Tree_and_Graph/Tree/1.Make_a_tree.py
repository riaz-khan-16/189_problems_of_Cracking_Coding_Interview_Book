class Node:

    def __init__(self,value):
        self.value=value
        self.children=[]
    def add_child(self,childnode):
        self.children.append(childnode)


def print_tree(node, level=0):
    if node is not None:
        print("  " * level + str(node.value))
        for child in node.children:
            print_tree(child, level + 1)




root=Node('A')
child1=Node('B')
child2=Node('C')
child3=Node('D')
child4=Node('E')




root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)

grand_child1=Node('X')
grand_child2=Node('Y')
grand_child3=Node('Z')

child1.add_child(grand_child1)
child1.add_child(grand_child2)
child1.add_child(grand_child3)

print_tree(root, level=0)