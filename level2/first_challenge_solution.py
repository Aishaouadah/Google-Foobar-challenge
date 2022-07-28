#Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. 
#  For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].
#post order perfect binary tree

class Node:
    def __init__(self,value,leftChild,rightChild):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def print_node(self):
        print("node",self.value,"left child ",self.leftChild,"right child",self.rightChild)


      
def construct_tree(h):
    root=2**h-1
    level=1 #number of nodes
    nodes=[]
    for i in range(1,root+1):
        nodes.append(Node(i+2,i,i+1))
        
    return nodes        


def  solution(h, q):
    root=2**h-1
    btree= construct_tree(h)
    output=[]
    for element in q:
        #FIXME #Find parent in btree
        parent=0
        output.append(parent)
        pass
    return parent


#HELPER
def print_tree(nodes):
    for element in nodes: element.print_node() 
  
#TEST
#solution(2, {19, 14, 28})
#solution(3, {19, 14, 28})

print_tree(construct_tree(3))