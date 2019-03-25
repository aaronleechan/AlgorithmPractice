from collections import deque
def numIslandCities(grid):
    ans = 0
    que = deque()
    n = len(grid)
    m = len(grid[0])
    vis = [[0 for j in range(m)] for i in range(n)]
    dxy = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(n):
        for j in range(m):
            #print({"vis[i][j]": vis[i][j]},{"grid[i][j]": grid[i][j]})
            if vis[i][j] == 1 or grid[i][j] == 0: # 1 means already visited, 0 mean nothing
                continue
            que.append((i,j))
            vis[i][j] = 1
            city = False
            #print(i,j,ans)
            #print(vis)
            while len(que) > 0:
                x,y = que.popleft()
                #print({"x": x},{"y": y})
                if grid[x][y] == 2:
                    city = True
                for incx,incy in dxy:
                    tx = x + incx
                    ty = y + incy
                    if tx < 0 or tx >= n or ty < 0 or ty >= m or vis[tx][ty] == 1 or grid[tx][ty] == 0:
                        continue
                    vis[tx][ty] = 1
                    que.append((tx,ty))
                if city:
                    ans = ans + 1
    return ans


def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                bfs(grid, i, j)
                islands += 1
    return islands


def bfs(grid, x, y):
    queue = deque([(x, y)])
    grid[x][y] = False
    while queue:
        x, y = queue.popleft()
        for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            next_x = x + delta_x
            next_y = y + delta_y
            if not is_valid(grid, next_x, next_y):
                continue
            queue.append((next_x, next_y))
            grid[next_x][next_y] = False


def is_valid(grid, x, y):
    n, m = len(grid), len(grid[0])
    return 0 <= x < n and 0 <= y < m and grid[x][y]



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




