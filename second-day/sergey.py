# hi :)
import numpy as np
import random
from copy import deepcopy


# initialization....
# see also prepare.sh

header = np.loadtxt("header.txt", dtype=int)
TIME   = header[2]
CARS   = header[3]
STARTPOINT  = header[4]

GRAPH = np.loadtxt("links.txt",dtype=int)
number_of_links = GRAPH.shape[0]
N = len(GRAPH[:,1])

VOIS=[]
TPS=[]
DIST=[]
AWARD=[]
for i in range(N):
	VOIS.append([])
	TPS.append([])
	DIST.append([])

for i in range(N):
	VOIS[GRAPH[i,0]].append(GRAPH[i,1])
	TPS[GRAPH[i,0]].append(GRAPH[i,3])
	DIST[GRAPH[i,0]].append(GRAPH[i,4])
	if GRAPH[i,2]==2:
		VOIS[GRAPH[i,1]].append(GRAPH[i,0])
		TPS[GRAPH[i,1]].append(GRAPH[i,3])
		DIST[GRAPH[i,1]].append(GRAPH[i,4])


# the main code

def best_neighbour(current_node, current_cost):
    neighbours = VOIS[current_node]
    # filter very costly
    good_neighbours_indexes = []
    for n in range(len(neighbours)):
        if current_cost + TPS[current_node][n] <= TIME:
            good_neighbours_indexes.append(n)
    best_neighbour_index = random.choice(good_neighbours_indexes)
    cost = TPS[current_node][best_neighbour_index]
    best_neighbour = neighbours[best_neighbour_index]
    return (best_neighbour, cost)

def remove_award(current_node, next_node):
    next_node_index = VOIS[current_node].index(next_node)
    """ the distance will be zero """
    DIST[current_node][next_node_index] = 0
    if GRAPH[current_node,2]==2:
        curent_node_index = VOIS[next_node].index(current_node)
        DIST[next_node][current_node_index] = 0

# CAR par CAR
print CARS
for CAR in range(CARS):
#    print (CAR)
    visited_nodes = []    
    current_node = STARTPOINT
    current_cost = 0
    visited_nodes.append(current_node)
    while current_cost < TIME:
        # choose a neighbour
        next_node, cost = best_neighbour(current_node, current_cost)
        current_cost = current_cost + cost
        # we was here, so we remove award
        remove_award(current_node, next_node)
        visited_nodes.append(next_node)
        
    # output for that CAR
    print len(visited_nodes)
    for n in visited_nodes:
        print n
