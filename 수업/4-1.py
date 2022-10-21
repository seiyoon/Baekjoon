# 사다리타기

t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split())
    ladder = []

    for _ in range(m):
        ladder.append(list(input()))

    a = 2*d - 2 # *이 있는 x 위치
    c = m

    while c != 1: # c가 9면 while문 나가기
        c -= 1
        tf = True
        if a - 1 >= 0:
            if ladder[c][a-1] == '+':
                a -= 2
                tf = False
        if tf and a+1 <= 2*n - 2:
            if ladder[c][a+1] == '+':
                a += 2

    print(a//2+1)
