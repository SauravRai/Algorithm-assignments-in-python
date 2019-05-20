'''The merge sort program
   @ Saurav rai '''
def merge_sort_routine(A,l,u):
	if l>=u:
		return A;
	#print A[l:u+1]
	m=(l+u)/2 #flooring
	merge_sort_routine(A,l,m) #sorting A[l:m+1]
	merge_sort_routine(A,m+1,u) #sorting A[m+1,u+1]
   
    #merge the sorted arrays
	L=A[l:m+1]
	"""for x in A[l,m+1]:
		L.append(x)"""
	U=A[m+1:u+1]
	"""for x in A[m+1:u+1]:
		U.append(x)"""
	n1=len(L)
	n2=len(U)
#loop invariant :
#A[0:i+j] is a sorted array comprising elements from L[0:i] and U[0:j]
#where i is from [0:n1] and j is form [0:n2]
# i(j) is the number of elemnts copied from L(U)
 
	i=0
	j=0
	k= l
	while i<n1 and j<n2:
		if L[i]<=U[j]:
			A[k]=L[i]
			i = i+1
			k = k+1
		else:
			A[k]=U[j]
			j = j+1
			k = k+1
 	
 	if i==n1:
		while j<n2:
				A[k]=U[j]
				j = j+1
				k = k+1
	elif j==n2:
		while i<n1:
				A[k]=L[i]
				i = i+1
				k = k+1
	return A
 


def mergesort(A):
	'''if not is type(A,list): '''
	N=len(A)
	A=merge_sort_routine(A,0,N-1)
	return A
			
print"Enter an array of integers"
A=[int(x) for x in raw_input().split()]
A=mergesort(A)
print"The Array is ",A
