# 19:32-21:37
zhouyu = input()
stack = [['', -1]]
length_zhouyu = 0
temp = 0
for i in range(len(zhouyu)):
    stack.append([zhouyu[i],i])
    if len(stack) < 2:
        continue
    if zhouyu[i] == ')':
        if stack[-2][0] == '(':
            stack.pop()
            stack.pop()
stack.append(['', i+1])
for i in range(1, len(stack)):
    length_zhouyu = max(stack[i][1]-stack[i-1][1]-1, length_zhouyu)

print(length_zhouyu)
