# 계산기만들기

t = int(input())
for i in range(t):
    n = int(input())
    i_s = list(input().split())
    stack = []
    result = ''
    rlist = []
    print(i_s)
    
    for s in i_s:
        if s.isdigit():
            result += s
            result += ','
        else:
            if s == '(':
                stack.append(s)
            elif s == '*' or s == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                    result += ','
                stack.append(s)
            elif s == '+' or s == '-':
                while stack and (stack[-1] != '('):
                    result += stack.pop()
                    result += ','
                stack.append(s)
            elif s == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                    result += ','
                stack.pop()
    while stack:
        result += stack.pop()
    print(result)
    rlist = list(result.split(','))

    stack=[]
    print(rlist)
    for j in rlist:
        if j == '+':
            stack.append(stack.pop() + stack.pop())
        elif j == '-':
            top = stack.pop()
            stack.append(stack.pop() - top)
        elif j == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(j))
            
    print(stack.pop())
