import networkx as nx
import sys
import pdb

def read_file(path):
	""" Parse link file into graph """
	G = nx.Graph()

	with open(path, 'r') as in_file:
		for line in in_file:
			contents = line.split(" ")
			u = int(contents[0])
			v = int(contents[1])
			street_type = int(contents[2])
			time = int(contents[3])
			length = int(contents[4])
			cost = 1/float(length)
			
			G.add_node(u)
			G.add_node(v)
			G.add_edge(u, v, street_type=street_type, time=time, length=length, cost=cost)

			sys.stdout.write(line)
	return G

# Graph edges can be accessed with G.edges(), and attributes of edge (x,y) with G[x][y]['attribute']
# Attributes are : street_type, time, length
# Graph nodes can be accessed with G.nodes()

# ingraph = read_file(sys.argv[1])
