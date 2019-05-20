"""
The quicksort algorithm which uses divide and conquer strategy
@ Saurav Rai
Rged no:17558
"""

def partition(A,l,u):
    i = l
    j = u
    
    while i<=j:
        if A[i] <= A[l]:
            i = i + 1
        
        elif A[j] > A[l]:
                j = j - 1
            
        else:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i = i + 1
            j = j - 1
    
    temp = A[l]
    A[l] = A[j]
    A[j] = temp
    
    return j

def quicksort(A,l,u):
    if l<u:
        p = partition(A,l,u)
        quicksort(A,l,p-1)
        quicksort(A,p+1,u)

print "Enter an array of numbers to be sorted by quicksort algorithm"
array = [int(x) for x in raw_input().split()]
n=len(array)	
quicksort(array,0,n-1)
print "The sorted array is ",array
