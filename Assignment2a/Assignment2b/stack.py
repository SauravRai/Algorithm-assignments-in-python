'''
Created on 09-Aug-2017

@author: sauravrai
Implementation of stack in Python(FILO)(lifo)
Linked List implementation
'''
# Class to represent a node
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
        print data
     
    def pop(self):
        if (self.isEmpty()):
            print'Stack is empty'
            return float("-inf")
        temp = self.root 
        self.root = self.root.next
        popped = temp.data
        return popped
     
    def top(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data
    

def main():
    stack = Stack()# Start with the empty list
    print'1.Push to Stack \n2.Pop from Stack \n3.Top element of Stack \n4.Check Empty or not\n5.Display '  
    
    choice= int(input("Enter menu choice:\t"))
    while choice != 6:
        #get file choice from user
        if choice == 1:
            new_data=raw_input('Enter the value you want to enter to the stack:\n')
            stack.push(new_data)
            print'The Stack is\n'
            stack.display()
       
        elif choice == 2:
            poped=stack.pop()
            print'The element popped is:\n',poped
            print'The Stack is\n'
            stack.display()    
        
        elif choice == 3:
            topp = stack.top()
            print'The top element of the stack is\n',topp
        
        elif choice == 4:
            stack.isEmpty()
        
        elif choice == 5:
            stack.display()
        
        elif choice > 6:
            print'You have entered an invalid key'
     
        choice = int(input("Enter menu choice:\t"))

    print("\nApplication Complete")

'''To use the Stack program we have first the main function'''           
main() 