def lex_bfs(graph):  # graph: adj list
    n = len(graph)
    order = []
    labels = [set() for _ in range(n)]
    unnumbered = set(range(n))
    for _ in range(n):
        v = max(unnumbered, key=lambda u: len(labels[u]))  # Max label size
        order.append(v)
        unnumbered.remove(v)
        for u in graph[v]:
            if u in unnumbered:
                labels[u].add(len(order) - 1)
    return order[::-1]