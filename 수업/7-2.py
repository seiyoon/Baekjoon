# 동적배열

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0]*2 for _ in range(101)] # 배열
    cnt = 0

    for _ in range(n):
        a, c = map(int, input().split()) # 배열 번호 / 입력될 데이터 수
        arr_size = 2

        if arr[a][1] == 0:
            while arr_size < c:
                arr_size *= 2
            arr[a][0] += c
            arr[a][1] = arr_size

        elif arr[a][1] < arr[a][0] + c:
            cnt += arr[a][0]
            arr[a][0] += c
            while True:
                if arr[a][1] < arr[a][0]:
                    arr[a][1] *= 2
                else:
                    break

        else:
            arr[a][0] += c

    print(cnt)