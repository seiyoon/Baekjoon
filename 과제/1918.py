# 백준 1918
# 후위 표기식

'''
우선순위
1. ( )
2. * /
3. + -
'''

str = list(input())
stack = []
result = ''

for s in str:
    if s.isalpha():
        result += s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(s)
        elif s== '+' or s == '-':
            while stack and (stack[-1] != '('):
                result += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)
