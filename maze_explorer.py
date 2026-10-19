def dfs_can_reach(maze, start, exit_room, visited=None, visit_order=None):
    if visited is None:
        visited = set()
    if visit_order is None:
        visit_order = []

    visited.add(start)
    visit_order.append(start)

    if start == exit_room:
        return True, visit_order

    for neighbor in maze.get(start, []):
        if neighbor not in visited:
            reached, order = dfs_can_reach(maze, neighbor, exit_room, visited, visit_order)
            if reached:
                return True, order

    return False, visit_order

# Initial maze configuration
maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": [],
    "SecretVault": [],
}

can_reach, order = dfs_can_reach(maze, "Entrance", "Exit")
print("Visit order:", order)
print("Can reach Exit from Entrance?", can_reach)