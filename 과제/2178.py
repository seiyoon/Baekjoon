# 백준 2178
# 미로탐색

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + row[i]
            ny = y + column[i]

            if 0 <= nx < n and 0 <= ny < m:
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y]+1
                    q.append((nx, ny))

    return miro[n-1][m-1]

n, m = map(int, input().split())
miro = []

for _ in range(n):
    miro.append(list(map(int, input())))

row = [-1, 1, 0, 0]
column = [0, 0, -1, 1]

print(bfs(0, 0))