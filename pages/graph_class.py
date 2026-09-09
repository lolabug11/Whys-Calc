from collections import deque
class GraphError(Exception):
    pass
class VertexNotFound(GraphError):
    def __init__(self, v):
        self.v = v
        super().__init__(f'{v} is not a real vertex')
class EdgeError(GraphError):
    def __init__(self, v1,v2):
        self.v1 = v1
        self.v2 = v2 
        super().__init__(f'There is something wrong with the edges {v1} and {v2}')
class ValidWeightError(GraphError):
    def __init__(self,):
        super().__init__('The supplied weight is not a valid weight')
class WeightNoneError(GraphError):
    def __init__(self):
        super().__init__('Your graph is weighted but the weight for an edge is `None`')



class Graph:
    def __init__(self, directional = False, weighted = False):
        self.adj_list = {}
        self.directional = directional
        self.weighted = weighted

    def __str__(self):
        return str(self.adj_list)
    
    def print_adj_list(self):
        print(self.adj_list)
    def _validate_vertex(self,vertex):
        if vertex not in self.adj_list:
            raise VertexNotFound(vertex)
    
    def _validate_edge(self, v1 , v2):  
        self._validate_vertex(v1)
        if v2 not in self.adj_list[v1]:
            raise EdgeError(v1,v2)

    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    
    def add_edge(self, v1,v2, weight = None):        
        if isinstance(weight,(int,float,type(None))) and (weight != True and weight != False):
            
            if self.weighted and weight is None:
                raise WeightNoneError()
            if not self.vertex_exists(v1):
                self.add_vertex(v1)
            if not self.vertex_exists(v2):
                self.add_vertex(v2)
            v1_neighbors = self.get_neighbors(v1)
            v2_neighbors = self.get_neighbors(v2)
            if not self.weighted and not self.directional:
                if v2 not in v1_neighbors and v1 not in v2_neighbors:
                    self.adj_list[v1][v2] = None
                    self.adj_list[v2][v1] = None
                else:
                    raise EdgeError(v1,v2)
            elif not self.directional and self.weighted:
                if v2 not in v1_neighbors and v1 not in v2_neighbors:
                    self.adj_list[v1][v2] = weight
                    self.adj_list[v2][v1] = weight
                else:
                    raise EdgeError(v1,v2)
            elif self.directional and self.weighted:
                if v2 not in v1_neighbors:
                    self.adj_list[v1][v2] = weight
                else:
                    raise EdgeError(v1,v2)
            elif self.directional and not self.weighted:
                if v2 not in v1_neighbors:
                    self.adj_list[v1][v2] = None
                else:
                    raise EdgeError(v1,v2)
        else:
            raise ValidWeightError
    def remove_edge(self,v1,v2):
        self._validate_edge(v1,v2)
        v1_neighbors = self.adj_list[v1]
        v2_neighbors = self.adj_list[v2]
        if v1 == v2:
            del v1_neighbors[v2]
            self.adj_list[v1] = v1_neighbors
        else:
            if self.directional:
                del v1_neighbors[v2]
                self.adj_list[v1] = v1_neighbors
            else:
                del v1_neighbors[v2]
                self.adj_list[v1] = v1_neighbors
                del v2_neighbors[v1]
                self.adj_list[v2] = v2_neighbors

    def vertex_count(self):
        return len(self.adj_list)

    def edge_count(self):
        total_edges = 0
        if self.directional:
            for vertex in self.adj_list:
                for edge in self.adj_list[vertex]:
                    total_edges += 1
            return total_edges
        else:
            visited_edges = set()
            for vertex in self.adj_list:
                for edge in self.adj_list[vertex]:
                    if (vertex, edge) not in visited_edges and (edge, vertex) not in visited_edges:
                        visited_edges.add((vertex,edge))
            for edge in visited_edges:
                total_edges += 1
            return total_edges

    def get_neighbors(self,vertex):
        self._validate_vertex(vertex)

        return self.adj_list[vertex]
    
    def remove_vertex(self,vertex):
        self._validate_vertex(vertex)
        del self.adj_list[vertex]
        for v in self.adj_list:
            if vertex in self.adj_list[v]:
                del self.adj_list[v][vertex]
    
    def vertex_exists(self, vertex):

        return vertex in self.adj_list

    def edge_exists(self,v1,v2):      
        self._validate_vertex(v1)
        self._validate_vertex(v2)
        if v2 in self.adj_list[v1]:
            return True
        return False
    
    def degree(self,vertex):
        degree = 0
        self._validate_vertex(vertex)
        if self.directional:
            return len(self.adj_list[vertex])
        else:
            for connection in self.adj_list[vertex]:
                if connection != vertex:
                    degree += 1
                elif connection == vertex:
                    degree += 2
            return degree

    def degree_sequence(self):
        sequence = []
        for x in self.adj_list:
            sequence.append(self.degree(x))
        sequence.sort(reverse=True)
        return sequence
    
    def average_degree(self):
        if len(self.adj_list) > 0:
            sequence = self.degree_sequence()
            total = 0
            for degree in sequence:
                total += degree
            return total/len(sequence)
        return None
        

    def max_possible_edges(self):
        if not self.directional:
            n = len(self.adj_list)  
            return (n*(n+1))//2
        else:
            n = len(self.adj_list)
            return n**2
        
            
    def density(self):
        if len(self.adj_list) > 0:
            max_possible_edges = self.max_possible_edges()
            total_edges_in_graph = self.edge_count()
            return total_edges_in_graph / max_possible_edges
        return None
    
    def is_complete(self):
        density = self.density()
        return density == 1 or density is None
    
    def breath_first_search(self,start):
        self._validate_vertex(start)
        to_visit = deque([start])
        visited_set = set([start])
        visited_list = []
        while len(to_visit) > 0:
            current = to_visit.popleft()
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited_set:
                    to_visit.append(neighbor)
                    visited_set.add(neighbor)
            visited_list.append(current)
        return visited_list
    


    def is_connected(self):
        if len(self.adj_list) != 0:
            connected = 0
            for x in self.adj_list:
                if len(self.breath_first_search(x)) == len(self.adj_list):
                    connected += 1
            if connected == len(self.adj_list):
                return True
            return False
        return True
    


        
g = Graph(weighted=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A','B')
g.add_edge('A','A')
g.add_edge('B','B')
print(g)
print(g.get_neighbors('A'), ' neighbors of a')
print(g.is_connected())
g.remove_vertex('A')
print(g)