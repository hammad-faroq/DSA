from collections import deque


def nearest_exit(maze, start):
    rows = len(maze)
    cols = len(maze[0])
    q = deque()
    q.append((start[0], start[1], 0))
    visited = set()
    visited.add((start[0], start[1]))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c, dist = q.popleft()
        # Check if it's an exit (like the border if row==fist row or lsat row , row-1)
        if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and (r, c) != tuple(start):
            return dist  # shortest distance (BFS guarantee)

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == "." and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))
    return -1  # no exit found
