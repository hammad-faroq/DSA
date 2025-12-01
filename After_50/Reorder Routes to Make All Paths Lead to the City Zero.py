from collections import defaultdict, deque
class Solution:
    def minReorder(self, n, connections):
        graph = defaultdict(list)
        directed = set()

        # build graph
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            directed.add((a, b))  # original direction

        q = deque([0])
        visited = set([0])
        changes = 0

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    # check if original direction is node -> nei
                    if (node, nei) in directed:
                        changes += 1  # this road must be reversed
                    visited.add(nei)
                    q.append(nei)
        return changes
