
from collections import deque
def canVisitAllRooms(rooms):
    visited = set()
    queue = deque([0])    # start from room 0
    visited.add(0)

    while queue:
        room = queue.popleft()

        # neighbors are just keys inside the current room
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                queue.append(key)
    if len(visited)!=len(rooms):
        return False
    return True
print(canVisitAllRooms(rooms = [[1],[2],[3],[]]))