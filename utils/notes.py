notes = {
    "BFS": """
Breadth-First Search (BFS)

Breadth-first search is a graph traversal algorithm that starts traversing the graph from the root node and explores all the neighboring nodes. Then, it selects the nearest node and explores all the unexplored nodes. While using BFS for traversal, any node in the graph can be considered as the root node.

There are many ways to traverse the graph, but among them, BFS is the most commonly used approach. It is a recursive algorithm to search all the vertices of a tree or graph data structure. BFS puts every vertex of the graph into two categories - visited and non-visited. It selects a single node in a graph and, after that, visits all the nodes adjacent to the selected node.

Applications of BFS algorithm

The applications of breadth-first-algorithm are given as follows:
    -BFS can be used to find the neighboring locations from a given source location.
    -In a peer-to-peer network, BFS algorithm can be used as a traversal method to find all the neighboring nodes. Most torrent clients, such as BitTorrent, uTorrent, etc. employ this process to find "seeds" and "peers" in the network.
    -BFS can be used in web crawlers to create web page indexes. It is one of the main algorithms that can be used to index web pages. It starts traversing from the source page and follows the links associated with the page. Here, every web page is considered as a node in the graph.
    -BFS is used to determine the shortest path and minimum spanning tree.
    -BFS is also used in Cheney's technique to duplicate the garbage collection.
    -It can be used in ford-Fulkerson method to compute the maximum flow in a flow network.

Algorithm

The steps involved in the BFS algorithm to explore a graph are given as follows:
    Step 1: SET STATUS = 1 (ready state) for each node in G
    Step 2: Enqueue the starting node A and set its STATUS = 2 (waiting state)
    Step 3: Repeat Steps 4 and 5 until QUEUE is empty
    Step 4: Dequeue a node N. Process it and set its STATUS = 3 (processed state).
    Step 5: Enqueue all the neighbours of N that are in the ready state (whose STATUS = 1) and set their STATUS = 2 (waiting state) 
        [END OF LOOP]
    Step 6: EXIT

Properties of search algorithms

Complete: If the shallowest goal node is at some finite depth, then BFS will find a solution.
Optimal: If the path cost is a non-decreasing function of the depth of the node.
Time Complexity: O(bd)
Space Complexity: O(bd)

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)

""",
    "DFS": """
Depth-First Search (DFS)

It is a recursive algorithm to search all the vertices of a tree data structure or a graph. The depth-first search (DFS) algorithm starts with the initial node of graph G and goes deeper until we find the goal node or the node with no children.

Because of the recursive nature, stack data structure can be used to implement the DFS algorithm. The process of implementing the DFS is similar to the BFS algorithm.

The step by step process to implement the DFS traversal is given as follows:
    1. First, create a stack with the total number of vertices in the graph.
    2. Now, choose any vertex as the starting point of traversal, and push that vertex into the stack.
    3. After that, push a non-visited vertex (adjacent to the vertex on the top of the stack) to the top of the stack.
    4. Now, repeat steps 3 and 4 until no vertices are left to visit from the vertex on the stack's top.
    5. If no vertex is left, go back and pop a vertex from the stack.
    6. Repeat steps 2, 3, and 4 until the stack is empty.

Applications of DFS algorithm

The applications of using the DFS algorithm are given as follows:
    -DFS algorithm can be used to implement the topological sorting.
    -It can be used to find the paths between two vertices.
    -It can also be used to detect cycles in the graph.
    -DFS algorithm is also used for one solution puzzles.
    -DFS is used to determine if a graph is bipartite or not.

Algorithm

The steps involved in the BFS algorithm to explore a graph are given as follows:
    Step 1: SET STATUS = 1 (ready state) for each node in G
    Step 2: Push the starting node A on the stack and set its STATUS = 2 (waiting state)
    Step 3: Repeat Steps 4 and 5 until STACK is empty
    Step 4: Pop the top node N. Process it and set its STATUS = 3 (processed state)
    Step 5: Push on the stack all the neighbors of N that are in the ready state (STATUS = 1) and set their STATUS = 2 (waiting state)
        [END OF LOOP]
    Step 6: EXIT

Properties of search algorithms

Complete: Within finite state space as it will expand every node within a limited search tree.
Not Optimal
Time Complexity: O(nm), where m = maximum depth of any node. This can be much larger than d (Shallowest solution depth).
Space Complexity: O(bm)

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)
        
""",
"DLS": """
Depth-Limited Search (DLS)

Depth Limited Search is a modified version of DFS that imposes a limit on the depth of the search. This means that the algorithm will only explore nodes up to a certain depth, effectively preventing it from going down excessively deep paths that are unlikely to lead to the goal. By setting a maximum depth limit, DLS aims to improve efficiency and ensure more manageable search times.

How Depth Limited Search Works
    1. Initialization: Begin at the root node with a specified depth limit.
    2. Exploration: Traverse the tree or graph, exploring each node's children.
    3. Depth Check: If the current depth exceeds the set limit, stop exploring that path and backtrack.
    4. Goal Check: If the goal node is found within the depth limit, the search is successful.
    5. Backtracking: If the search reaches the depth limit or a leaf node without finding the goal, backtrack and explore other branches.

Depth-limited search can be terminated with two Conditions of failure:
    -Standard failure value: It indicates that problem does not have any solution.
    -Cutoff failure value: It defines no solution for the problem within a given depth limit.

Applications of Depth Limited Search in AI

    -Pathfinding in Robotics: DLS is employed for nonholonomic motion planning of robots in the presence of obstacles. By imposing restriction on the depth it makes the robot stop after exploring a particular depth of an area and restricting the robot from too much wandering.
    -Network Routing Algorithms: A DLS can be implemented to compute paths between nodes in computer networks restricting the number of hops to prevent loops.
    -Puzzle Solving in AI Systems: DLS can be used to solve puzzles such as the 8-puzzle or Sudoku by manipulating possible moves a fixed number of times that reduces how many steps are taken in the search.
    -Game Playing: In AI for games, instead, DLS can be used to plan forward a few moves up to a certain level of depth to help decide how much effort to put into a given decision.

DFS can be used for various tasks, including searching for a path between two nodes, traversing a tree or graph to visit all nodes, or solving certain types of puzzles. It's often used as a building block in more complex algorithms and AI applications, such as solving mazes, analyzing game states, or exploring decision trees in search algorithms like minimax for games like chess or tic-tac-toe.

Properties of search algorithms

Complete: If the solution is above the depth-limit.
Not Optimal
Time Complexity: O(bℓ)
Space Complexity: O(b×ℓ)

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)

""",
    "UCS": """
Uniform-Cost Search (UCS)

Uniform Cost Search is a pathfinding algorithm that expands the least cost node first, ensuring that the path to the goal node has the minimum cost. Unlike other search algorithms like Breadth-First Search (BFS), UCS takes into account the cost of each path, making it suitable for weighted graphs where each edge has a different cost.

Key Concepts of Uniform Cost Search

    -Priority Queue: UCS uses a priority queue to store nodes. The node with the lowest cumulative cost is expanded first. This ensures that the search explores the most promising paths first.
    -Path Cost: The cost associated with reaching a particular node from the start node. UCS calculates the cumulative cost from the start node to the current node and prioritizes nodes with lower costs.
    -Exploration: UCS explores nodes by expanding the least costly node first, continuing this process until the goal node is reached. The path to the goal node is guaranteed to be the least costly one.
    -Termination: The algorithm terminates when the goal node is expanded, ensuring that the first time the goal node is reached, the path is the optimal one.

How Does Uniform Cost Search Work?

UCS operates under a simple principle: among all possible expansions, pick the path that has the smallest total cost from the start node. This is implemented using a priority queue to keep the partial paths in order, based on the total cost from the root node.

Here's the step-by-step process of how UCS works:
    1. Initialization: UCS starts with the root node. It is added to the priority queue with a cumulative cost of zero since no steps have been taken yet.
    2. Node Expansion: The node with the lowest path cost is removed from the priority queue. This node is then expanded, and its neighbors are explored.
    3. Exploring Neighbors: For each neighbor of the expanded node, the algorithm calculates the total cost from the start node to the neighbor through the current node. If a neighbor node is not in the priority queue, it is added to the queue with the calculated cost. If the neighbor is already in the queue but a lower cost path to this neighbor is found, the cost is updated in the queue.
    4. Goal Check: After expanding a node, the algorithm checks if it has reached the goal node. If the goal is reached, the algorithm returns the total cost to reach this node and the path taken.
    5. Repetition: This process repeats until the priority queue is empty or the goal is reached.

Applications of UCS in AI

Uniform Cost Search is widely applicable in various fields within AI:
    -Pathfinding in Maps: Determining the shortest route between two locations on a map, considering different costs for different paths.
    -Network Routing: Finding the least-cost route in a communication or data network.
    -Puzzle Solving: Solving puzzles where each move has a cost associated with it, such as the sliding tiles puzzle.
    -Resource Allocation: Tasks that involve distributing resources efficiently, where costs are associated with different allocation strategies.

Properties of search algorithms

Complete: If there is a solution, UCS will find it.
Optimal: It only selects a path with the lowest path cost.
Time Complexity: O(b1 + [C*/ε]), where C* = cost of the optimal solution, and ε = each step to get closer to the goal node.
Space Complexity: O(b1 + [C*/ε])

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)

""", 
"IDDFS": """
Iterative Deepening Depth-First Search (IDDFS)

Iterative Deepening Search (IDS) is a search algorithm used in AI that blends the completeness of Breadth-First Search (BFS) with the space efficiency of Depth-First Search (DFS). IDS explores a graph or a tree by progressively increasing the depth limit with each iteration, effectively performing a series of DFS operations until the goal node is found.

This approach is particularly advantageous when the depth of the solution is unknown, and we aim to achieve both optimality and completeness without excessive memory usage.

How Iterative Deepening Search Works

The core concept of IDS revolves around repeatedly running a depth-limited DFS up to increasing depth levels. It starts with a depth limit of zero, then increments this limit iteratively. Each iteration performs a DFS search up to the current depth limit.

Here's a step-by-step breakdown of the algorithm:
    -Start at the Root Node: Begin the search from the root node (or starting point).
    -Perform DFS with Depth Limit (L): In each iteration, perform a DFS with a depth limit L.
    -Increment Depth: After each iteration, increment L by 1.
    -Repeat: Continue this process until the goal node is found or the search space is exhausted.

Applications

IDS is particularly useful in AI applications where both memory efficiency and finding the shortest solution path are crucial. Here are a few notable use cases:
    -Game AI (Chess, Go): IDS is widely used in game AI where the search space is vast, and the solution depth is unpredictable. Game trees with millions of possible states are explored more efficiently using IDS.
    -Pathfinding Algorithms: IDS can be employed in real-time pathfinding scenarios, especially in cases where the destination's depth in the search space is unknown, such as robot navigation.
    -Search Engines: IDS can be applied in crawling strategies for search engines, where it's essential to balance memory consumption while ensuring all relevant results are discovered.
    -Puzzle Solving (e.g., 8-puzzle): In AI, solving puzzles where the optimal solution requires traversing multiple states can benefit from IDS, as it efficiently handles the exponential growth of possible states.

Properties of search algorithms

Complete: If the branching factor is finite.
Optimal: If path cost is a non decreasing function of the depth of the node.
Time Complexity: O(bd)
Space Complexity: O(bd)

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)

""", 
    "Bidirectional Search": """
Bidirectional Search

Bidirectional search is an effective search technique used in the field of artificial intelligence (AI) for finding the shortest path between an initial and a goal state. It operates by simultaneously running two separate search processes—one forward from the initial state and the other backward from the goal state. The search stops when the two processes meet in the middle. This method is particularly useful in large search spaces where traditional search techniques like Depth-First Search (DFS) or Breadth-First Search (BFS) may be inefficient.

How Bidirectional Search Works?

Bidirectional search uses two simultaneous searches to potentially reduce the total search time. Here’s a step-by-step breakdown of how it typically works:
    -Initial Setup: Initialize two searches. One starts from the initial state and expands forward. The other starts from the goal state and expands backward.
    -Node Expansion: Both searches alternately expand the nearest unexplored node. For each node, all possible successors (in the forward direction) or predecessors (in the backward direction) are generated.
    -Checking Intersections: After each expansion, check if any of the newly generated nodes are present in the frontier of the opposite search.
    -Meeting Point: Once a common node is discovered, this node acts as the meeting point, and the optimal path can be constructed by joining the paths from the initial state to the meeting point and from the meeting point to the goal state.

Practical Applications of Bidirectional Search in AI

Bidirectional search is not just a theoretical construct but has practical applications in various fields within AI:
    -Pathfinding in AI Navigation Systems: Commonly used in scenarios ranging from GPS navigation to movement planning in robotics.
    -Puzzle Solving: Effective in games and puzzle-solving where a clear goal state is defined, such as in solving Rubik's Cube.
    -Network Analysis: Useful in social network analysis, where connections between entities (like finding the degree of separation between two people) need to be established quickly.

Properties of search algorithms

Complete: If we use BFS in both searches.
Optimal
Time Complexity: O(bd)
Space Complexity: O(bd)

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)

""",
"Best-First Search" : """
Best-First Search

BFS stands for Best First Search, which is a type of Search in the context of artificial intelligence that aims to choose the best paths toward the target path by evaluating the nodes using a pre-stipulated evaluation function. This algorithm takes the best features of the DFS and BFS strategies to perform an efficient search in a search space. Heuristic information assists the BFS algorithm in choosing the next appropriate node for expansion so as to minimize the overall Search and potential to get closer to the goal state.

The evaluation function, normally used as a heuristic function, measures the cost of steps needed to reach the goal from the current node. Using an example, in Greedy Best-First Search such as A*, the algorithm preferentially opens nodes with the least estimated cost and swiftly moves towards the goal node. In contrast, the A* Search algorithm considers two factors: the cost of the path and the estimated cost to reach the goal, making it even more effective in the selection of the most suitable path. BFS can originate from any node and expand in all directions at once; this is especially advantageous when searching over a large area and the goal is not easily recognizable. Still, BFS is quite powerful in practice, but its success greatly depends on the quality of the heuristic function applied, which defines the algorithm's outcome and precision.

In simpler terms, Best-first search algorithm chooses the nodes, taking into consideration the goal's cost estimate. It favors those nodes that look like they are closest to the goal, but it does not always guarantee an optimal solution. It is useful when a good heuristic is found, meaning that we do not always have to solve the problem from scratch.

The Mechanism of Greedy Best-first search Algorithm

The algorithm attempts to complete its search with the shortest heuristic cost on the nodes, effectively seeking to reach the goal. Steps:
    1. Initialization:
        -Begin with the first node that you have chosen, which is also the only node we have.
        -Enter the first node into the priority queue by the amount of its estimated heuristic function h(n).  
    2. Expand the most promising node:
        -The marked node with the lowest value - this node must be removed
        -The next available processor takes an h(n) from the priority queue.
        -If this node is the goal, then print the path at this node, and the search is done.
    3. Generate successors:
        -Produce all possible successors (the cellular neighbours) of the current node.
    4. Evaluate and add successors:
        -Determine a heuristic value h for each of the successors.
        -The successors are added to the priority queue according to their h values.
    5. Repeat:
        -Perform steps 2 to 4 as many times as could be possible until either a goal node is discovered or until the priority queue is exhausted and no nodes can be retrieved from it.

Unique Features in the Best First Search Algorithm

Heuristic Evaluation Function: BFS always has an order of visiting nodes determined by a heuristic evaluation function. This function calculates the cost required from the starting node to the goal node, thus increasing the algorithm's efficiency by identifying the most prospecting moves.

Priority Queue: The nodes to be explored are stored in the prioritized queue in BFS. The paths that correspond to nodes that are defined as the farthest from the heuristic costs' start point are given high preference, giving the algorithm a better chance of pursuing the best paths first.

Generality: The BFS algorithm is indeed rather general and can be used for further needs with specific alterations. Due to the changes in heuristic function, the BFS can be converted to another, such as the A* Search, and thus helpful in solving different forms of search problems.

Informed Search: While the searched paths, in this case, are generated randomly without any information on the costs to the target, BFS is an informed search algorithm. Heuristics help to control the direction of the search, thus making it more effective in arriving at the best search path.

Applications of Best First Search

    -Pathfinding in Games: BFS algorithms are frequently employed in video games to a path for character to reach its goal from the starting point.
    -Robotics: In robotics, BFS algorithms are useful for applying movement in the presence of navigation. 
    -Network Routing: Nowadays, BFS algorithms are employed in network routing, enabling data packets to pass through the network with ease. 
    -Artificial Intelligence: BFS algorithms are very important to AI when it comes to providing solutions to difficult issues like NL, ML, and decision-making solutions. 
    -Navigation Systems: Navigation systems, including GPS, use BFS algorithms to determine the shortest and quickest means of traveling. 

Properties of search algorithms

Complete: No, it is incomplete, even if the given state space is finite.
Optimal: No
Time Complexity: O(bm), where m is the maximum depth of the search space.
Space Complexity: O(bm)


""", 
"A* Search" : """
A* Search

Developed in 1968 by Peter Hart, Nils Nilsson, and Bertram Raphael, the A* algorithm was designed as an extension and improvement of Dijkstra's algorithm, which is also known for finding the shortest path between nodes in a graph. Unlike Dijkstra's algorithm, which uniformly explores all directions around the starting node, A* uses heuristics to estimate the cost from a node to the goal, thereby optimizing the search process and reducing the computational load.

The Mechanism of A* Algorithm

The core of the A* algorithm is based on cost functions and heuristics. It uses two main parameters:
    -g(n): The actual cost from the starting node to any node n.
    -h(n): The heuristic estimated cost from node n to the goal. This is where A* integrates knowledge beyond the graph to guide the search.

The sum, f(n)=g(n)+h(n), represents the total estimated cost of the cheapest solution. The A* algorithm functions by maintaining a priority queue (or open set) of all possible paths along the graph, prioritizing them based on their f(n) values. The steps of the algorithm are as follows:
    1. Initialization: Start by adding the initial node to the open set with its f(n).
    2. Loop: While the open set is not empty, the node with the lowest f(n) value is removed from the queue.
    3. Goal Check: If this node is the goal, the algorithm terminates and returns the discovered path.
    4. Node Expansion: Otherwise, expand the node (find all its neighbors), calculating g, h, and f values for each neighbor. Add each neighbor to the open set if it's not already present, or if a better path to this neighbor is found.
    5. Repeat: The loop repeats until the goal is reached or if there are no more nodes in the open set, indicating no available path.

Heuristic Function in A* Algorithm

The effectiveness of the A* algorithm largely depends on the heuristic used. The choice of heuristic can dramatically affect the performance and efficiency of the algorithm. A good heuristic is one that helps the algorithm find the shortest path by exploring the least number of nodes possible. The properties of a heuristic include:
    -Admissibility: A heuristic is admissible if it never overestimates the cost of reaching the goal. The classic example of an admissible heuristic is the straight-line distance in a spatial map.
    -Consistency (or Monotonicity): A heuristic is consistent if the estimated cost from the current node to the goal is always less than or equal to the estimated cost from any adjacent node plus the step cost from the current node to the adjacent node.

Common heuristics include the Manhattan distance for grid-based maps (useful in games and urban planning) and the Euclidean distance for direct point-to-point distance measurement.

Applications of A*

The A* algorithm's ability to find the most efficient path with a given heuristic makes it suitable for various practical applications:
    -Pathfinding in Games and Robotics: A* is extensively used in the gaming industry to control characters in dynamic environments, as well as in robotics for navigating between points.
    -Network Routing: In telecommunications, A* helps in determining the shortest routing path that data packets should take to reach the destination.
    -AI and Machine Learning: A* can be used in planning and decision-making algorithms, where multiple stages of decisions and movements need to be evaluated.

Properties of search algorithms

Complete: Yes, as long as:
    -The branching factor is finite.
    -The cost at every action is fixed.
Optimal: Yes, if it follows these two conditions:
    -Admissible: h(n) should be an admissible heuristic for A* tree search. An admissible heuristic is optimistic in nature.
    -Consistent: This condition is only required for A* graph search.
Time Complexity: O(bd), where b is the branching factor. The time complexity is dependent on the heuristic function. The number of nodes expanded is exponential to the depth of the solution (d).
Space Complexity: O(bd)

where, b: Maximum branching factor of the search tree (actions per state).
       d: Depth of the solution
       m: Maximum depth of the state space (may be ∞)

""",
}
