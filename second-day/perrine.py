#!/usr/bin/env python2
# sam1.py
# Perrine Letellier
#

import numpy as np
from scipy import ndimage
import networkx as nx
import readfile
import operator

time = 54000
nb_car = 8
source = 4516
graph = readfile.read_file("links.txt")


f=open("sol","w")
print>>f, nb_car


for car in range(nb_car) :
	costs_dict = dict()
	paths_dict = dict()
	time_dict = dict()
	for vertice in graph.nodes() :
		a,b = nx.shortest_path(graph, source, vertice, weight='cost')
		costs_dict[str(vertice)] = a
		paths_dict[str(vertice)] = b
		#compute the time needed for each path
		total = 0
		for i in range(len(b)-1):
			total = total + graph[b[i]][b[i+1]]['time']

		time_dict[str(vertice)] = total


	#filter those with a cost less than total time
	filter_costs = dict()
	for k in costs_dict:
	    if time_dict[k] <= time:
	        filter_costs[str(k)] = costs_dict[k]

	sorted_costs = sorted(filter_costs.iteritems(), key=operator.itemgetter(1))
	# these are sorted in the reverse order because real length = 1/cost
	best_node = sorted_costs[1][1]


	#TODO : remettre le score à 0 pour les chemins deja parcourus

	#TODO si le temps n'est pas épuisé continue en prenant un chemin inférieur au temps restant

	print>>f,len(paths_dict[best_node])
	for node in paths_dict[best_node]:
		print>>f,node



f.close()	