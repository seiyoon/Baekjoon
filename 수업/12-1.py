# 도어락

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    password = input()
    fake_password = input()

    if fake_password.find(password) == -1:
        print(0)
    else:
        print(1)