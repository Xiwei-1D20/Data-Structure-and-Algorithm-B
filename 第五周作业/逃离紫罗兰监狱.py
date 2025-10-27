Row, Col, k = map(int, input().split())
maze = []
start = None
end = None
for i in range(Row):
    maze.append(list(input()))
for i in range(Row):
    for j in range(Col):
        if maze[i][j] == 'S':
            start = ((i, j), k)
        elif maze[i][j] == 'E':
            end = (i, j)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = []
queue.append((start, 0))

visited = set()
visited.add(start)
success = 0

while queue:
    if success == 1:
        break
    current_position, path = queue.pop(0)
    for dx, dy in directions:
        index_x, index_y = current_position[0][0] + dx, current_position[0][1] + dy
        if 0 <= index_x < Row and 0 <= index_y < Col:
            if maze[index_x][index_y] == 'E':
                success = 1
                break
            elif ((index_x, index_y), current_position[1]) not in visited and maze[index_x][index_y] == '.':
                now = ((index_x, index_y), current_position[1])
                visited.add(now)
            elif maze[index_x][index_y] == '#' and current_position[1] > 0 and ((index_x, index_y), current_position[1]-1) not in visited:
                now = ((index_x, index_y), current_position[1]-1)
                visited.add(now)
            else:
                continue
            new_path = path + 1
            queue.append((now, new_path))

if success == 1:
    print(path+1)
else:
    print(-1)


