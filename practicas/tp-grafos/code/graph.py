class GraphNode:
    def __init__(self , key = None):
        self.key = key
        self.list = []


class Graph:
    def __init__(self , vertices = None):
        self.vertices = len(vertices)

    def createGraph(self , vertices, aristas):
        dict = {}
        for key in range(len(vertices)):
            pos = vertices[key]
            dict[pos] = GraphNode(pos)

        dict = self.connections(dict , aristas)
        return dict

    def connections(self , dict , aristas):

        for (v1 , v2) in aristas:
            dict[v1].list.append(v2)
            dict[v2].list.append(v1)
        return dict
    
    def print_graph(self , graph):
        for key in graph:
            print(f"{key}: {graph[key].list}")