'''Permute by sorting : The python program for hiring assistant problem using a priority list '''
import random
def hire_assistant(newList,cost_int, cost_hir):
	best=0
	n= len(newList)
	count = 0
	for i in range (0,n):
		if newList[i] > best:
			best=newList[i]
			print'Candidate',i,'person is hired'
			count=count + 1
	cost_hir = cost_hir * count
	cost_int=  cost_int * n
	print'The interview_cost and hiring_cost are',cost_int,cost_hir

print'Please enter the Candidates value'
A=[ int(x) for x in raw_input().split() ] 
m=len(A)
p=[]
for i in range(0,m):
	p.append(random.randint(0,m*m*m))
print'The priority list is',p	
length_p=len(p)
sum=0
maxx= max(p)
newList= []
for i in range(0,length_p):
	index= p.index(min(p))
	newList.append(A[index])
	p[index] += maxx
print'The new list according to the priority is',newList
cost_interview=int(raw_input("Enter the interview cost of a person:"))
cost_hiring=int(raw_input("Enter the hiring cost of a new person:"))
hire_assistant(newList,cost_interview,cost_hiring) 
		 
