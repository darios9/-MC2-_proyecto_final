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

        # Agrega nodos con una letra del abecedario como atributo
        nodes = list(range(self.num_nodes))
        letters = [chr(i) for i in range(65, 65 + self.num_nodes)]
        node_attributes = {node: {'letter': letter} for node, letter in zip(nodes, letters)}
        for node, attributes in node_attributes.items():
            G.add_node(node, **attributes)

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
    
    def draw_path(self, start_letter, end_letter):
        # Busca los nodos que corresponden a las letras dadas
        start_node = None
        end_node = None
        for node, attributes in self.graph.nodes(data=True):
            if attributes['letter'] == start_letter:
                start_node = node
            elif attributes['letter'] == end_letter:
                end_node = node

        # Si alguna de las letras no corresponde a ningún nodo, muestra un mensaje de error
        if start_node is None or end_node is None:
            print(f"Error: No se encontró algún nodo correspondiente a las letras '{start_letter}' o '{end_letter}'.")
            return

        # Busca el camino más corto entre los dos nodos
        path = nx.shortest_path(self.graph, start_node, end_node)

        # Crea un nuevo grafo solo con los nodos y aristas del camino
        path_graph = self.graph.subgraph(path)

        # Obtiene la posición de cada nodo y la letra del atributo 'letter'
        pos = nx.get_node_attributes(path_graph, 'pos')
        labels = nx.get_node_attributes(path_graph, 'letter')

        # Dibuja el grafo
        nx.draw(path_graph, pos, labels=labels, with_labels=True)

        # Muestra el grafo en una ventana emergente
        import matplotlib.pyplot as plt
        plt.show()

    def draw_ordered_path(self, start_letter, end_letter):
        # Busca los nodos que corresponden a las letras dadas
        start_node = None
        end_node = None
        for node, attributes in self.graph.nodes(data=True):
            if attributes['letter'] == start_letter:
                start_node = node
            elif attributes['letter'] == end_letter:
                end_node = node

        # Si alguna de las letras no corresponde a ningún nodo, muestra un mensaje de error
        if start_node is None or end_node is None:
            print(f"Error: No se encontró algún nodo correspondiente a las letras '{start_letter}' o '{end_letter}'.")
            return

        # Busca el camino más corto entre los dos nodos
        path = nx.shortest_path(self.graph, start_node, end_node)

        # Crea un nuevo grafo solo con los nodos y aristas del camino
        path_graph = self.graph.subgraph(path)

        # Obtiene la posición de cada nodo y la letra del atributo 'letter'
        pos = nx.get_node_attributes(path_graph, 'pos')
        labels = nx.get_node_attributes(path_graph, 'letter')

        # Ordena los nodos según su posición en el camino
        ordered_nodes = sorted(path_graph.nodes, key=lambda x: path.index(x))

        # Crea un nuevo grafo solo con los nodos en orden y sus aristas
        ordered_graph = nx.Graph()
        for i, node in enumerate(ordered_nodes):
            ordered_graph.add_node(i, pos=pos[node], letter=self.graph.nodes[node]['letter'])
            if i > 0:
                prev_node = ordered_nodes[i-1]
                if self.graph.has_edge(node, prev_node):
                    ordered_graph.add_edge(i, i-1)

        # Dibuja el grafo
        nx.draw(ordered_graph, nx.get_node_attributes(ordered_graph, 'pos'), labels=nx.get_node_attributes(ordered_graph, 'letter'), with_labels=True)

        # Muestra el grafo en una ventana emergente
        import matplotlib.pyplot as plt
        plt.show()



    def show_graph(self):
        # Obtiene la posición de cada nodo y la letra del atributo 'letter'
        pos = nx.get_node_attributes(self.graph, 'pos')
        labels = nx.get_node_attributes(self.graph, 'letter')

        # Dibuja el grafo
        nx.draw(self.graph, pos, labels=labels, with_labels=True)

        # Muestra el grafo en una ventana emergente
        import matplotlib.pyplot as plt
        plt.show()

'''random_graph = RandomGraph(8, 10)
random_graph.show_graph()

# Dibujar camino entre nodos 'A' y 'D'
#random_graph.draw_path('A', 'D')
random_graph.draw_ordered_path('A','D')'''


