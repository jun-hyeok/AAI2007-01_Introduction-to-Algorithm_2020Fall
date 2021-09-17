def choose_min_vertex(dist, found):	
    min = INF
    minpos = -1
    for i in range(len(dist)) :				
        if dist[i] < min and found[i] == False:	
            min = dist[i]
            minpos = i
    return minpos;							

def dijkstra(vtx, adj, start):						
    vsize = len(vtx)
    dist = list(adj[start])					
    path = [start] * vsize					
    found= [False] * vsize					
    found[start] = True						
    dist[start] = 0							
    for i in range(vsize):
        u = choose_min_vertex(dist, found)		
        found[u] = True						
        for w in range(vsize):				
            if not found[w]:				
                if  dist[u] + adj[u][w] < dist[w]:	
                    dist[w] = dist[u] + adj[u][w]	
                    path[w] = u						
    return path							            

INF = float('inf')
vertex =   ['A', 'B', 'C', 'D', 'E', 'F', 'G']
adj_matrix = [ [0, 3, 7, 5, INF, INF, INF],
               [3, 0, 2, INF, 9, INF, INF],
               [7, 2, 0, 1, 6, 12, 25],
               [5, INF, 1, 0, INF, INF, 20],
               [INF, 9, 6, INF, 0, 4, INF],
               [INF, INF, 12, INF, 4, 0, 8],
               [INF, INF, 25, 20, INF, 8, 0]] 

print("Shortest Path by Dijkstra's Algorithm")
start = 0		
path = dijkstra(vertex, adj_matrix, start)

for end in range(len(vertex)):
    if end != start:
        print("[Shortest Path: %s->%s] %s" %
				(vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start):
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])



        



        