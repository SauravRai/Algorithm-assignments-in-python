'''
Created on 12-Sep-2017

@author: sauravrai

The delete and insert operation operation in Dynamic Table 
using Fibonacci sequence 

'''

from copy import deepcopy
import math

 
    
class table1:
    def __init__(self,size,count):
        self.table = []
        self.size = size
        self.count = count
    # A utility function that returns true if x is perfect square
    def isPerfectSquare(self,x):
        s = int(math.sqrt(x))
        return s*s == x
    # Returns true if n is a fiboNumber, else false
    def isFibonacci(self,n):
 
    # n is fiboNumber if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
        return self.isPerfectSquare(5*n*n + 4) or self.isPerfectSquare(5*n*n - 4)
    
   
    def table_insert(self,x):
        if self.size == 0:
            self.table=[None]
            self.size+= 1
        elif  self.size == self.count:
            Newtable = [None] * 2 *self.size
            '''self.table1[0:self.count]= self.table[0:self.count] '''  
            Newtable[0:self.count]= deepcopy(self.table[0:self.count])
            self.table = Newtable
            self.size=2*self.size
        self.table[self.count]=x
        self.count=self.count + 1
    
    def table_delete(self,x):
        if self.size ==0:
            print 'There is no element to be deleted in the list'
            # first we need to pop an element an element 
        elif self.size > 0 :
            print'self.count',self.count
            print'self.size',self.size
            value=self.isFibonacci(self.size)
            print value
            if value:
                for i in range(0,self.size-1):
                    if(self.table[i]==x):
                        Newtable = [None] *self.size
                        del self.table[i]
                        self.count=self.count-1
                        Newtable[0:self.count]= deepcopy(self.table[0:self.count])
                        self.table = Newtable
                        print'self.count in fib',self.count
                        print'self.size in fib',self.size
                        
            elif value ==False:
                print 'sairam'
                for i in range(0,self.size-1):
                    if(self.table[i]==x):
                        del self.table[i]
                        self.count=self.count-1
                        self.size=self.size-1
                        print'self.count',self.count
                        print'self.size',self.size
                        print 'ram'
            
                
# The initialization of the table
t =table1(0,0)

t.table_insert(4)
t.table_insert(5)
t.table_insert(6)
t.table_insert(7)
t.table_insert(8)
print 'before delete'

for i in range (0, t.count):
    print t.table[i]

print t.table

print 'after delete'

t.table_delete(6)
'''for i in range (1, t.count):
    print t.table[i]
'''
print t.table
'''
Created on 22-Sep-2017

@author: sauravrai
'''
