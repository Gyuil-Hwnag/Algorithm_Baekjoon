import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0<=nx<N) and (0<=ny<N):
            if arr[nx][ny]>h and visited[nx][ny]==0:
                visited[nx][ny] = 1
                dfs(nx, ny, h)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

for k in range(max(map(max, arr))):
    cnt = 0
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]>k and visited[i][j]==0:
                visited[i][j] = 1
                cnt += 1
                dfs(i, j, k)
    res = max(res, cnt)

print(res)