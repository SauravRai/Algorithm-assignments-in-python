'''The python program for randomize in place'''
import random

print'Enter the input array'
A=[int(x) for x in raw_input().split()]
print'The initial values of the array',A
n=len(A)
ran=[]
for i in range (0,n):
	index = random.randint(0,n)
	(A[i], A[index])= (A[index], A[i])
print'The new array after swapping with the randomized array values is',A
