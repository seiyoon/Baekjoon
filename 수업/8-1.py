# 이미지 회전

t = int(input())
for _ in range(t):
    n, a = map(int, input().split())
    img = []
    for i in range(n):
        pix = input()
        ppix = list(pix)
        img.append(ppix)

    if a == 90 or a == -270:
        for i in range(n):
            for j in range(n-1,-1,-1):
                print(img[j][i],end='')
            print('')
    elif a == 180 or a == -180:
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                print(img[i][j],end='')
            print('')
    elif a == -90 or a == 270:
        for i in range(n-1,-1,-1):
            for j in range(n):
                print(img[j][i],end='')
            print('')
    elif a == 0:
        for i in range(n):
            for j in range(n):
                print(img[i][j], end='')
            print('')