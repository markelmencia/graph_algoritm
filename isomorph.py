import random

g1 = [
    [2,1,0,0,1],
    [1,0,1,1,1],
    [0,1,2,1,0],
    [0,1,1,0,0],
    [1,1,0,0,0]
]

g2 = [
    [0,1,2,1,0],
    [1,1,0,0,0],
    [2,1,0,0,1],
    [0,1,1,0,0],
    [1,0,1,1,1]
]

def swap_graph_vertices(graph, v1, v2):

    v1 -= 1
    v2 -= 1

    graph[v1], graph[v2] = graph[v2], graph[v1]
    return graph

def edge_amm(graph):
    result = 0

    for line in graph:
        for num in line:
            result += num
    
    return result / 2
    
def degrees(graph):
    result = []
    for line in graph:
        sum = 0
        for num in line:
            sum += num
        result.append(sum)
    return result

def compare_degrees(graph_degrees1, graph_degrees2):
    # True if same degrees, false if not
    d2 = graph_degrees2

    for degree in graph_degrees1:
        if (degree in d2):
            d2.remove(degree)
        else:
            return False
    return True

def link_degrees(graph1, graph2):

    graph1_copy = graph1
    graph2_copy = graph2

    d1 = degrees(graph1)
    d2 = degrees(graph2)
    
    ordered_graph1 = []
    ordered_graph2 = []

    for _ in range(len(graph1)):
        ordered_graph1.append(graph1[d1.index(min(d1))])
        graph1_copy.remove(graph1[d1.index(min(d1))])
        d1.remove(min(d1))

    for _ in range(len(graph2)):
        ordered_graph2.append(graph2[d2.index(min(d2))])
        graph2_copy.remove(graph2[d2.index(min(d2))])
        d2.remove(min(d2))

    print(ordered_graph1)
    print(ordered_graph2)

def isomorphs(graph1, graph2):
    if (len(graph1) != len(graph2)): # Checks if the amount of vertices in both graphs is the same
        return False
    
    if (edge_amm(graph1) != edge_amm(graph2)): # Checks if the amount of edges in both graphs is the same
        return False

    if (compare_degrees(degrees(graph1), degrees(graph2)) == False): # Checks if both graphs' vertices have the same degrees
        return False

