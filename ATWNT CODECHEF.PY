#THIS  CODE IS PARTIAL CORRECT
import sys 

  
# the setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 

  

sys.setrecursionlimit(10**8) 
    
    
def count(graph,v,w):
    
    if len(graph[v]) == 0 :
    	#print("v" , str(v))
    	return 0
    else :
    #	print(str(v),str(w),str(len(graph[v])))
    	if w%len(graph[v]) != 0:
    	#	print("not",str(v))
    		return w
    	
    	else :
        	w=w//len(graph[v])
        	cnt=0
        	
        	for i in graph[v] :
        	#	print("i",str(i))
        		cnt+= count(graph,i,w)
        	#	print(cnt)
        	return cnt		
    
n=int(input())
ar=list(map(int,input().split()))
dic={}
for i in range(1,n+1):
	dic[i]=[]
for i in range(n-1):
	dic[ar[i]].append(i+2)
#print(dic)	
for _ in range(int(input())):
		v,w=map(int,input().split())
		visi=[]
		cnt=0
		c=0
	#	dfs(dic,v,visi,w)
	#	print(cnt)
		print(count(dic,v,w))
		
