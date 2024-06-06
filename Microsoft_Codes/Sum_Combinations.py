# Problem Statement: Given a positive integer, target, print all possible combinations of positive
# integers that sum up to the target number.

# For example, if we are given input ‘5’, these are the possible sum combinations.

# if we are given input ‘5’, these are the possible sum combinations.

# 1, 4
# 2, 3
# 1, 1, 3
# 1, 2, 2
# 1, 1, 1, 2
# 1, 1, 1, 1, 1


# Simple Graphs
#
# class Graph:
#
#     def __init__(self):
#         self.nodes = set()
#         self.edges = {}
#
#     def add_nodes(self, value):
#         self.nodes.add(value)
#         if value not in self.edges:
#             self.edges[value] = []
#
#     def add_edges(self, from_node, to_node):
#         if from_node in self.nodes and to_node in self.nodes:
#             self.edges[from_node].append(to_node)
#             self.edges[to_node].append(from_node)
#         else:
#             raise ValueError("Both the nodes should be in the graph")
#
#     def __repr__(self):
#         return f"Nodes: {self.nodes}\nEdges: {self.edges}"
#
#
# g = Graph()
#
# g.add_nodes("A")
# g.add_nodes("B")
# g.add_nodes("C")
# g.add_nodes("D")
#
# g.add_edges("A", "B")
# g.add_edges("B", "C")
# g.add_edges("C", "D")
# g.add_edges("D", "A")
#
# print(g)





class Graph:

    def __init__(self):
        self.node = set()
        self.edge = {}

    def add_node(self,value):
        self.node.add(value)
        if value not in self.edge:
            self.edge[value] = []

    def add_edge(self,from_node,to_node):
        if from_node in self.node and to_node in self.node:
            self.edge[from_node].append(to_node)
            self.edge[to_node].append(from_node)
        else:
            print("Both the values should be in graph")

















