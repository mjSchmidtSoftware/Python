#Jordan Jones jbjones
#Michael Schmidt mjschmid
import os
import queue
class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

    def path(self, src, dest):
        """ implement your shortest path function here """
        shortest_path = [] #holds the shortest path

        q = queue.Queue() 
        q.put(src)  #put src in q
        
        visited = set() 
        visited.add(src) #add src to set of visited vertices        
        
        dist = dict() #dist contains distance of vertices from src
        pred = dict() #contains predecessors of 

        for v in self.vertices:
            dist[v] = None  # set to infinity actually
        dist[src] = 0
        pred[src] = None
        #run regular BFS
        while not q.empty():
            u = q.get() #pop head of q
            #print("u:", u, "dist:", dist[u])
            for v in self.adj_list[u]: #iterate through u's neighbors
                if v not in visited:
                    visited.add(v) #1 add vertex to visited
                    pred[v] = u #2 set its predecessor
                    dist[v] = dist[u] + 1 #3 increment dist
                    q.put(v) #4 put v in q
                    if v == dest: #dest was found, quit BFS
                        break
                    #print("v:",v, "pred:", pred[v],"dist: ", dist[v] )

        #put shortest path between src and dest 
        #found by BFS in shortest_path
        #idea taken from Cesh's lecture
        v = dest
        while v != None:
            shortest_path.insert(0,v)
            v = pred[v]
        return shortest_path

    def levels(self, src):
        """ implement your level set code here """
        level_sizes = []
        #fill level_sizes with zeroes
        for i in range(0,7): 
            level_sizes.append(0)
        level_sizes[0] = 1 #src has only one vertex with distance 0, itself
        q = queue.Queue()
        q.put(src) #put src in queue
        
        visited = set()
        visited.add(src) #add src to visited set  
        
        dist = dict() #dist contains distance of vertices from src
        #pred = dict()
        
        #for v in self.vertices:
        #    dist[v] = None  # set to infinity actually
        dist[src] = 0 #dist of src from itself is 0
        #pred[src] = None
        
        #run regular BFS
        while not q.empty():
            u = q.get() # pop u off q
            #print("u:", u, "dist:", dist[u])
            for v in self.adj_list[u]: #iterate through u's neighbors
                if v not in visited:
                    visited.add(v) #1 v has now been visited
                    #pred[v] = u #2
                    dist[v] = dist[u] + 1 #3 increment dist
                    q.put(v) #4 put v into back of q
                   
                    #check to see dist of v from src
                    #if dist in [1,2,3,4,5,6,7]
                    #increment level_sizes[dist[v]]
                    
                    if dist[v] == 1: 
                        level_sizes[1] += 1
                    elif dist[v] == 2:
                        level_sizes[2] += 1
                    elif dist[v] == 3:
                        level_sizes[3] += 1
                    elif dist[v] == 4:
                        level_sizes[4] += 1
                    elif dist[v] == 5:
                        level_sizes[5] += 1
                    elif dist[v] >= 6:
                        level_sizes[6] += 1
                        #for number 5
                        #print("dist[v]:", dist[v], ", v:",v)
                   
                    
        return level_sizes
