'''
Created on 19-Sep-2017

@author: sauravrai
'''
RED="RED"
BLACK="BLACK"

        
class NilNode(object):
    def __init__(self):
        self.colour = BLACK

"""We define NIL to be the leaf sentinel of our tree."""
NIL = NilNode()


class Node(object):
    def __init__(self, key):
        self.key = key
        self.colour = RED
        self.left = NIL
        self.right = NIL
        self.p = NIL
        
class Tree(object):
    def __init__(self):
        self.root = NIL

    
    def inorder(self,z):
        if z is NIL:
            return
        if (z!=NIL):
            self.inorder(z.left)
            print z.key ,z.colour
            self.inorder(z.right)

    
    def left_rotate(self,T, x):    
        assert (x.right !=NIL )
        y = x.right
        x.right = y.left
        if y.left != NIL:
            y.left.p = x
        y.p = x.p
        if x.p == NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y


    def right_rotate(self,T, x):
        assert (x.left != NIL)
        y = x.left
        x.left = y.right
        if y.right != NIL:
            y.right.p = x
        y.p = x.p
        if x.p == NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y


    def tree_insert(self,T, z):
        y = NIL
        x = T.root  
        #   print 'Node.key', z.key
        #   print 'x.key', x.key
        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        #print 'x or parent of z is',z.p
        
        #print 'z key', z.key
        if z.p == NIL:
            tree.root = z
        elif z.key < z.p.key:
            z.p.left = z
        else:
            z.p.right = z  
        z.left =NIL
        z.right=NIL 
        z.colour =RED
        #print'z',z
        #print 'z parent in insert function is',z.p.key
        #print 'z parent colour in insert function is',z.p.colour
        self.rb_insert(T,z)
            
            
    
    def rb_insert(self,T, x):
        #x.colour = RED
        #print'z',x
        #print'z colour',x.colour
        #print'z parent',x.p.key
        #print'z parent colur',x.p.colour
        while x != T.root and x.p.colour == RED:
            if x.p == x.p.p.left:
                y = x.p.p.right
                if y.colour == RED:
                    x.p.colour = BLACK
                    y.colour = BLACK
                    x.p.p.colour = RED
                    x = x.p.p
                else:
                    if x == x.p.right:
                        x = x.p
                        T.left_rotate(self, x)
                    x.p.colour = BLACK
                    x.p.p.colour = RED
                    self.right_rotate(self, x.p.p)
            else:
                y = x.p.p.left
                if y.colour == RED:
                    x.p.colour = BLACK
                    y.colour = BLACK
                    x.p.p.colour = RED
                    x = x.p.p
                else:
                    if x == x.p.left:
                        x = x.p
                        self.right_rotate(self, x)
                    x.p.colour = BLACK
                    x.p.p.colour = RED
                    T.left_rotate(self, x.p.p)
        T.root.colour = BLACK

    def RB_Transplant(self,T,u,v):
        if u.p == NIL:
            T.root= v
        elif u == u.p.left:
            u.p.left= v
        else:
            u.p.right= v
        if v is not None:
            v.p= u.p
    
    def Minimum_BST(self,node):
        while node.left is not NIL:
            node= node.left
        return node
    def RedBlack_Delete(self,T,z):
        y= z
        colour= y.colour
        if z.left == NIL:
            x= z.right
            self.RB_Transplant(T,z,z.left)
        elif z.right == NIL:
            x= z.left
            self.RB_Transplant(T,z,z.left)
        else:
            y= self.Minimum_BST(z.right)
            colour= y.colour
            x= y.right
            if y.p == z:
                x.p= y
            else:
                self.RB_Transplant(T,z,z.left)
                y.right= z.right
                y.right.p= y
            self.RB_Transplant(T,z,y)     
            y.left= z.left
            y.left.p= y
            y.colour= z.colour
        if colour== BLACK:
            self.RB_Delete_Fixup(T,x)  

    def RB_Delete_Fixup(self,T,x):
        while x != T.root and x.colour == BLACK:
            if x == x.p.left:
                w= x.p.right
                if w.colour == RED:
                    w.colour= BLACK
                    x.p.colour= RED
                    self.left_rotate(T, x.p)
                    w= x.p.right
                if w.left.colour == BLACK and w.right.colour == BLACK:
                    w.colour= RED
                    x= x.p
                elif(w.right.colour == BLACK):
                    w.left.colour= BLACK
                    w.colour= RED
                    self.right_rotate(T, w)
                    w= x.p.right
                w.colour= x.p.colour
                x.p.colour= BLACK
                w.right.colour= BLACK
                self.left_rotate(T, x.p)
                x= T.root
            else:
            
                    w= x.p.left
                    if w.colour == RED:
                        w.colour= BLACK
                        x.p.colour= RED
                        self.right_rotate(T, x.p)
                        w=   x.p.right
                    if w.left.colour == BLACK and w.right.colour == BLACK:
                        w.colour= RED
                        x= x.p
                    elif(w.left.colour == BLACK):
                        w.right.colour= BLACK
                        w.colour= RED
                        self.left_rotate(T, w)
                        w= x.p.left
                    w.colour= x.p.colour
                    x.p.colour= BLACK
                    w.left.colour= BLACK
                    self.right_rotate(T, x.p)
                    x= T.root
            x.colour= BLACK
                
                
    def searchBST(self,node,value):
        
        while node is not None:
        
            if node == NIL:
                print "The Node your searching is not present in the tree"
                return False
            
            if(node.key == value):
                return node
            if value < node.key:
                node= node.left
            elif value > node.key:
                node= node.right
        return False    

'''main program'''
if __name__ == "__main__":
    print'Enter the elements of the Tree\n'
    tree =Tree()
    A=[11, 2,14,1,7,15,5,8,4]
    for i in A:
        tree.tree_insert(tree,Node(i))

print'The elements of the tree are:'

tree.inorder(tree.root)
    
a= tree.searchBST(tree.root, 4)
print a
tree.RedBlack_Delete(tree, a)

print "After Deletion of the node"
print'The contents of the table are:'
tree.inorder(tree.root)
    
