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

    def dft(self, value):
        start = self.vertices[value]
        stack = []
        to_process = set()

        stack.append(start)
        to_process.add(start)

        while len(stack) > 0:
            top = stack.pop()
            print(top.value)

            for neighbour, weight in top.neighbours:
                if neighbour not in to_process:
                    stack.append(neighbour)
                    to_process.add(neighbour)

    def dfs(self, value, target):
        start = self.vertices[value]
        stack = []
        to_process = set()

        stack.append(start)
        to_process.add(start)

        while len(stack) > 0:
            top = stack.pop()
            if top.value == target:
                return True

            for neighbour, weight in top.neighbours:
                if neighbour not in to_process:
                    stack.append(neighbour)
                    to_process.add(neighbour)

        return False
    #
    def bft(self, value):
        start = self.vertices[value]
        queue = []
        to_process = set()

        queue.append(start)
        to_process.add(start)

        while len(queue) > 0:
            top = queue.pop(0)
            print(top.value)

            for neighbour, weight in top.neighbours:
                if neighbour not in to_process:
                    queue.append(neighbour)
                    to_process.add(neighbour)

    def connected_components(self):
        components = []
        stack = []
        to_process = set()

        for start in self.vertices.values():
            if start in to_process:
                continue

            component = []
            stack.append(start)
            to_process.add(start)

            while len(stack) > 0:
                top = stack.pop()

                component.append(top.value)
                for neighbour, weight in top.neighbours:
                    if neighbour not in to_process:
                        stack.append(neighbour)
                        to_process.add(neighbour)

            components.append(component)

        return components


graph = Graph()
graph.create_vertex("A")
graph.create_vertex("B")
graph.create_vertex("C")
graph.create_vertex("D")
graph.create_vertex("E")
graph.create_vertex("F")

graph.create_edge("A", "B", 10)
graph.create_edge("C", "B", 20)

graph.create_edge("E", "D", 30)
graph.create_edge("F", "D", 40)

print(graph.connected_components())





