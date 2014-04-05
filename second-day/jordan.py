#!/usr/bin/env python2
# sam1.py
# Jordan Viard
#

import networkx as nx
from readfile import *
import pdb


def get_score(graph, start_node, depth):
	to_visit = graph.neighbors(start_node)
	best_score = 0 
	curr_depth = 0
	best_path = []
	best_node = start_node
	curr_length = 0

	while len(to_visit) is not 0 and curr_depth <= depth:
		for node in to_visit:
					
			to_visit.remove(node)
			
			if curr_length + graph[best_node][node]['length'] > best_score:
				best_score = curr_length + graph[best_node][node]['length']
				best_node = node
		curr_depth += 1

		#for neigh in graph.neighbors(node):
		#	to_visit.append(neigh)
		#	print neigh

	return best_path

graph = read_file("links.txt")
source = 4516

length = []
l_path = []

print get_score(graph, 4516, 1)

#for vertice in graph.nodes() :
	#change all length so that it becomes a minimisation problem : length = 1/length
#	a,b = bidirectional_dijkstra(graph, source, vertice, weight='length')
#	c,d = bidirectional_dijkstra(graph, source, vertice, weight='time')
#	length.append(a)
#	l_path.append(b)

