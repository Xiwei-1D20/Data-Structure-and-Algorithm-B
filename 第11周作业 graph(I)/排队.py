def main():
    n, d = [int(x) for x in input().split()]
    que = []
    for i in range(n):
        que.append(int(input()))
    diff = [0]
    for i in range(1,n):
        if que[i] - que[i-1] > d:
            diff.append(i)


if __name__ == '__main__':
    main()

