import time

MAXN = 100
MAXM = 100

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [0, 0, 0, -1, -1, -1, 1, 1, 1]

def isValid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def canAssignMine(arr, x, y, N, M):
    if not isValid(x, y, N, M):
        return False
    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        if isValid(nx, ny, N, M) and arr[nx][ny] == 0:
            return False
    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        if isValid(nx, ny, N, M):
            arr[nx][ny] -= 1
    return True

def findUnvisited(visited, N, M):
    for x in range(N):
        for y in range(M):
            if not visited[x][y]:
                return (x, y)
    return None

def isVisitedandSatisfied(arr, visited, N, M):
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 or not visited[i][j]:
                return False
    return True

def SolveBackTrackMinesweeper(grid, arr, visited, N, M):
    if isVisitedandSatisfied(arr, visited, N, M):
        return True
    unvisited = findUnvisited(visited, N, M)
    if unvisited is None:
        return False
    x, y = unvisited
    visited[x][y] = True
    if canAssignMine(arr, x, y, N, M):
        grid[x][y] = 'X'
        if SolveBackTrackMinesweeper(grid, arr, visited, N, M):
            return True
        grid[x][y] = '-'
        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]
            if isValid(nx, ny, N, M):
                arr[nx][ny] += 1
    if SolveBackTrackMinesweeper(grid, arr, visited, N, M):
        return True
    visited[x][y] = False
    return False

# Example input
N = 8
M = 8
arr = [
    [1, 1, 1, 0, 1, 1, 1, 0],   
    [1, 1, 1, 0, 2, 3, 4, 2],
    [0, 0, 0, 0, 1, 2, 4, 3],
    [1, 1, 1, 0, 1, 2, 4, 3],
    [1, 2, 2, 1, 0, 0, 1, 1],
    [2, 3, 2, 1, 0, 0, 0, 0],
    [1, 3, 2, 2, 0, 0, 0, 0],
    [1, 2, 1, 1, 0, 0, 0, 0]
]
start_time = time.perf_counter()
end_time = time.perf_counter()
grid = [['-' for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
execution_time = (end_time - start_time) * 1000

if SolveBackTrackMinesweeper(grid, arr, visited, N, M):
    print("Solusi ditemukan:")
    # for row in grid:
    #     print(' '.join(row))
else:
    print("No solution found.")

def SolveBruteForceMinesweeper(grid, arr, visited, N, M):
    for x in range(N):
        for y in range(M):
            if not visited[x][y]:
                visited[x][y] = True
                if canAssignMine(arr, x, y, N, M):
                    grid[x][y] = 'X'
                    if SolveBruteForceMinesweeper(grid, arr, visited, N, M):
                        return True
                    grid[x][y] = '-'
                    for i in range(9):
                        nx, ny = x + dx[i], y + dy[i]
                        if isValid(nx, ny, N, M):
                            arr[nx][ny] += 1
                visited[x][y] = False
    return isVisitedandSatisfied(arr, visited, N, M)

if SolveBruteForceMinesweeper(grid, arr, visited, N, M):
    print("Solution found:")
    for row in grid:
        print(' '.join(row))
else:
    print("No solution found.")

print(f"Execution time: {execution_time} ms")
