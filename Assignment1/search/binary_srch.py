'''This is a binary search program 
   for finding the leftmost ocurring of an element
  @ SAURAV RAI '''
print"Enter an array of integers"
A=[int(y) for y in raw_input().split()]
print"Enter search element"
x=int(raw_input())
n=len(A)
l=0
u=n-1
while l<u: 
	m=(l+u)/2 #flooring
	if A[m]>= x:# progress part
		u=m
	else:
		l=m+1
if x==A[l]:
	print"The leftmost ocurrening element is at ",(l+1)
else:
	print"Not present"
