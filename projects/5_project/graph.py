from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

#class Vertex:
#    '''Add additional helper methods if necessary.'''
#    def __init__(self, key):
#        '''Add other attributes as necessary'''
#        self.id = key
#        self.adjacent_to = []

class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency
            list representation You may assume the graph is not empty and is a correct specification.
            E.g. each edge is represented by a pair of vertices.  Note that the graph is not directed
            so each edge specified in the input file should appear on the adjacency list of each
            vertex of the two vertices associated with the edge.'''
        fp = open(filename, 'r')
        self.graph = {}
        for line in fp.readlines():
            line = line.split()
            if line[0] in self.graph:
                self.graph[line[0]].append(line[1])
            else:
                self.graph.update({line[0]:[line[1]]})
            if line[1] in self.graph:
                self.graph[line[1]].append(line[0])
            else:
                self.graph.update({line[1]:[line[0]]})
        fp.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if key not in self.graph:
            self.graph.update({key:[]})

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        if key in self.graph:
            return key
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return sorted(self.graph)

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        output = []
        check = {}
        s = Stack(len(self.graph))
        for vertex in self.graph:
            if vertex not in check:
                cur = []
                s.push(vertex)
                cur.append(vertex)
                check.update({vertex:None})
                while s.num_items!=0:
                    for i in self.graph[s.items[s.num_items-1]]:
                        if i not in check:
                            s.push(i)
                            cur.append(i)
                            check.update({i:None})
                            break
                    else:
                        s.pop()
                output.append(sorted(cur))
        return sorted(output)

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        check = {}
        q = Queue(len(self.graph))
        for vertex in self.graph:
            if vertex not in check:
                q.enqueue(vertex)
                check.update({vertex:True})
                while q.num_items!=0:
                    for i in self.graph[q.items[q.front]]:
                        if i not in check:
                            q.enqueue(i)
                            check.update({i:not check[q.items[q.front]]})
                            break
                    else:
                        for i in self.graph[q.items[q.front]]:
                            if check[i]==check[q.items[q.front]]:
                                return False
                        q.dequeue()
        return True
