#!/usr/bin/env python2
#
# Perrine Letellier
#

import numpy as np
from scipy import ndimage


input = np.loadtxt("doodle.txt",delimiter=" ",dtype=int)
L,H = input.shape
#T = min(L,H)
T=150
f=open("sol","w")


if T%2==0:
	T=T-1

for o in range(T,0,-2):
	structure = np.ones(shape=(o,o),dtype=int)
	print "--processing erosion for ", str(o), "cells structure"
	res = ndimage.morphology.binary_erosion(input,structure)
	print "--erosion processed"
	res1=np.ones(shape=res.shape,dtype=int)
	res1[res==True] = 1
	res1[res==False] = 0
	tmp=res1.copy()
	for i in range(L):
		for j in range(H):
			if tmp[i,j] == 1:
				S=(o-1)/2
				a = max(i-2*S,0)
				b = min(i+2*S,H)
				c = max(j-2*S,0)
				d = min(j+2*S,L)
				tmp[a:b,c:d] = 0
				res1[a:b,c:d] = 0
				res1[i-S:i+S+1,j-S:j+S+1]=1
				print res1
				print a, b, c, d
				print>>f,"PAINTSQ",str(i),str(j),o
				print "PAINTSQ",str(i),str(j),o
	diff = input - res1
	input =diff

f.close()	

