'''
Created on 09-Aug-2017

@author: sauravrai
'''
# Python program to demonstrate insert operation in binary search tree 
#Recursive way 
# A utility class that represents an individual node in a BST
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        self.parent=None
        
def insert(root,node):
    if root is None:
        root = node
    else:
        current=root
            
        if current.val < node.val:
            if current.right is None:
                current.right = node
                current.right.parent = current
            else:
                insert(current.right, node)
            
        else:
                
            if current.left is None:
                current.left = node
                current.left.parent = current
            
            else:
                insert(current.left, node)
# A utility function to do inorder tree traversal
def inorder(rt): # left root right
    if rt:
        inorder(rt.left)
        print(rt.val)
        inorder(rt.right)
        
def preorder(rt): # root left right
    if rt:
        print(rt.val)    
        preorder(rt.left)
        preorder(rt.right) 


def postorder(rt): #  left right root
    if rt:
        postorder(rt.left)
        postorder(rt.right) 
        print(rt.val)

def main():

    #rt=int(raw_input('Enter the root of the tree'))
    val=input('Enter the value of the root')
    rt=Node(val)
    opt= 'y'
    while opt == 'y':
        print'1.Insert in the tree\n2.In order traversal of the tree\n3.Preorder Traversal of the Tree\n4.Postorder Traversal of the Tree'  
    
        choice= input("Enter menu choice:\t")
        #get file choice from user
        if choice ==1:
            value = int(raw_input('Enter the element to the BST\n'))
            insert(rt,Node(value))
            
        elif  choice == 2:
            inorder(rt)
        
        elif choice == 3:    
            preorder(rt)
        
        elif choice == 4:
            postorder(rt) 
        else:
            print"Wrong input"
         
        print "\nDo u wish to contiunue"
        opt = raw_input("y/n")
        
    print "Hii i'm out of the loop"
    return 
    
main()

        
