import sys
input = sys.stdin.readline

def Solve():
    global dp
    for i in range(n):
        for j in range(n):
            if i == n - 1 and j == n - 1:
                print(dp[i][j])
                break

            if j + board[i][j] < n:
                dp[i][j + board[i][j]] += dp[i][j]

            if i + board[i][j] < n:
                dp[i + board[i][j]][j] += dp[i][j]

n = int(input())
board = list(list(map(int, input().split())) for _ in range(n))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
Solve()