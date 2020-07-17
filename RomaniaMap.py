from collections import deque


# Class to represent a graph object
class Graph:

	# Constructor
	def __init__(self, edges, x, N):

		self.adjList = [[] for _ in range(3 * N)]

		# add edges to the undirected graph
		for (v, u, weight) in edges:

			# create two vertices v+N and v+2*N if the weight
			# of edge is 3x. Also, split the edge (v, u) into (v, v+N),
			# (v+N, v+2N) and (v+2N, u) each having weight x
			if weight == 3 * x:
				self.adjList[v].append(v + N)
				self.adjList[v + N].append(v + 2 * N)
				self.adjList[v + 2 * N].append(u)

			# create one vertex v+N if the weight of the edge
			# is 2x. Also split the edge (v, u) into (v, v+N),
			# (v+N, u) each having weight x
			elif weight == 2 * x:
				self.adjList[v].append(v + N)
				self.adjList[v + N].append(u)

			# no splitting is needed if edge weight is 1x
			else:
				self.adjList[v].append(u)


# Recursive function to print path of given vertex v from the source vertex
def printPath(predecessor, v, cost, N):

	if v >= 0:
		cost = printPath(predecessor, predecessor[v], cost, N)
		cost = cost + 1

		# consider only original nodes present in the graph
		if v < N:
			print(v, end=' ')

	return cost


# Perform BFS on graph starting from vertex source
def BFS(graph, source, dest, N):

	# stores vertex is discovered in BFS traversal or not
	discovered = [False] * 3 * N

	# mark source vertex as discovered
	discovered[source] = True

	# predecessor stores predecessor information. It is used
	# to trace least cost path from destination back to source.
	predecessor = [-1] * 3 * N

	# create a queue used to do BFS and push source vertex
	# into the queue
	q = deque()
	q.append(source)

	# run till queue is not empty
	while q:

		# pop front node from queue and print it
		curr = q.popleft()

		# if destination vertex is reached
		if curr == dest:
			print("Least cost path between", source, "and", dest, "is ", end='')
			print("having cost", printPath(predecessor, dest, -1, N))

		# do for every adjacent edge of current vertex
		for v in graph.adjList[curr]:
			if not discovered[v]:
				# mark it discovered and push it into queue
				discovered[v] = True
				q.append(v)

				# set curr as predecessor of vertex v
				predecessor[v] = curr


# Least cost path in weighted digraph using BFS
if __name__ == '__main__':

    x = 1

	# List of graph edges as per above diagram
	
    with open('input.txt') as f:
        mylist = list(f)
    #line = file.readLines()
    nodes=[]
    #generate edges in nodes list
    for i in range(len(mylist)):
        node1, node2, distance = mylist[i].split("x")
        dist=distance.rstrip()
        nodes.append((node1,node2,int(dist)* x))
    #print(nodes)   
    edges =nodes
	# Set number of vertices in the graph
	

	# create a graph from edges
	graph = Graph(edges, x, 20)

	# given source and destination vertex
	source = "Arad"
	dest = "Bucharest"

	# Do BFS traversal from given source
	BFS(graph, source, dest, 20)
