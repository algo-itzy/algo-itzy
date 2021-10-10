class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self

    def get_parent(self):
        while self.parent != self.parent.parent:
            self.parent = self.parent.parent
        return self.parent

    def union(self, Node):
        a = self.get_parent()
        b = Node.get_parent()

        if a.data > b.data:
            a.parent = b
        else:
            b.parent = a
            

class Edge:
    def __init__(self, node_a, node_b, weight):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight
    
    # for debugging
    def __str__(self):
        return f"Edge(node_a: {self.node_a}, node_b: {self.node_b}, weight: {self.weight})"


def Kruskal_MST(graph):
    sum_of_weights = 0

    for edge in graph:
        if nodes[edge.node_a].get_parent() != nodes[edge.node_b].get_parent():
            sum_of_weights += edge.weight
            nodes[edge.node_a].union(nodes[edge.node_b])

    return sum_of_weights


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        V, E = map(int, input().split())
        graph = []
        nodes = [Node(i) for i in range(V+1)]

        for _ in range(E):
            n1, n2, w = map(int, input().split())
            graph.append(Edge(n1, n2, w))
        
        graph.sort(key=lambda x: x.weight)

        print(f"#{tc} {Kruskal_MST(graph)}")

# git commit -m "code: Solve swea L5249 최소 신장 트리 (yoonbaek)"