# 백준 2606
# 바이러스

from collections import deque

c = int(input())
n = int(input())
graph = [[] for i in range(c+1)]
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (c+1)   # 방문처리 : 방문한 컴퓨터 수를 출력해야하므로 visited에 true/false가 아닌 0/1로 처리

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

bfs(1)
print(sum(visited)-1)   # 방문한 컴퓨터 개수 - 1번 컴퓨터