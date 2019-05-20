'''The python program for randomly hiring assistant problem'''
import random
def hire_assistant(A,cost_int, cost_hir):
	best=0
	n= len(A)
	count = 0
	for i in range (0,n):
		if A[i] > best:
			best=A[i]
			count=count + 1
	print "count",count,"\n"
	cost_hir = cost_hir * count
	cost_int=  cost_int * n
	print'The interview_cost and hiring_cost are',cost_int,cost_hir

print'Please enter the Candidates value'
A=[ int(x) for x in raw_input().split() ] 
random.shuffle(A)
print'The values of the array A after shuffling are:',A
cost_interview=int(raw_input("Enter the interview cost of a person:"))
cost_hiring=int(raw_input("Enter the hiring cost of a new person:"))
hire_assistant(A,cost_interview,cost_hiring) 
		 
