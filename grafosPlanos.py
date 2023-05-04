import networkx as nx
import networkx as nx
import random
import matplotlib.pyplot as plt

class RandomGraph:
    def __init__(self, num_nodes, num_edges):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.graph = self._create_random_graph()

    def _create_random_graph(self):
        # Crea un grafo vacío
        G = nx.Graph()

        # Agrega nodos
        nodes = list(range(self.num_nodes))
        G.add_nodes_from(nodes)

        # Agrega aristas
        edges = []
        while len(edges) < self.num_edges:
            # Selecciona dos nodos aleatorios
            node1 = random.choice(nodes)
            node2 = random.choice(nodes)

            # Asegúrate de que los nodos no estén conectados y no sean el mismo nodo
            if node1 != node2 and not G.has_edge(node1, node2):
                edges.append((node1, node2))

        G.add_edges_from(edges)

        # Asigna posiciones aleatorias a los nodos
        pos = {node: (random.random(), random.random()) for node in nodes}

        # Almacena las posiciones como un atributo del grafo
        nx.set_node_attributes(G, pos, 'pos')

        return G

random_graph = RandomGraph(num_nodes=8, num_edges=16)
print(random_graph.graph.nodes)
print(random_graph.graph.edges)
nx.draw(random_graph.graph, pos=nx.get_node_attributes(random_graph.graph, 'pos'))
plt.show()  # <-- Mostrar la ventana emergente
