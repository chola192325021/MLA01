from collections import deque

def three_jug_problem(jug1_cap, jug2_cap, jug3_cap, target):
    # Initial state: jug1 has 12L, jug2 and jug3 are empty
    start = (jug1_cap, 0, 0)
    visited = set()
    queue = deque([(start, [])])

    while queue:
        (a, b, c), path = queue.popleft()

        if (a, b, c) in visited:
            continue

        visited.add((a, b, c))
        path = path + [(a, b, c)]

        # Check if target is reached in any jug
        if a == target or b == target or c == target:
            print("Steps to reach target:")
            for step in path:
                print(step)
            return

        # All possible pour operations
        states = []

        # Pour jug1 → jug2
        t = min(a, jug2_cap - b)
        states.append((a - t, b + t, c))

        # Pour jug1 → jug3
        t = min(a, jug3_cap - c)
        states.append((a - t, b, c + t))

        # Pour jug2 → jug1
        t = min(b, jug1_cap - a)
        states.append((a + t, b - t, c))

        # Pour jug2 → jug3
        t = min(b, jug3_cap - c)
        states.append((a, b - t, c + t))

        # Pour jug3 → jug1
        t = min(c, jug1_cap - a)
        states.append((a + t, b, c - t))

        # Pour jug3 → jug2
        t = min(c, jug2_cap - b)
        states.append((a, b + t, c - t))

        for state in states:
            if state not in visited:
                queue.append((state, path))

    print("Target not reachable")



three_jug_problem(8, 5, 3, 4)
