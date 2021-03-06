# hi :)
import numpy as np
import random
from pprint import pprint
from copy import deepcopy,copy
from sys import stderr
import sys


sys.setrecursionlimit(50000) #lol

# initialization....
# see also prepare.sh


header = np.loadtxt("header.txt", dtype=int)
GRAPH = np.loadtxt("links.txt",dtype=int)
COORDINATES = np.loadtxt("nodes.txt",dtype=float)
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


def remove_award(current_node, next_node, local_DIST):
    next_node_index = VOIS[current_node].index(next_node)
    # the distance will be zero 
    local_DIST[current_node][next_node_index] = 0
    if current_node in VOIS[next_node]:
        current_node_index = VOIS[next_node].index(current_node)
        local_DIST[next_node][current_node_index] = 0


def distance(node1, node2):
    return (
               abs(COORDINATES[node1][0] - COORDINATES[node2][0]) + 
               abs(COORDINATES[node1][1] - COORDINATES[node2][1]))
        
# VOIS[2803] = [1231, 123,123]
# TPS[2803]  = [10s, 20s, 30s]
# DIST[2803] = [10m, 200m, 300m]
# the main code

# paths ---look_forward---> paths
# path = (nodes, award, cost, local_dist)
def look_forward(paths, recursion=2):
    if recursion == 0:
        return paths
    out = []
    for p in paths:
        path = copy(p)
        nodes = path[0]
        current_award = path[1]
        current_cost  = path[2]
        local_dist  = path[3]
        current_node = nodes[-1]
        neighbours = VOIS[current_node]
        # filter very costly
        for n in range(len(neighbours)):
            next_node = VOIS[current_node][n]
            next_cost = TPS[current_node][n]
            next_award = local_dist[current_node][n]
            if current_cost + next_cost <= TIME and \
               (len(nodes) < 2 or not next_node == nodes[-2]):
                new_nodes = deepcopy(nodes)
                new_nodes.append(next_node)
                cost = current_cost + next_cost
                award = current_award + next_award
#                local_dist = deepcopy(local_dist)
#                remove_award(current_node, next_node, local_dist)
                newpath = (new_nodes, award, cost, local_dist)
                out.append(newpath)
    return (look_forward(out,recursion-1))


def best_neighbour(current_node, current_cost):
    paths = [
        ([current_node], 0, current_cost, DIST)
        ]
    res = look_forward(paths, recursion=6)
    # THINK ABOUT LOCAL DEEPCOPY OF DIST!
    awards = [r[1] for r in res]
    if len(awards) == 0:
        return (-100,-100)
    maward = max(awards)
    neighbours = [r[0][1] for r in res 
                  if r[1] == maward]
    neigh = random.choice(neighbours)
    time = TPS[current_node] [VOIS[current_node].index(neigh)]
    return (neigh, time)

print CARS
TOTAL_AWARD = 0
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
            TOTAL_AWARD = TOTAL_AWARD + DIST[current_node][VOIS[current_node].index(next_node)]
            print >>stderr, "TOTAL:AWARD: ", TOTAL_AWARD 
            # we was here, so we remove award
            remove_award(current_node, next_node, DIST)
            visited_nodes.append(next_node)
            current_node = next_node
            current_time = current_time + time
    # output for that CAR
    print len(visited_nodes)
    for n in visited_nodes:
        print n

print >>stderr, "TOTAL:AWARD: ", TOTAL_AWARD 
