import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(V, E, R, order):
    V[R] = order
    edges = E[R]

    for edge in edges:
        if V[edge] == 0:
            order = DFS(V, E, edge, order+1)
    return order

N, M, R = map(int, input().split())
V = [0 for _ in range(N + 1)]
E = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

for i in range(1, N + 1):
    E[i].sort()

DFS(V, E, R, 1)

for i in range(1, N + 1):
    print(V[i])