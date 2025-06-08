class Graph:
    def __init__(self):
        self.graph = {}       

    def add_edge(self, u, v):
        self.graph.setdefault(u, set()).add(v)
        self.graph.setdefault(v, set()).add(u)   
          