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
	if GRAPH[i,2] == 2:
		VOIS[GRAPH[i,1]].append(GRAPH[i,0])
		TPS[GRAPH[i,1]].append(GRAPH[i,3])
		DIST[GRAPH[i,1]].append(GRAPH[i,4])

# VOIS[2803] = [1231, 123,123]
# TPS[2803]  = [10s, 20s, 30s]
# DIST[2803] = [10m, 200m, 300m]

# the main code

def best_neighbour(current_node, current_cost):
    # fix     
    neighbours = VOIS[current_node]
    # filter very costly
    good_neighbours_indexes = []
    for n in range(len(neighbours)):
        if current_cost + TPS[current_node][n] <= TIME:
                good_neighbours_indexes.append(n)


    if len(good_neighbours_indexes) > 0:
        awards = [DIST[current_node][ind] 
                 for ind in good_neighbours_indexes]
        maward = max(awards)
        indexes = [ind for ind in good_neighbours_indexes
                   if DIST[current_node][ind] == maward]

        costs = [TPS[current_node][ind] 
                 for ind in good_neighbours_indexes]
        mincost = min(costs)
        
        indexes2 = [ind for ind in good_neighbours_indexes
                    if TPS[current_node][ind] == mincost]
        
        best_neighbour_index = random.choice(indexes)
        cost = TPS[current_node][best_neighbour_index]
        best_neighbour = neighbours[best_neighbour_index]
    else:
        # error
        cost = -100
        best_neighbour = -100
    return (best_neighbour, cost)

def remove_award(current_node, next_node):
    next_node_index = VOIS[current_node].index(next_node)
    # the distance will be zero 
    DIST[current_node][next_node_index] = 0
    if current_node in VOIS[next_node]:
        current_node_index = VOIS[next_node].index(current_node)
        DIST[next_node][current_node_index] = 0

print CARS
# CAR par CAR
for CAR in range(CARS):
    visited_nodes = []    
    current_node = STARTPOINT
    current_time = 0
    visited_nodes.append(current_node)
    while current_time < TIME:
        # choose a neighbour
        next_node, time = best_neighbour(current_node, current_time)
        if next_node == -100:
            break
        else:
            # we was here, so we remove award
            remove_award(current_node, next_node)
            visited_nodes.append(next_node)
            current_node = next_node
            current_time = current_time + time
    # output for that CAR
    # print len(visited_nodes)
    print len(visited_nodes)
    for n in visited_nodes:
        print n
