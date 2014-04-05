# hi :)
import numpy as np
import random
from pprint import pprint
from copy import deepcopy
import sys


sys.setrecursionlimit(50000) #lol

# initialization....
# see also prepare.sh


header = np.loadtxt("header.txt", dtype=int)
GRAPH = np.loadtxt("links.txt",dtype=int)
#header = np.loadtxt("header-small.txt", dtype=int)
#GRAPH = np.loadtxt("links-small.txt",dtype=int)
TIME   = header[2]
CARS   = header[3]
STARTPOINT  = header[4]


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

# paths ---look_forward---> paths
# path = (nodes, award, cost)
def look_forward(paths, recursion=3):

    if recursion == 0:
        return paths
    out = []
    for p in paths:
        path = deepcopy(p)
        nodes = path[0]
        current_award = path[1]
        current_cost  = path[2]
        current_node = nodes[-1]
        neighbours = VOIS[current_node]
        # filter very costly
        for n in range(len(neighbours)):
            if current_cost + TPS[current_node][n] <= TIME:
                new_nodes = deepcopy(nodes)
                new_nodes.append(VOIS[current_node][n])
                cost = current_cost + TPS[current_node][n]
                award = current_award + DIST[current_node][n]
                newpath = (new_nodes, award, cost)
                out.append(newpath)
    return (look_forward(out,recursion-1))


def best_neighbour(current_node, current_cost):
    paths = [
        ([current_node], 0, current_cost)
        ]
    res = look_forward(paths, recursion=4)
    awards = [r[1] for r in res]
    if len(awards) == 0:
        return (-100,-100)
    maward = max(awards)
    neighbours = [r[0][1] for r in res 
                  if r[1] == maward]

    neigh = random.choice(neighbours)
    time = TPS[current_node] [VOIS[current_node].index(neigh)]
    return (neigh, time)

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
