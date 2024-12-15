import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph(parent, algorithm, adjacency_list, weighted=False):
    """ 
    Plot a graph from an adjacency list and display it in the given parent widget.
    """
    G = nx.DiGraph()

    # Add edges
    for node, neighbors in adjacency_list.items():
        if weighted:
            G.add_weighted_edges_from((node, neighbor, weight) for neighbor, weight in neighbors)
        else:
            G.add_edges_from((node, neighbor) for neighbor in neighbors)

    pos = _binary_tree_layout(G, list(adjacency_list.keys())[0])

    # Create a figure and draw the graph
    fig, ax = plt.subplots(figsize=(5,3))
    nx.draw(
        G, pos, with_labels=True, ax=ax, 
        node_color='white', node_size=250, font_size=12, font_weight='normal',
    )

    if weighted:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, font_size=8)

    ax.set_title(f"{algorithm} Graph")
    fig.tight_layout()

    # Embed the figure in the parent widget
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

    # Ensure the figure is closed to prevent lingering Tk references
    plt.close(fig)


def _binary_tree_layout(G, root, width=2.0, height=1.0, x_offset=0.0, y_offset=0.0, layer_sep=1.5, pos=None, level=0, visited=None):
    """ Recursively generate positions for a binary tree-like layout with cycle detection. """
    if pos is None:
        pos = {}
    if visited is None:
        visited = set()

    if root in visited:
        return pos
    visited.add(root)

    children = list(G.successors(root))
    if not children:
        pos[root] = (x_offset, y_offset)
    else:
        mid = len(children) // 2
        for i, child in enumerate(children):
            dx = width / 2 ** (level + 1)
            next_x = x_offset + (i - mid) * dx
            next_y = y_offset - layer_sep
            _binary_tree_layout(G, child, width, height, next_x, next_y, layer_sep, pos, level + 1, visited)
        pos[root] = (x_offset, y_offset)

    return pos