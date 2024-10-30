class Graph:

    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        # print("hii",[0] * size for _ in range(size))
        # print("hii",self.adj_matrix)
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v,weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            # self.adj_matrix[u][v] = 1
            # self.adj_matrix[v][u] = 1
            self.adj_matrix[u][v] = weight

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        print("\data",self.vertex_data)
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")


g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
# g.add_edge(0, 1)  # A - B
# g.add_edge(0, 2)  # A - C
# g.add_edge(0, 3)  # A - D
# g.add_edge(1, 2)  # B - C

g.add_edge(0, 1, 3)  # A -> B with weight 3
g.add_edge(0, 2, 2)  # A -> C with weight 2
g.add_edge(3, 0, 4)  # D -> A with weight 4
g.add_edge(2, 1, 1)  # C -> B with weight 1


g.print_graph()