# 주식투자
# ICPC 2015

from collections import deque

t = int(input())
for _ in range(t):
    d = int(input())
    dl = deque((map(int, input().split()))) # deque로 설정
    b=0
    r=0
    while dl:
        a = dl.pop() # a는 dl의 가장 마지막 원소
        if a>b: # a가 b보다 크면
            b = a # b는 a임
            continue
        r += b-a # b가 a보다 크면 바로 r에 더함

    print(r)
