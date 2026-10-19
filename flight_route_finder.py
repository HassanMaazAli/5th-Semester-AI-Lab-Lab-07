def path_cost(path):
    return sum(cost for _, cost in path)

def ucs_cheapest_route(graph, start, goal):
    visited = set()
    # Queue stores list of tuples: [(city1, cost1), (city2, cost2), ...]
    queue = [[(start, 0)]]
    explored_count = 0

    print("--- Paths Explored in Order ---")
    while queue:
        # Sort queue by path cost (lowest first)
        queue.sort(key=path_cost)
        path = queue.pop(0)
        current_node = path[-1][0]
        current_cost = path_cost(path)

        explored_count += 1
        city_sequence = [city for city, _ in path]
        print(f"Exploring: {city_sequence} with cost {current_cost}")

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            route = [city for city, _ in path]
            return route, current_cost, explored_count

        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(path + [(neighbor, cost)])

    return None, None, explored_count

flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": [],
}

route, cost, explored_count = ucs_cheapest_route(flights, "Islamabad", "Quetta")
print("\nCheapest route:", route)
print("Total ticket cost:", cost)