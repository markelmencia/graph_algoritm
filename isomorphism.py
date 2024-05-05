import copy

'''
        # EXAMPLES (remove quotation marks): (g1, g2), (g5, g6), (g9, g10) are isomorphic. Any other graph combination is not

        g1 = [
            [0,1,1,1,1],
            [1,0,0,0,0],
            [1,0,2,2,0],
            [1,0,2,0,1],
            [1,0,0,1,2]
        ]

        g2 = [
            [0,1,1,2,0],
            [1,2,1,0,0],
            [1,1,0,1,1],
            [2,0,1,2,0],
            [0,0,1,0,0]
        ]

        g3 = [
            [0,1,1,0,0],
            [1,0,0,1,1],
            [1,0,0,1,0],
            [0,1,1,2,2],
            [1,1,0,2,0]
        ]

        g4 = [
            [0,0,1,1,1],
            [0,0,1,2,1],
            [1,1,0,0,0],
            [1,2,0,2,1],
            [1,1,0,1,0]
        ]

        g5 = [
            [2,1,0,0,1],
            [1,0,1,1,1],
            [0,1,2,1,0],
            [0,1,1,0,0],
            [1,1,0,0,0]
        ]

        g6 = [
            [2,0,0,1,1],
            [0,2,1,1,0],
            [0,1,0,1,0],
            [1,1,1,0,1],
            [1,0,0,1,0]
        ]

        g7 = [
            [2,0,0,0,1],
            [0,2,1,0,1],
            [0,1,0,1,0],
            [0,0,1,0,1],
            [1,1,0,1,0]
        ]

        g8 = [
            [0,1,0,1,0],
            [1,0,1,0,1],
            [0,1,0,1,0],
            [1,0,1,2,0],
            [0,1,0,0,2]
        ]

        g9 = [
            [0,1,2,1,1],
            [1,0,1,1,0],
            [2,1,2,1,1],
            [1,1,1,0,2],
            [1,0,1,2,0]
        ]

        g10 = [
            [0,1,2,1,1],
            [1,2,1,2,1],
            [2,1,0,1,0],
            [1,2,1,0,1],
            [1,1,0,1,0]
        ]
'''


def get_edges(graph):
    # Gets the edge ammount in the graph
    sum = 0
    for line in graph:
        for num in line:
            sum += num
    return sum / 2


def get_degree(vertex):
    # Gets the degree of the vertex of a graph
    return sum(vertex)


def get_degrees(graph):
    # Gets the degrees of every vertex of the graph
    result = []
    for file in graph:
        sum = 0
        for num in file:
            sum += num
        result.append(sum)
    return result
   

def swap_files_columns(graph, fc1, fc2):
    # Swaps the fc1'th and fc2'th files and columns
    graph[fc1 - 1], graph[fc2 - 1] = graph[fc2 - 1], graph[fc1 - 1]

    for line in graph:
        line[fc1 - 1], line[fc2 - 1] = line[fc2 - 1], line[fc1 - 1]


def pair_graphs(graph1, graph2):
    # Swaps files and columns to make all files of the matrix have the same degree
    pair_movements = []
    graph1_degrees = get_degrees(graph1)
    graph2_degrees = get_degrees(graph2)

    for i in range(len(graph1_degrees)): # gets all the possible file and column swaps
        num_index = graph2_degrees.index(graph1_degrees[i])
        pair_movements.append([i + 1, num_index + 1])
        # graph2_degrees[num_index] = -1

    sorted_pair_movements = [] 
    for pair1 in pair_movements: # Removes unnecessary swaps
        if ((pair1[0] != pair1[1]) and pair1[0] != -1):
            sorted_pair_movements.append(copy.deepcopy(pair1))
            for pair2 in pair_movements:
                if pair1[0] == pair2[1]:
                    pair2[0] = -1
    
    for pair in sorted_pair_movements: # Does the swaps
        swap_files_columns(graph2, pair[0], pair[1])


def find_permutations(graph):
    # Gets all the possible permutations
    result = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if ((i != j) and (get_degree(graph[i]) == get_degree(graph[j]))):
                result.append([i + 1, j + 1])

    for pair1 in result: # Finds the unnecessary ones
        for pair2 in result:
            if pair1[0] == pair2[1] and pair1[1] == pair2[0]:
                pair2[0] = - 1

    sorted_result = []
    for pair in result: # Removes them
        if pair[0] >= 0:
            sorted_result.append(pair)
    return sorted_result


def permute(graph1, graph2):
    # Permutes through every possible combination until it finds an equal graph or not
    permutation_pairs = find_permutations(graph2)
    init_permutation = copy.deepcopy(graph2)

    if (graph1 == graph2): # Checks if init == graph1
            return True

    for pair1 in permutation_pairs: # Goes through every permutation combination
        graph2 = copy.deepcopy(init_permutation)
        swap_files_columns(graph2, pair1[0], pair1[1])
        current_permutation = copy.deepcopy(graph2)

        if (graph1 == graph2):
            return True
        
        for pair2 in permutation_pairs:
            graph2 = copy.deepcopy(current_permutation)
            if pair1 != pair2:
                swap_files_columns(graph2, pair2[0], pair2[1])
                if (graph1 == graph2):
                    return True
   
    return False


def isomorphic(graph1, graph2):
    # MAIN FUNCTION: Returns true if the graphs are isomorphic or false if they're not
    if (len(graph1) != len(graph2)): 
        # Checks that both graphs have the same vertex amount
        return False
    
    if (get_edges(graph1) != get_edges(graph2)):
        # Checks that both graphs have the same edge ammount
        return False
    
    if (get_degrees(graph1).sort() != get_degrees(graph2).sort()): 
        # Checks that both graphs have the same degrees in every vertex
        return False
    
    pair_graphs(graph1, graph2) # Pairs the graphs to permute one of them
    
    return permute(graph1, graph2) # Permutes graph2 and returns whether the graphs are isomorphic
