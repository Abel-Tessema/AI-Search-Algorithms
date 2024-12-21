bidirectional_search_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

bidirectional_search_graph_1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 1)],
    'D': [('B', 2), ('G', 1)],
    'E': [('B', 5), ('G', 2)],
    'F': [('C', 1), ('G', 3)],
    'G': [('D', 1), ('E', 2), ('F', 3)]
}

bfs_and_dfs_search_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

depth_limited_search_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'I'],
    'D': ['J'],
    'E': ['K', 'L'],
    'F': [],
    'G': ['M'],
    'H': [],
    'I': ['N', 'O'],
    'J': ['P'],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
    'P': []
}

iddfs_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

uniform_cost_search_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

informed_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

informed_heuristic = {
    'A': 7,
    'B': 6,
    'C': 8,
    'D': 3,
    'E': 2,
    'F': 6,
    'G': 0
}

informed_detail = (informed_graph, informed_heuristic)