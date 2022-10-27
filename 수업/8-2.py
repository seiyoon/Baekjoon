# 보물찾기

direction = {
    'F': '0',
    'R': '1',
    'B': '2',
    'L': '3',
}

t = int(input())
for _ in range(t):
    n = int(input())    # n : 지도의 크기
    map = []
    check = [[0 for _ in range(n)] for _ in range(n)]   # check : 중복으로 지나가는 부분 표시할 지도
    for _ in range(n):
        map.append(input().split())

    prev_d = 2
    r, c = 0, 0

    while 1:
        a = map[r][c][0]
        b = int(map[r][c][1])
        next_d = int((prev_d + int(direction[a]))%4)

        check[r][c] += 1
        if check[r][c] >= 2:
            print(r, c)
            break

        if next_d == 0:
            r += b
        elif next_d == 1:
            c += b
        elif next_d == 2:
            r -= b
        elif next_d == 3:
            c -= b
        prev_d = next_d