def get_min_dist_node(distances, unvisited):
    smallest = float('inf')
    min_dist_node = None
    for n in unvisited:
        if distances[n] < smallest:
            smallest = distances[n]
            min_dist_node = n
                
    return min_dist_node