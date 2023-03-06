
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

class priority_queue(object): 
    def __init__(self):
        self.pq = []
        self.len = len(self.pq)

    def add(self, vertex, weight):
        if(len(self.pq)==0):
           self.pq.append((vertex, weight))
        elif(self.pq[0][1] > weight): 
            self.pq.insert(0, (vertex, weight))
        else: 
            self.pq.append((vertex, weight))

        self.len+=1

    def remove(self, vertex): 
        for v in self.pq: 
            if v[0] == vertex: 
                self.pq.remove(v)
                self.len -= 1

    def getMin(self):
        return self.pq[0]

    def printQueue(self):
        print(self.pq)

def DijkstraAlgo_A(graph, source):
    d = []
    pi = []
    S = []
    pq = priority_queue()

    for v in range(graph.getSize()):
        d.append(float('inf'))
        pi.append(0)
        S.append(None)

    d[source-1] = 0

    # Push every vertex into priority queue using array based on d[]
    for vertex in range(len(d)):
        pq.add(vertex, d[vertex])

    while pq.len:
        
        # Get minimum weight    
        u = pq.getMin()[0] 
        S[u] = 1
        pq.remove(u)

        # For every adjacent node
        for v in range(graph.getSize()):
            if ((graph.adjMatrix[u][v] != 0) and (graph.adjMatrix[u][v] != float('inf'))
            and (d[v] > d[u] + graph.adjMatrix[u][v])):
                pq.remove(v)
                d[v] = d[u] + graph.adjMatrix[u][v]
                pi[v] = u+1
                pq.add(v, d[v])

    return S, d, pi
            

def DijkstraAlgo_B(graph, source):
    d = []
    pi = []
    S = []
    pq = priority_queue()

    for v in range(graph.getSize()):
        d.append(float('inf'))
        pi.append(0)
        S.append(None)

    d[source-1] = 0

    # Push every vertex into priority queue using array based on d[]
    for vertex in range(len(d)):
        pq.add(vertex, d[vertex])

    while pq.len:
        
        # Get minimum weight    
        u = pq.getMin()[0] 
        S[u] = 1
        pq.remove(u)

        # For every adjacent node
        # Node Structure: Header Node -> [(Node, Edge Weight)]
        for nodes in graph.adjList: 
            for node in graph.adjList[nodes]:
                v = node[0] - 1 
                if d[v] > d[u] + node[1]:
                    pq.remove(v)
                    d[v] = d[u] + node[1]
                    pi[v] = u+1
                    pq.add(v, d[v])

    return S, d, pi


def main():
    import time, random

    s = 5
    g = Graph(s)
    
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 6)
    g.add_edge(1, 5, 8)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 5, 3) 
    g.add_edge(3, 4, 1)
    g.add_edge(4, 2, 1)
    g.add_edge(4, 5, 3)

    # Adjacency Matrix
    g.print_matrix()

    start_time = time.time()
    S, d, pi = DijkstraAlgo_A(g, 1)
    elapsed_time = time.time() - start_time 
    
    print("Elapsed Time: {:2}s".format(elapsed_time))
 
    # Adjacency Lists
    g.print_list()

    start_time = time.time()
    S, d, pi = DijkstraAlgo_B(g, 1)
    elapsed_time = time.time() - start_time 

    print("Elapsed Time: {:2}s".format(elapsed_time))

if __name__ == '__main__':
    main()
