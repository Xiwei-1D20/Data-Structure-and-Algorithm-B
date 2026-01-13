stack = []
helper = []
while 1:
    try:
        os = input().split()
        if os[0] == 'push':
            stack.append(int(os[1]))
            if helper:
                if int(os[1]) > helper[-1]:
                    helper.append(helper[-1])
                    continue
            helper.append(int(os[1]))
        elif os[0] == 'pop':
            if len(stack) > 0:
                stack.pop()
                helper.pop()
        else:
            if len(stack) > 0:
                print(helper[-1])

    except EOFError:
        break