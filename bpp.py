import random
import numpy as np

def create_graph(bins, items):
    graph = []
    list = []
    for i in range(items):
        for j in range(bins):
            list.append(random.random())
        graph.append(list)
        list = []
    return graph


def find_path(graph):
    path_taken = []
    for i in range(len(graph)):
        probabilitylist = []
        total = sum(graph[i])
        for j in range(len(graph[0])):
            probabilitylist.append(graph[i][j]/total)
        #random.choice(probabilitylist)
        #choice_ = np.random.choice([1, 2, 3], 1, p= probabilitylist)
        path_taken.append(np.random.choice([i for i in range(len(graph[0]))], 1, p= probabilitylist)[0])
        
    return path_taken

def set_P_paths(p, graph):
    paths = []
    for i in range(p):
        paths.append(find_path(graph))
    return paths

def fitness(bins):
    """ 
    This takes the list of bins and returns the difference between the minimum and maximum of the sums of the bins.
    """
    sums = []
    for i in bins:
        sums.append(sum(i))
    fitness = max(sums) - min(sums)
    return fitness

def fill_bins(bins, path, weights):
    """
    The paths are converted into bins of weights. The list of lists returned has a list of weights in each bin.
    """
    binlist = []
    for i in range(bins):
        binlist.append([])
    for j in range(len(path)):
        binlist[path[j]].append(weights[j])
    return binlist

def update_pher(graph, path, fitness):
    """
    a new graph is returned with the updated pheromones for 1 ant path
    """
    pheremone = 100/fitness
    new_graph = graph.copy()
    for i in range(len(path)):
        new_graph[i][path[i]] = graph[i][path[i]] + pheremone  
    return new_graph

def evapourate(evap_rate, graph):
    print(graph)
    for bin in range(len(graph)):
        new_bin = [j * evap_rate for j in graph[bin]]
        graph[bin] = new_bin
    print(graph)
    return graph

def runall():
    graph = create_graph()
    weights = [i for i in range(500)]
    bins = 3
    p = 100
    p_paths = set_P_paths(p, graph)
    binlist = []
    for path in p_paths:
        binlist.append(fill_bins(bins, path, weights))
    
    
weights = [i for i in range(500)]
graph = create_graph(3, 500)
# printgraph(graph)
path = find_path(graph)
# print(set_P_paths(5, graph))
bins = fill_bins(3, path, weights)
# print(fitness(bins))
# print(update_pher(graph , path, fitness(bins)))
evapourate(0.3, graph)