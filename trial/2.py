import numpy as np

A=np.loadtxt("doodle.txt",dtype=int)
n,m=A.shape
print sum(sum(A))
print sum(sum(A-1))
f=open("sol","w")
for i in range(n):
	for j in range(m):
		if A[i,j]==1:
			for k in range(1,1000):
				if i+k>=716 or j+k>=1522:
					break
				cpt=False
				for l in range(k+1):
					if A[i+k,j+l]==0:
						cpt=True
						break
				for l in range(k+1):
					if A[i+k,j+l]==0:
						cpt=True
						break
				if cpt:
					break
			k-=1
			if k/2!=k/2.:
				k-=1
			print k,i+k,j+k
			for l1 in range(k):
				for l2 in range(k):
					A[i+l1,j+l2]=0
			print>>f,"PAINTSQ",str(i+k/2),str(j+k/2),str(k/2)
f.close()
