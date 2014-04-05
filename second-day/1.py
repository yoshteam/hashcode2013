import numpy as np
import random
N=11348 #nombre d'intersections
R=17958 #number of streets
C=8 #nombre de voitures
T=54000 #tps virtuel
S=4516 #indice de depart

VOIS=[]
TPS=[]
DIST=[]
for i in range(N):
	VOIS.append([])
	TPS.append([])
	DIST.append([])

L=np.loadtxt("links.txt")
for i in range(R):
	VOIS[int(L[i,0])].append(int(L[i,1]))
	TPS[int(L[i,0])].append(int(L[i,3]))
	DIST[int(L[i,0])].append(int(L[i,4]))
	if L[i,2]==2:
		VOIS[int(L[i,1])].append(int(L[i,0]))
		TPS[int(L[i,1])].append(int(L[i,3]))
		DIST[int(L[i,1])].append(int(L[i,4]))

VIS=np.zeros(N,dtype=bool)
VIS[S]=True

t=0
length=0
p=S
P=[S]
while t<T:
	i=-1
	for j in range(len(VOIS[p])):
		if len(VOIS[VOIS[p][j]])!=0 and not(VIS[VOIS[p][j]]):
			i=j
			length+=DIST[p][i]
			break
	if i==-1:
		i=random.randint(0,len(VOIS[p])-1)
		while len(VOIS[VOIS[p][i]])==0:
			i=random.randint(0,len(VOIS[p])-1)
	print i
	t+=TPS[p][i]
	p=VOIS[p][i]
	VIS[p]=True
	P.append(p)

print P
print length
print t
n=len(P)-1

f=open("sol","w")
print>>f,8
for i in range(7):
	print>>f,1
	print>>f,S
print>>f,n
for i in range(n):
	print>>f,P[i]
f.close()

