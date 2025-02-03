from collections import deque

def water_jug_solver(jug1, jug2, target):
    visited = set()
    q = deque([(0, 0)])  # Start with both jugs empty

    while q:
        current = q.popleft()
        x, y = current

        if current in visited:
            continue
        visited.add(current)

        if x == target or y == target:
            return f"Solved: {current}"

        # Possible states
        next_states = [
            (jug1, y),  # Fill jug1
            (x, jug2),  # Fill jug2
            (0, y),     # Empty jug1
            (x, 0),     # Empty jug2
            (min(x + y, jug1), y - (min(x + y, jug1) - x)),  # Pour jug2 to jug1
            (x - (min(x + y, jug2) - y), min(x + y, jug2))   # Pour jug1 to jug2
        ]

        for state in next_states:
            if state not in visited:
                q.append(state)

    return "No solution"

# Example
print(water_jug_solver(4, 3, 2))
