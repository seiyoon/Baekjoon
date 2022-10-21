# 사다리타기2

t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    ladder = []
    a = []
    endpoint = [] #답

    for i in range(m):
        ladder.append(input())
        if '?' in ladder[i]:
            id = i

    rd = 2*d - 2
    for i in range(m-2, id, -1):
        if rd+2 < 2*n-1:
            if ladder[i][rd+1] == '+':
                rd += 2
                continue
        if rd-2 > -1:
            if ladder[i][rd-1] == '+':
                rd -= 2
                continue
    if rd+2 < 2*n-1:
        a.append(rd+2)
    if rd-2 > -1:
        a.append(rd-2)
    a.append(rd)

    def start(s):
        for i in range(id-1, -1, -1):
            if s+2 < 2*n-1:
                if ladder[i][s+1] == '+':
                    s += 2
                    continue
            if s - 2 > -1:
                if ladder[i][s - 1] == '+':
                    s -= 2
                    continue
        return s

    for i in a:
        b = start(i) // 2 + 1
        endpoint.append(b)
    endpoint.sort()
    for i in endpoint:
        print(i, end=' ')
    print()