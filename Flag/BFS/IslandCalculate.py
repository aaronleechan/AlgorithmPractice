from collections import deque

def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]: # the the value is 1 which mean island
                print({"Start_x": i},{"Start_y": j})
                bfs(grid,i,j)
                islands += 1
    return islands

def bfs(grid,x,y):
    queue = deque([(x,y)])
    grid[x][y] = False
    while queue:
        x, y = queue.popleft()
        for testx,texty in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            next_x = x + testx
            next_y = y + texty
            if not valid(grid, next_x, next_y):
                continue
            queue.append((next_x, next_y))
            grid[next_x][next_y] = False

def valid(grid,x,y):
    outside = len(grid)
    inside = len(grid[0])
    return 0 <= x < outside and 0 <= y < inside and grid[x][y]



# numIslandCitiesgrid = [
#     [1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 1],
#     [0, 0, 2, 1, 2],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 2]
# ]
# solution = numIslandCities(numIslandCitiesgrid)
# print({"numIslandCitiesgrid Solution": solution})

numsofIslandgrid = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [0,0,0,1,1],
    [0,0,0,0,0],
    [0,0,0,0,1]
]
solutionTwo = numIslands(numsofIslandgrid)
print({"numsofIslandgrid Solution": solutionTwo})




