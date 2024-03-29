## 14651
import sys

input = sys.stdin.readline
N = int(input())
dp = [0 for _ in range(N+1)]
 
if N >= 2:
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = (dp[i-1] * 3) % 1000000009
 
print(dp[N])