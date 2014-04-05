import numpy as np
import random
N=11348 #nombre d'intersections
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
for i in range(N):
	VOIS[int(L[i,0])].append(int(L[i,1]))
	TPS[int(L[i,0])].append(int(L[i,3]))
	DIST[int(L[i,0])].append(int(L[i,4]))
	if L[i,2]==2:
		VOIS[int(L[i,1])].append(int(L[i,0]))
		TPS[int(L[i,1])].append(int(L[i,3]))
		DIST[int(L[i,1])].append(int(L[i,4]))


print VOIS

t=0
p=S
P=[S]
while t<T:
	i=random.randint(0,len(VOIS[p])-1)
	while len(VOIS(VOIS[p][i]))<0:
		i=random.randint(0,len(VOIS[p])-1)
	print i
	t+=TPS[p][i]
	p=VOIS[p][i]
	P.append(p)

n=len(P)-1

f=open("sor","w")
print>>f,8
for i in range(7):
	print>>f,1
	print>>f,S
print>>f,n
for i in range(n):
	print>>f,P[i]
f.close()




