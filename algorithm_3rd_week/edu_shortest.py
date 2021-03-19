import heapq

def dijkstra(graph, start, end):
	distances = {vertex: [float('inf'), start] for vertex in graph}

	distances[start] = [0, start]

	# min-heap
	queue = []

	heapq.heappush(queue, [distances[start][0], start])





	return distances


mygraph = {
	'A':{'B':8, 'C':1, 'D':2},
	'B':{},
	'C':{'B':5, 'D':2},
	'D':{'E':3, 'F':5},
	'E':{'F':1},
	'F':{'A':5}
}

print(dijkstra(mygraph, 'A', 'F'))
