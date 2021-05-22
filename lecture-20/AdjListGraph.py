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

    def dft(self, value):
        start = self.vertices[value]
        stack = []
        to_process = set()

        stack.append(start)
        to_process.add(start)

        while len(stack) > 0:
            top = stack.pop()
            print(top.value)

            for neighbour in top.neighbours:
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

            for neighbour in top.neighbours:
                if neighbour not in to_process:
                    stack.append(neighbour)
                    to_process.add(neighbour)

        return False

    def bft(self, value):
        start = self.vertices[value]
        queue = []
        to_process = set()

        queue.append(start)
        to_process.add(start)

        while len(queue) > 0:
            top = queue.pop(0)
            print(top.value)

            for neighbour in top.neighbours:
                if neighbour not in to_process:
                    queue.append(neighbour)
                    to_process.add(neighbour)

    def min_dist_eq(self, value):
        start = self.vertices[value]
        queue = []
        to_process = set()

        queue.append(start)
        to_process.add(start)
        queue.append(None)
        layer = 0

        while len(queue) > 1:
            top = queue.pop(0)

            if not top:
                queue.append(None)
                layer += 1
                continue

            print(top.value, layer)

            for neighbour in top.neighbours:
                if neighbour not in to_process:
                    queue.append(neighbour)
                    to_process.add(neighbour)


graph = Graph()
graph.create_vertex("A")
graph.create_vertex("B")
graph.create_vertex("C")
graph.create_vertex("D")

graph.create_edge("A", "B")
graph.create_edge("C", "D")
graph.create_edge("B", "D")
graph.create_edge("A", "D")

graph.min_dist_eq("A")





