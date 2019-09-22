import math
    
def intersection_neighbours(graph, position):
    return graph.roads[position]
     

def heuristic(graph, current, goal):
    base = (graph.intersections[current][0] - graph.intersections[goal][0]) ** 2
    height = (graph.intersections[current][1] - graph.intersections[goal][1]) ** 2
    return math.sqrt(base+height)
    

def move_cost(graph, a, b):
    base = (graph.intersections[a][0] - graph.intersections[b][0]) ** 2
    height = (graph.intersections[a][1] - graph.intersections[b][1]) ** 2
    return math.sqrt(base+height)
    
def shortest_path(M,start,goal):
    print("shortest path called")
    
    # Declare F and G as dictionaries
    G = {}
    F = {}
    
    # Initialize starting values
    G[start] = 0
    F[start] = heuristic(M, start, goal)
    
    # Initialize both open and closed set
    open_set = set()
    closed_set = set()
    
    # Initialize parent dictionary
    parent = {}
    
    # Add the start point
    open_set.add(start)
    
    # Loop until the end is found
    while len(open_set) > 0:

        # Get point in open_set with lowest F score
        current = None
        currentFscore = None
        
        for item in open_set:
            if current is None or F[item] < currentFscore:
                currentFscore = F[item]
                current = item
                
        # Found the goal
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(current)
            # Return reversed path
            return path[::-1]
        
        # Make the current point as closed
        open_set.remove(current)
        closed_set.add(current)
            
        # Update scores for vertices connected to the current position
        for child in intersection_neighbours(M, current):
            if child in closed_set:
                 # This point has already been processed exhaustively
                continue
            candidateG = G[current] + move_cost(M, current, child)
            
            if child not in open_set:
                # A new intersection discovered
                open_set.add(child)
                
            elif candidateG >= G[child]:
                # This G score is worse than previously found
                continue
                
            # Adopt this G score
            parent[child] = current
            G[child] = candidateG
            H = heuristic(M, child, goal)
            F[child] = G[child] + H
    
    return