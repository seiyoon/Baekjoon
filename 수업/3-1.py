# 택배배송

from collections import deque

t = int(input())

for _ in range(t):

    n, m, a, b = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    start = 1000000000
    end = 1

    def bfs(c):
        queue = deque([a])
        visited = [False] * (n+1)
        visited[a] = True
        while queue:
            x = queue.popleft()
            for y, weight in graph[x]: # mid값이 거리에 해당하는 weight보다 작은지 검사
                if not visited[y] and weight >= c:
                    visited[y] = True
                    queue.append(y)
        return visited[b]

    for _ in range(m): # 양방향
        o, d, c = map(int, input().split())
        graph[o].append((d, c))
        graph[d].append((o, c))
        start = min(start, c)
        end = max(end, c)

    result = start
    while start <= end:
        mid = (start + end) // 2
        if bfs(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)