from collections import deque
city = 0
def numIslandCities(grid):
    island = 0
    if not grid or not grid[0]:
        return city
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                bfs(grid,i,j,city)
                island += 1
    print({"City": city})
    return island

def bfs(grid,i,j,city):
    print({"BFS": grid[i][j]})
    queue = deque([(i,j)])

    if grid[i][j] == 2:
        city += 1

    grid[i][j] = False
    while queue:
        i, j = queue.popleft()
        for neighbor_x, neighbor_y in [(0,1),(0,-1),(1,0),(-1,0)]:
            visit_x = neighbor_x + i
            visit_y = neighbor_y + j
            if not valid(grid,visit_x,visit_y):
                continue
            queue.append((visit_x,visit_y))
            if grid[visit_x][visit_y] == 2:
                city += 1
            grid[visit_x][visit_y] = False

def valid(grid,x,y):
    #print({"Visit_x": x}, {"Visit_Y": y}, {"Grid": grid[x][y]})
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]


numIslandCitiesgrid = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 2, 1, 2],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2]
]
solution = numIslandCities(numIslandCitiesgrid)
print({"numIslandCitiesgrid Solution": solution})