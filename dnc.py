import time

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [0, 0, 0, -1, -1, -1, 1, 1, 1]

def isValid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def countAdjacentMines(arr, x, y, N, M):
    count = 0
    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        if isValid(nx, ny, N, M) and arr[nx][ny] == 'X':
            count += 1
    return count

def divideAndConquerMinesweeper(arr, N, M):
    def divideAndConquerHelper(x_start, x_end, y_start, y_end):
        if x_start == x_end or y_start == y_end:
            return

        if x_start + 1 == x_end and y_start + 1 == y_end:
            if arr[x_start][y_start] == '-':
                adjacent_mines = countAdjacentMines(arr, x_start, y_start, N, M)
                arr[x_start][y_start] = str(adjacent_mines)
            return

        x_mid, y_mid = (x_start + x_end) // 2, (y_start + y_end) // 2

        divideAndConquerHelper(x_start, x_mid, y_start, y_mid)
        divideAndConquerHelper(x_start, x_mid, y_mid, y_end)
        divideAndConquerHelper(x_mid, x_end, y_start, y_mid)
        divideAndConquerHelper(x_mid, x_end, y_mid, y_end)

    divideAndConquerHelper(0, N, 0, M)
    return arr

# Example input
N = 16
M = 16
arr = [
    ['-', 'X', '-', '-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],   
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', 'X', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
]

start_time = time.perf_counter()
result = divideAndConquerMinesweeper(arr, N, M)
end_time = time.perf_counter()
execution_time = (end_time - start_time) * 1000

print("Solusi divide and conquer ditemukan:")
for row in result:
    print(' '.join(row))

print(f"Execution time: {execution_time} ms")