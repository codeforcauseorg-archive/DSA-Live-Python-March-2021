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


    def create_edge(self, first, second):

        if (first in self.vertices) and (second in self.vertices):
            vfirst = self.vertices[first]
            vsecond = self.vertices[second]

            vfirst.neighbours.append(vsecond)
            vsecond.neighbours.append(vfirst)

    def display(self):
        for vertex in self.vertices.values():
            print(vertex.value, end=" => ")
            print(", ".join([neighbour.value for neighbour in vertex.neighbours]))


graph = Graph()
graph.create_vertex("A")
graph.create_vertex("B")
graph.create_vertex("C")
graph.create_vertex("D")

graph.create_edge("A", "B")
graph.create_edge("C", "D")
graph.create_edge("B", "D")
graph.create_edge("A", "D")

graph.display()





