class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []


class Graph:

    def __init__(self):
        self.vertices = {}

    def create_vertex(self, value):
        if value not in self.vertices:
            vertex = Vertex(value)
            self.vertices[value] = vertex

    def create_edge(self, first, second, weight):

        if (first in self.vertices) and (second in self.vertices):
            vfirst = self.vertices[first]
            vsecond = self.vertices[second]

            vfirst.neighbours.append((vsecond, weight))
            vsecond.neighbours.append((vfirst, weight))

    def display(self):
        for vertex in self.vertices.values():
            print(vertex.value, end=" => ")
            print(", ".join([str(neighbour.value) + " : " + str(weight) for (neighbour, weight) in vertex.neighbours]))


    @classmethod
    def find(cls, current, p_map):
        while p_map[current] != None:
            current = p_map[current]
        return current

    @classmethod
    def union(cls, first, second, p_map):

        rep_f = Graph.find(first, p_map)
        rep_s = Graph.find(second, p_map)

        if rep_f != rep_s:
            p_map[rep_f] = rep_s
            return True
        else:
            return False

    def mst(self):
        weight_mst = 0
        edges = []

        for vertex in self.vertices.values():
            first = vertex.value
            for (second, weight) in vertex.neighbours:
                edges.append((weight, first, second.value))

        sorted_edges = sorted(edges)

        p_map = {}
        for vertex in self.vertices.keys():
            p_map[vertex] = None

        for (weight, first, second) in sorted_edges:
            if Graph.union(first, second, p_map):
                weight_mst += weight

        return weight_mst


graph = Graph()
graph.create_vertex("A")
graph.create_vertex("B")
graph.create_vertex("C")
graph.create_vertex("D")

graph.create_edge("A", "B", 20)
graph.create_edge("A", "C", 10)

graph.create_edge("A", "D", 5)
graph.create_edge("B", "D", 15)
graph.create_edge("C", "D", 6)

print(graph.mst())





