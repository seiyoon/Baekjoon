# 편세권

'''
1. 집으로부터 거리가 10 이하인 편의점의 수
 2. 집으로부터 거리가 3 이하인 편의점 × 2
 3. 거리는 맨하탄 거리로 계산
 4. 편의점이 있는 위치는 제외
'''

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    cc = []
    count = 0
    mmap = [[0]*n for _ in range(n)]
    for _ in range(c):
        a, b = map(int, input().split())
        mmap[a][b] = -1
        cc.append([a, b])

    max = [0, 0, 0]

    for i in range(n):
        for j in range(n):
            if mmap[i][j] == -1:
                continue
            for a, b in cc:
                dist = abs(a - i) + abs(b - j) # abs : 절대값 함수
                if dist <= 3:
                    count += 3
                elif dist <= 10:
                    count += 1
            if count > max[2]:
                max = [i, j, count]
            count = 0

    for i in max:
        print(i, end=' ')
    print()