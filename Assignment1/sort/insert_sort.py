"""
The python program illustrates the implementation of insertion Sort
"""

# definition 
# i is defined as the no. of element sorted till now
# loop invariant
# The  array A[0:i-1] is sorted
print'Enter the elements of the given array'
inputList=[int(x) for x in raw_input().split()]
print " list before sorting is : ",inputList

i = 1
n = len(inputList)

while( i != n ) :
	temp = inputList[i]
	j = i-1
	
	while( j >= 0 and inputList[j] > temp ):
		inputList[j+1] = inputList[j]
		j = j -1
		
	inputList[j+1] = temp
	i = i+1


print " list after sorting is :", inputList
