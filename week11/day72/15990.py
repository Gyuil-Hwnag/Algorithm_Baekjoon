import sys
input = sys.stdin.readline

def Solve():
    global dp
    dp[1] = [1, 0, 0]
    dp[2] = [0, 1, 0]
    dp[3] = [1, 1, 1]
    for i in range(4, 100001):
        dp[i][0] = dp[i-1][1]%1000000009 + dp[i-1][2]%1000000009  # 합이 1로 끝나는 것 제외
        dp[i][1] = dp[i-2][0]%1000000009 + dp[i-2][2]%1000000009  # 합이 2로 끝나는 것 제외
        dp[i][2] = dp[i-3][0]%1000000009 + dp[i-3][1]%1000000009  # 합이 3으로 끝나는 것 제외

dp = [[0 for _ in range(3)] for _ in range(100001)]
n = int(input())
Solve()

for _ in range(n):
    t = int(input())
    print(sum(dp[t])%1000000009)
    