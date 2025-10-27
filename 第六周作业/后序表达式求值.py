def cal(m, n, sign):
    if sign == '+':
        return m + n
    elif sign == '-':
        return m - n
    elif sign == '*':
        return m * n
    elif sign == '/':
        return m / n

def main():
    n = int(input())
    for i in range(n):
        stack = []
        string = list(input().split())
        for j in string:
            if j in ['+', '-', '*', '/']:
                q = stack.pop()
                p = stack.pop()
                stack.append(cal(p, q, j))
            else:
                stack.append(float(j))
        print(f'{stack[0]:.2f}')



if __name__ == '__main__':
    main()