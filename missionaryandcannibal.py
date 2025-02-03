def missionaries_and_cannibals():
    from collections import deque

    initial_state = (3, 3, 1)  
    target_state = (0, 0, 0)
    visited = set()
    q = deque([(initial_state, [])])

    while q:
        (missionaries, cannibals, boat), path = q.popleft()

        if (missionaries, cannibals, boat) in visited:
            continue
        visited.add((missionaries, cannibals, boat))

        if (missionaries, cannibals, boat) == target_state:
            return path + [target_state]

      
        possible_moves = [
            (-1, 0), (-2, 0), (0, -1), (0, -2), (-1, -1)
        ]
        for m, c in possible_moves:
            new_state = (
                missionaries - m * boat,
                cannibals - c * boat,
                1 - boat
            )
            if is_valid(new_state):
                q.append((new_state, path + [(missionaries, cannibals, boat)]))

    return "No solution"

def is_valid(state):
    m, c, b = state
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

# Example
print(missionaries_and_cannibals())
