def get_path(dest, predecessors):
    """
    Reconstructs the path from a source node to a destination node using a predecessors dictionary.
    
    Args:
        dest (str): A string representing the label of the destination node.
        predecessors (dict): A dictionary mapping each node to its predecessor.
                            For example, {'a': 'b'} means that 'b' leads to 'a'.
    
    Returns:
        list: A list of nodes representing the path through the graph.
              The last node in the list will be the destination node,
              and the first node will be the source node.
              Returns an empty list if no path exists.
    """
    current_node = dest
    path = [current_node]
    while current_node in predecessors:
      predecessor_node = predecessors[current_node]
      path.insert(0, predecessor_node)
      current_node = predecessor_node
      
    return path
      
    
