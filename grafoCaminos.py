from graphviz import Graph

class Grafo:
    def __init__(self, vertices, inicio, final):
        self.vertices = vertices
        self.inicio = inicio
        self.final = final
        
    def llenar_vertices(self, n):
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.vertices = list(abc[:n])
    
    def asignar_letras(self, inicio, final):
        self.inicio = chr(65 + inicio - 1)
        self.final = chr(65 + final - 1)
        
    def crear_grafo(self):
        # Crear el objeto Graph de graphviz
        dot = Graph(comment='Multigrafo no dirigido')
        
        # Agregar los vértices al grafo
        for v in self.vertices:
            if v == self.inicio:
                dot.node(v, style='filled', fillcolor='red')
            elif v == self.final:
                dot.node(v, style='filled', fillcolor='green')
            else:
                dot.node(v)
        
        # Recorrer la matriz y agregar las aristas al grafo
        for i in range(len(self.vertices)):
            for j in range(i+1, len(self.vertices)):
                if self.vertices[i] != self.vertices[j] and self.vertices[i] in self.vertices[j]:
                    # Utilizar el atributo "label" para indicar cuántas veces se conectan los nodos
                    dot.edge(self.vertices[i], self.vertices[j], label=str(self.matriz[i][j]))
        
        # Agregar una arista adicional
        dot.edge(self.inicio, self.final, color='blue', penwidth='2.0', label='3')
        
        # Renderizar el grafo y mostrarlo
        dot.render('multigrafo', view=True)


# Crear un objeto de la clase Grafo
g = Grafo([], "", "")

# Llenar la matriz con 5 vértices
g.llenar_vertices(5)

# Asignar las letras "B" y "E" a las variables de la clase
g.asignar_letras(2, 5)

# Definir la matriz con conexiones múltiples
g.matriz = [[0, 3, 1, 2, 1],
            [3, 0, 2, 1, 2],]

