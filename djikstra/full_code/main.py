def dijkstra(graph, src, dest):
    # Create an empty unvisited set to keep track of the nodes that haven't yet been visited
    unvisited = set()
    # Create an empty predecessors dictionary to keep track of the path we're traversing
    predecessors = {}
    # Create an empty distances dictionary to keep track of the shortest known distance from the src to each node
    distances = {}
    
    # Add each node to the unvisited set and initialize distances to infinity
    for node in graph:
        unvisited.add(node)
        distances[node] = float('inf')
    
    # Set the distance to the src node to 0
    distances[src] = 0
    
    # While there are still nodes to visit
    while unvisited:
        # Get the node with the minimum distance from the src that hasn't yet been visited
        min_dist_node = get_min_dist_node(distances, unvisited)
        
        # If we couldn't find a valid node, break out of the loop
        if min_dist_node is None:
            break
            
        # Mark that node as visited
        unvisited.remove(min_dist_node)
        
        # If the min_dist_node is the destination, we're done
        if min_dist_node == dest:
            return get_path(dest, predecessors)
        
        # For each unvisited neighbor of the min_dist_node
        for neighbor, weight in graph[min_dist_node].items():
            if neighbor in unvisited:
                # Calculate the total distance from src to neighbor through min_dist_node
                distance = distances[min_dist_node] + weight
                
                # If the total distance is less than the previously known distance
                if distance < distances[neighbor]:
                    # Update the distance
                    distances[neighbor] = distance
                    # Update the predecessor
                    predecessors[neighbor] = min_dist_node
    
    # If we get here, there's no path to the destination
    return get_path(dest, predecessors)
    


# don't touch below this line


def get_path(dest, predecessors):
    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path


def get_min_dist_node(distances, unvisited):
    min_dist = float("inf")
    min_dist_node = None
    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            min_dist_node = v
    return min_dist_node
