#!/usr/bin/env python2
# sam1.py
# Perrine Letellier
#

import numpy as np
from scipy import ndimage
import networkx as nx


graph = 
source =


length = []
l_path = []
for vertice in graph.vertices :
	a,b = bidirectional_dijkstra(graph, source, vertice, weight='weight')
	length.append(a)
	l_path.append(b)
