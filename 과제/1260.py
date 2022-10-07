# 백준 1260
# dfs와 bfs

from collections import deque

def dfs(v):
    print(v, end=' ')
    visited2[v] = True
    for i in graph[v]:
        if not visited2[i]:
            dfs(i)
            visited2[i]=True

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
visited2 = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print()
bfs(v)
