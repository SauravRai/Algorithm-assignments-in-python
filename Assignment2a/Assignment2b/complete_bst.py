'''
Created on 17-Aug-2017

@author: sauravrai

This is the python program for Binary Search Tree

'''
class StackNode:
 
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data 
        self.next = None
 
class Stack:
     
    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None
        
    
    def display(self):
        temp =self.root 
        while(temp):
            print temp.data
            temp=temp.next
      
 
    def isEmpty(self):
        return True if self.root is None else  False
 
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root 
        self.root = newNode
        
     
    def pop(self):
        temp=self.root
        if temp.next!=None:
            self.root = self.root.next
            popped = temp.data
            return popped
     
    def top(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data
    


class Node:
    def __init__(self,data,parent):
        self.left = None
        self.right = None
        self.data = data
        self.parent=parent
    
    
class bst:
    def __init__(self,data,parent):
        
        self.root = Node(data,parent)
        #print "self.root",self.root
    
    def search(self,data):
        if(self.root == None):
            print "Tree is empty"
        else:
            temp = self.root
            while(temp!= None):
                if(temp.data==data):
                    #print "Element is present"
                    return temp
                elif(temp.data > data):
                    temp = temp.left
                else:
                    temp = temp.right
            return temp
                    
    def recursiveBST(self, node, data,parent):            
        if node is None:
            node = Node(data,parent)                
        elif node.data > data:
            parent = node
            node.left = self.recursiveBST(node.left, data,parent)
        elif  node.data < data:
            parent = node
            node.right = self.recursiveBST(node.right, data,parent)

        return node
    
    def insert(self, data,parent):
        self.root = self.recursiveBST(self.root, data,parent)
   
    def preorder(self,node):
        if node is None:
            return
        else:
            print node.data
            self.preorder(node.left)
            self.preorder(node.right)
    
            
    def inorder(self,node):
        if node is None:
            return
        if (node!=None):
            self.inorder(node.left)
            print node.data
            self.inorder(node.right)


    
    
    
    def postorder(self,node):
        if node is None:
            return
        else:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data
    
    
    def minimum(self,node):
        if node == None:
            print'The tree is empty'
            
        """Returns the node with the smallest key in the subtree rooted by this node."""
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def maximum(self,node):
        if node == None:
            print'The tree is empty'
        """Returns the node with the smallest key in the subtree rooted by this node."""
        current = node
        while current.right is not None:
            current = current.right
        return current.data
    
    def find_succesor(self,data,node):
        if node == None:
            print'The tree is empty\n'
        srch_node = self.search(data)
        if srch_node == None:
            print'The element is not present in the tree\n'
        else:
            if srch_node.right != None:
                return self.minimum(srch_node.right)
            y=srch_node.parent
            while y !=None and srch_node == y.right:
                srch_node = y
                y = y.parent
            return y.data
        
    def iterativein(self,node):
        stack = Stack()
        stack.push((None,None))
        data = (node,1)
        stack.push(data)
        while(stack.top!=None):
            address,purpose = stack.pop()
            if(address!=None):
                if purpose == 1:
                    stack.push((address,0))
                    #if(address.left!=None):
                    stack.push((address.left,1))
                if purpose == 0:
                    print address.data
                    #if address.right!=None:
                    stack.push((address.right,1))    

    def iterativepre(self,node):
        stack=Stack()
        stack.push((None,None))
        stack.push(node)
        while(stack.top!=None):
            address = stack.pop()
            if(address!= None):
                print address.data
                stack.push(address.right)
                stack.push(address.left)
                 
# Given a binary search tree and a key, this function
# delete the key and returns the new root
    def deleteNde(self,node,data):

    # Base Case
        if node is None:
            return node 
        temp=node

    # If the key to be deleted is similiar than the root's
    # key then it lies in  left subtree
        if data < temp.data:
            temp.left = self.deleteNde (temp.left,data)

    # If the key to be delete is greater than the root's key
    # then it lies in right subtree
        elif(data > temp.data):
            temp.right = self.deleteNde (temp.right, data)

    # If key is same as root's key, then this is the node
    # to be deleted
        else:
        
        # Node with only one child or no child
            if temp.left is None :
                temp1 = temp.right 
                temp = None 
                return temp1 
            
            elif temp.right is None :
                temp1 = temp.left 
                temp = None
                return temp1

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
            temp1 = self.minimum(temp.right)

        # Copy the inorder successor's content to this node
            temp.data = temp1.data

        # Delete the inorder successor
            temp.right = self.deleteNde(temp.right , temp1.data)


        return temp

def main():
   
    
    opt= 'y'
    while opt == 'y':
        print'The following options can be performed in this program\n'
        print'\n1.Preorder traversal\n2.Inorder traversal\n3.Postorder traversal\n4.Mininmum element\n5.Maximum element\n6.Succesor of the element\n7.Search for the element\n8.Delete an element in the tree\n9.Iterative Inorder\n10.Iterative Preorder\n'  
    
        choice= input("Enter your choice:\t")
        #get file choice from user
        if choice == 1:
            print "Preorder Traversal of the tree:"
            binaryST.preorder(binaryST.root)

        elif choice == 2:
            print "inorder"
            binaryST.inorder(binaryST.root)
        
        elif choice == 3:
            print "postorder"
            binaryST.postorder(binaryST.root)

        elif choice == 4:
            print "Minimum element of the tree\n"
            minimum=binaryST.minimum(binaryST.root)
            print minimum
        
        elif choice == 5:
            print "Maximum element of the tree\n"
            maximum=binaryST.maximum(binaryST.root)
            print maximum
            
        elif choice == 6:
            m=input("Enter the element of which you want to find the sucessor in the tree:\n")
            sucessor=binaryST.find_succesor(m,binaryST.root)
            print sucessor

        elif choice == 7:
            srch=input('Enter the value you want to search in the tree\n')
            search = binaryST.search(srch)
            if(search == None):
                print "Element is absent in the tree\n"
            else:
                print "Element is Present in the tree\n"
            
            
        elif choice == 8:
            d=input("Enter the element you wish to delete in the tree")
            binaryST.deleteNde(binaryST.root,d)

        elif choice == 9:
            print 'The iterative inorder traversal of the tree is\n'
            binaryST.iterativein(binaryST.root)
        
        elif choice == 10:    
            print 'The iterative preorder traversal of the tree is\n'
            binaryST.iterativepre(binaryST.root)
        
        else:
            print"Wrong input"
         
        print "\nDo u wish to contiunue"
        opt = raw_input("y/n")
        
            

n = input("Enter the root of the Binary Search Tree:")
binaryST = bst(n,None)
print'Enter the elements of the Tree\n'
A=[int(x) for x in raw_input().split()]
for i in A:
    binaryST.insert(i,binaryST.root)

main()

'''
# For checking various addresses in the tree
binaryST.insert(33,binaryST.root)
binaryST.insert(25,binaryST.root)
binaryST.insert(60,binaryST.root)
binaryST.insert(20,binaryST.root)
binaryST.insert(100,binaryST.root)
print "BinaryST:",binaryST
print "Binary.root",binaryST.root
print binaryST.root.data,binaryST.root.parent
print binaryST.root.left.data,binaryST.root.left.parent
print binaryST.root.left.left.data,binaryST.root.left.left.parent
#
'''









