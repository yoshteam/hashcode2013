import numpy as np
from copy import deepcopy

A=np.loadtxt("doodle.txt",dtype=int)
n,m=A.shape
print sum(sum(A))
print sum(sum(A-1))
f=open("sol","w")


input = deepcopy(A)

for s in range(25,-1,-1): 
  print (s)
  for x in range(s,n-s):
    for y in range(s,m-s):
      if (np.all(input[(x-s):(x+s+1),(y-s):(y+s+1)] == 1)):
#        print (x-s),(x+s),(y-s),(y+s)
        print >>f, "PAINTSQ", x, y, s
        print "PAINTSQ", x, y, s
        input[(x-s):(x+s),(y-s):(y+s)] = 0

f.close()
