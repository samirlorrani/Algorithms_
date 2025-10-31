# Simplified 2D grid version (assumes uniform cost)
def jps(start, goal, grid):  # grid: 0=free, 1=wall
    open_set = [(0, start[0], start[1])]  # (f_score, x, y)
    came_from = {}
    g_score = {start: 0}
    while open_set:
        current = heapq.heappop(open_set)[-1]  # Pop lowest f
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in get_neighbors(current, grid):
            if is_jump_point(current, neighbor, grid):  # Prune non-jump points
                tentative_g = g_score[current] + dist(current, neighbor)
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor[0], neighbor[1]))
    return None