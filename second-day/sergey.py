# hi :)
import numpy as np
from copy import deepcopy

header = np.loadtxt("header.txt", dtype=int)
TIME   = header[2]
CARS   = header[3]
STARTPOINT  = header[4]

GRAPH = np.loadtxt("links.txt",dtype=int)
number_of_links = L.shape[0]


