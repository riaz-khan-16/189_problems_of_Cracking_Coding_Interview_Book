# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
#               at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 



class Node:
    def __init__(self,value):
           self.value=value
           self.right=None
           self.left=None
    def insert_left(self, new):
           new=Node(new)
           self.left=new
    def insert_right(self, new):
           new=Node(new)
           self.right=new    

    #          A
    #        /   \
    #     B        C
    #    /  \     /  \
    #  B1    B2   C1  C2
           

           
tree=Node('A')
tree.insert_left('B')
tree.insert_right('C')

tree.left.insert_left('B1')
tree.left.insert_right('B2')

tree.right.insert_left('C1')
tree.right.insert_right('C2')


# now make a bfs

queue=[tree]
while queue:
      level=[]
      for i in range(len(queue)):
            node=queue.pop(0)
            level.append(node.value)
            if node.left:
                  queue.append(node.left)
            if node.right:
                  queue.append(node.right)
                  
      print(level)


