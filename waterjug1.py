from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])  # (jug1_amount, jug2_amount)
    path = []

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path.append((x, y))

        # Check if target is reached
        if x == target or y == target:
            print("Steps to reach target:")
            for step in path:
                print(step)
            return

        # Possible operations
        states = [
            (jug1, y),           # Fill jug1
            (x, jug2),           # Fill jug2
            (0, y),              # Empty jug1
            (x, 0),              # Empty jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour jug1 → jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour jug2 → jug1
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Target not reachable")


# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
water_jug(4, 3, 2)
