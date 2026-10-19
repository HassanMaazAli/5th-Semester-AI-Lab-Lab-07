def bfs_shortest_path(graph, start, goal):
    # Queue stores tuples of (current_node, path_taken)
    queue = [(start, [start])]
    visited = {start}

    while queue:
        current_node, path = queue.pop(0)

        if current_node == goal:
            return path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

# Initial network configuration
network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara", "Usman"],
    "Usman": ["Hira"],
}

path = bfs_shortest_path(network, "Ali", "Hira")

if path:
    print(f"Shortest chain from Ali to Hira: {path}")
    print(f"Number of introductions needed: {len(path) - 1}")
else:
    print("No path found.") 