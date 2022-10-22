# 계단오르기

t = int(input())

for i in range(t):
    n, p = map(int, input().split())

    if p%2:
        if n % 2:  # 홀수 계단
            print(n // 2 + 1)
        else:  # 짝수 계단
            print(n // 2)
    else:
        if n%2:  # 홀수 계단
            print(n//2+1)
        else:   # 짝수 계단
            print(n//2+1)