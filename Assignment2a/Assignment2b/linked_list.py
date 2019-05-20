'''
Created on 09-Aug-2017

@author: sauravrai

The Linked List implementation in python 
 '''
 
''' Node  class'''

class Node:
 
    ''' Function to initialise the node object'''
    def __init__(self, data):
        self.data = data   # Assign data 
        self.next = None   # Initialize next as null
 
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next
        
# This function is defined in Linked List class
    # Appends a new node at the end.  This method is
    # defined inside LinkedList class shown above */
    def enter_last(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
            new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        #    new node as head
            if self.head is None:
                self.head = new_node
                return
 
        # 5. Else traverse till the last node
            last = self.head
            while (last.next):
                last = last.next
 
        # 6. Change the next of last node
            last.next =  new_node
    def enter_beg(self, new_data):
 
        # 1 & 2: Allocate the Node &
        # Put in the data
        new_node = Node(new_data)
 
        # 3. Make next of new Node as head
        new_node.next = self.head
 
        # 4. Move the head to point to new Node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
 
        # 1. check if the given prev_node exists
        if prev_node is None:
            print "The given previous node must inLinkedList."
            return
 
        #  2. create new node &
        #      Put in the data
        new_node = Node(new_data)
 
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
 
        # 5. make next of prev_node as new_node
        prev_node.next = new_node
    
    def deleteNode(self, key):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            print'The list is empty'
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None

# This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head # Initialise temp
        count = 0 # Initialise count
 
        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count
     
    # Given a reference to the head of a list 
    # and a position, delete the node at a given position
    def delete_Node_pos(self, position):
 
        # If linked list is empty
        if self.head == None:
            return
 
        # Store head node
        temp = self.head
 
        # If head needs to be removed
        if position == 0:
            self.head = temp.next
            temp = None
            return
 
        # Find previous node of the node to be deleted
        for i in range(position -1 ):
            temp = temp.next
            if temp is None:
                break
 
        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return
 
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
 
        # Unlink the node from linked list
        temp.next = None
 
        temp.next = next    
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        if(found==True):
            print'Yes ! the element searched is available in the linked list\n'
        else:
            print'Sorry the element searched is not available in the linked list\n'
        #return found   



def main():
    llist = LinkedList()# Start with the empty list
    print'1.Enter at Beg \n2.Enter after certain element \n3.Enter at the end \n4.Print the list of elements\n5.Delete an element in the list\n6.Delete_node_at_given_pos\n7.Countof the list\n8.Search  '  
    
    choice= int(input("Enter menu choice:\t"))
    
 
    while choice != 9:
        #get file choice from user
        if choice == 1:
            new_data=int(raw_input('Enter the value to be entered at the begining:\n'))
            llist.enter_beg(new_data)
            print'The list is\n'
            llist.printList()
            
        elif choice == 2:
            new_data=int(raw_input('Enter the value to be entered after certain element:\n'))
            llist.insertAfter(llist.head.next ,new_data)
            print'The list is\n'
            llist.printList()
        
        elif choice == 3:
            new_data=int(raw_input('Enter the value to be entered at the end:\n'))
            llist.enter_last(new_data)
            print'The list is\n'
            llist.printList()
        
        elif choice == 4:
            print 'Created linked list is:\n',
            llist.printList()
        
        elif choice == 5:
            new_data=int(raw_input('Enter the value to be deleted:\n'))
            llist.deleteNode(new_data)
            llist.printList()
        
        elif choice ==6:
            posi=int(raw_input('Enter the position you want to delete an element:\n'))
            llist.delete_Node_pos(posi)
            llist.printList()
        
        elif choice ==7:
            count=llist.getCount()
            print'The no of the nodes in the list is :\n',count
        
        elif choice == 8:
            new_data=int(raw_input('Enter the value to search whether it is present in the list or not:\n'))
            llist.search(new_data)        
        
        elif choice > 8:
            
            print'The entered choice is not valid\n'
       
        choice = int(input("Enter menu choice:\t"))

    print("\nApplication Complete")
    
'''To operate the whole program we need to first call the main function '''
main()
    
    

