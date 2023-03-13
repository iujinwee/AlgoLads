import heapq
import numpy as np
# Adjacency Matrix representation in Python

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        self.adjList = {}
        self.size = size

        # Adjacency Matrix
        for i in range(size):
            self.adjMatrix.append([float('inf') if i != j else 0 for j in range(size)])

        # Adjacency List 
        for i in range(size): 
            self.adjList[i] = []
        
    # Add edges
    def add_edge(self, v1, v2, weight):
        if v1 == v2:
            print("Same vertex {} and {}".format(v1, v2))
        elif (v1==0) | (v2==0):
            print("Please enter vertex between 1 - {}".format(self.size))
        
        # Adjacency Matrix
        self.adjMatrix[v1-1][v2-1] = weight
        
        add = 1
        # Adjacency List 
        for item in self.adjList[v1-1]:
            if item[0] == v2: 
                add = 0

        if add: 
            self.adjList[v1-1].append((v2, weight))

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between {} and {}".format(v1, v2))
        elif (v1==0) | (v2==0):
            print("Please enter vertex between 1 - {}".format(self.size))
            return
        
        # Adjacency Matrix
        self.adjMatrix[v1-1][v2-1] = float('inf')

        # Adjacency Matrix 
        self.adjList[v1].remove(v2)

    def getSize(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=" "),
            print("\n")

    def print_list(self): 
        for vertex in self.adjList:
            print("{} -> ".format(vertex+1), end=" ")
            for item in self.adjList[vertex]:
                print("{}".format(item), end=" ")
            print("\n")

    # Check if graph is strongly connected
    def is_strongly_connected(self):
        # Perform DFS from each vertex
        for start in range(self.size):
            visited = [False] * self.size
            self._dfs(start, visited)

            # Check if all vertices were visited
            if not all(visited):
                return False

        return True
    
    # Helper function for DFS
    def _dfs(self, vertex, visited):
        visited[vertex] = True
        for neighbor in self.adjList[vertex]:
            if not visited[neighbor[0] - 1]:
                self._dfs(neighbor[0] - 1, visited)


class priority_queue(object): 
    def __init__(self):
        self.pq = []
        self.len = len(self.pq)

    def add(self, vertex, weight):
        if not self.pq:
            self.pq.append((vertex, weight))
            self.len += 1
            return

        # Binary Search
        low, high = 0, self.len-1

        while low <= high:
            mid = (low + high) // 2
            if self.pq[mid][1] < weight:
                low = mid + 1
            else:
                high = mid - 1

        self.pq.insert(low, (vertex, weight))
        self.len += 1

    def remove(self, vertex): 
        for v in self.pq: 
            if v[0] == vertex: 
                self.pq.remove(v)
                self.len -= 1

    def getMin(self):
        return self.pq[0]

    def printQueue(self):
        print(self.pq)



class priority_queue_heap(object):
    def __init__(self):
        self.pq = []
        self.len = len(self.pq)

    def add(self, vertex, weight):
        heapq.heappush(self.pq, (weight, vertex))
        self.len += 1

    def remove(self, vertex):
        for v in self.pq:
            if v[1] == vertex:
                self.pq.remove(v)
                self.len -= 1

    def getMin(self):
        return self.pq[0]

    def printQueue(self):
        print(self.pq)

# def DijkstraAlgo_A(graph, source):
#     d = []
#     pi = []
#     S = []
#     pq = []
    
#     # Initialization 
#     for v in range(graph.getSize()):
#         d.append(float('inf'))
#         pi.append(0)
#         S.append(None)
#         pq.append((v, d[v])) # Push every vertex into priority queue using array

#     # Set source node 
#     d[source-1] = 0

#     while len(pq):
            
#         pq.sort(key=lambda x: x[1])
#         print(pq)

#         # Get minimum weight
#         u = pq[0][0]

#         if S[u] == 1:
#             for i in range(len(pq)-1): 
#                 if pq[i][0] == u:
#                     pq.remove(pq[i])
#             continue

#         S[u] = 1
#         for v in range(graph.getSize()):
#             # For every adjacent node
#             if ((graph.adjMatrix[u][v] != 0) and 
#                 (graph.adjMatrix[u][v] != float('inf'))
#                 # Not already minimized 
#                 and (S[v] != 1) 
#                 # Can minimize d[v]
#                 and (d[v] > d[u] + graph.adjMatrix[u][v])): 
#                 d[v] = d[u] + graph.adjMatrix[u][v]
#                 pi[v] = u+1
#                 pq.append((v, d[v]))

#     return S, d, pi


def DijkstraAlgo_A(graph, source):
    d = []
    pi = []
    S = []
    pq = []
    counter = 0

    # Initialization 
    for v in range(graph.getSize()):
        d.append(float('inf'))
        pi.append(0)
        S.append(None)
        # Push every vertex into priority queue using array
        pq.append((v, d[v]))

    # Set source node 
    d[source-1] = 0

    while counter != len(pq):
        
        u = 0
        # Get minimum weight (vertex, weight)
        weight = d[0]
        for index in range(1, len(pq)): 
            if(pq[index][1] < weight): 
                u = index
                weight = pq[index][1]

        S[u] = 1

        # Remove u from PQ
        for index in range(len(pq)):
            if pq[index][0] == u:
                pq[index] = (u, d[u])
                counter+=1
                break

        for v in range(graph.getSize()):
            # Adjacent vertex
            w = graph.adjMatrix[u][v]
            
            if ((w !=0) and 
                (w != float('inf'))):

                # If v is visited, ignore
                if(S[v]==1):
                    continue

                temp_weight = d[u] + w

                if temp_weight < d[v]:
                    # Update weight
                    d[v] = temp_weight 
                    pq[v] = (v, temp_weight)

    return S, d, pi
            

def DijkstraAlgo_B(graph, source):
    # use the adjacency list to find the shortest path
    d = []
    pi = []
    S = []
    pq = priority_queue_heap()

    for v in range(graph.getSize()): # Time Complexity = O(V)
        d.append(float('inf'))
        pi.append(0)
        S.append(None)

    d[source-1] = 0

    # Push every vertex into priority queue using array based on d[]
    for vertex in range(len(d)):
        pq.add(vertex, d[vertex])

    while pq.len:
            
            # Get minimum weight    
            u = pq.getMin()[1] # Time Complexity = O(1)
            S[u] = 1
            pq.remove(u) # Time Complexity = O(V)

            # For every adjacent node
            # Use BFS to traverse the graph using the adjacency list
            for v in graph.adjList[u]: # Time Complexity = O(|E| + |V|)
                if ((v[1] != 0) and (v[1] != float('inf'))
                and (d[v[0]-1] > d[u] + v[1]) and (S[v[0]-1] == None)):
                    pq.remove(v[0]-1) # Time Complexity = O(V)
                    d[v[0]-1] = d[u] + v[1] 
                    pi[v[0]-1] = u+1
                    pq.add(v[0]-1, d[v[0]-1]) # Time Complexity = O(log(V))


    return S, d, pi

import random

def generate_graph(size, num_edges, sparse=True):
    graph = Graph(size)
    
    # generate dense graph
    if not sparse:
        edge_count = 0
        for i in range(size):
            for j in range(i+1, size):
                if edge_count < num_edges:
                    weight = random.randint(1, 100)
                    graph.add_edge(i+1, j+1, weight)
                    edge_count += 1
                else:
                    break
        return graph
    
    # generate sparse graph
    # set the number of edges for each vertex
    num_edges_per_vertex = num_edges // size

    for i in range(size):
        edges_added = 0
        while edges_added < num_edges_per_vertex:
            j = random.randint(1, size)
            if i+1 != j and graph.adjMatrix[i][j-1] == float('inf'):
                weight = random.randint(1, 100)
                graph.add_edge(i+1, j, weight)
                edges_added += 1    
                
    return graph


def main():
    # part_a()

    part_c()


def part_a():
    import time, random, matplotlib.pyplot as plt 

    
    # Part A 
    sizes = range(10, 200, 10)
    runtime_dense = []
    runtime_sparse = []
    runs = 100  

    for size in sizes: 
        # g = generate_random_graph(size)

        edges = size * (size-1) / 2
        g = generate_graph(size, edges, sparse=True)
        elapsed_time = 0    
        
        for _ in range(runs): 
            start_time = time.time()
            DijkstraAlgo_A(g, 1)
            # print(S, d, pi)
            elapsed_time += time.time() - start_time 

        print(size)
        # print("Elapsed Time: {:2}s".format(elapsed_time))
        runtime_sparse.append(elapsed_time/runs)

        g = generate_graph(size, edges, sparse=False)
        elapsed_time = 0    
        
        for _ in range(runs): 
            start_time = time.time()
            DijkstraAlgo_A(g, 1)
            # print(S, d, pi)
            elapsed_time += time.time() - start_time 

        print(size)
        # print("Elapsed Time: {:2}s".format(elapsed_time))
        runtime_dense.append(elapsed_time/runs)

    # Plot the runtime against the vertex size
    plt.plot(sizes, runtime_sparse, label="Sparse Graph")
    plt.plot(sizes, runtime_dense, label="Dense Graph")
    plt.xlabel('|V|')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime vs |V| for Sparse vs Dense Graphs')
    plt.legend()
    plt.show()

def part_c(): 
    import time, matplotlib.pyplot as plt
    v = 100
    x = [i for i in range(v-1, v(v-1)/2, 5)]

    for e in x:
        g = generate_connected_graph(v, e)
        runs = 100

        runtime_a = []
        runtime_b = []
        elapsed_time = 0    
            
        for _ in range(runs): 
            start_time = time.time()
            DijkstraAlgo_A(g, 1)
            # print(S, d, pi)
            elapsed_time += time.time() - start_time 

    runtime_a.append(elapsed_time/runs)
    runtime_b.append(elapsed_time/runs)

    # Plot the runtime against the vertex size
    plt.plot(x, runtime_a, label="")
    plt.plot(x, runtime_b, label="Dense Graph")
    plt.xlabel('|V|')
    plt.ylabel('Runtime (seconds)')
    plt.title('Runtime vs |V| for Sparse vs Dense Graphs')
    plt.legend()
    plt.show()

def generate_connected_graph(num_vertices, num_edges):
    import networkx as nx

    # Create an empty graph with n nodes
    G = nx.Graph()
    G.add_nodes_from(range(num_vertices))

    edges = 0

    # Add random edges until the graph becomes strongly connected
    while not nx.is_strongly_connected(G) and edges <= num_edges:
        # Choose two random nodes
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)

        # Add an edge between them
        G.add_edge(u, v)
        edges+=1

    return G

if __name__ == '__main__':
    main()
