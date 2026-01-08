def dfs(graph, start):
    visited = set()
    stack = [start]

    print("DFS Traversal:", end=" ")

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

graph = {
    '1': ['2', '7'],
    '2': ['1', '3', '6'],
    '3': ['2', '4','5'],
    '4': [],
    '5': [],
    '6': [],
    '7': ['1','8','10'],
    '8': ['7','9'],
    '9': [],
    '10':[]
}

dfs(graph,'1')
