# 미로탐색

# 미로탐색
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) #현재 위치를 추가

    while queue:
        x, y = queue.popleft()
        for i in range(4): #현재 위치에서 4가지 방향 탐색
            nx = x + row[i]
            ny = y + column[i]

            if 0 <= nx < n and 0 <= ny < m:
               if miro[nx][ny] == 1:
                   miro[nx][ny] = miro[x][y] + 1
                   queue.append((nx, ny))

    return miro[n - 1][m - 1] #마지막 값에서 카운트 값 빼기


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    miro = []
    for i in range(n):
        miro.append(list(map(int, input())))

    row = [-1,1,0,0]
    column = [0,0,-1,1]

    print(bfs(0,0))