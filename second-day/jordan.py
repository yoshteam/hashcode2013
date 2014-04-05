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
for vertice in graph.nodes() :
	#change all length so that it becomes a minimisation problem : length = 1/length
	a,b = bidirectional_dijkstra(graph, source, vertice, weight='length')
	c,d = bidirectional_dijkstra(graph, source, vertice, weight='time')
	length.append(a)
	l_path.append(b)

