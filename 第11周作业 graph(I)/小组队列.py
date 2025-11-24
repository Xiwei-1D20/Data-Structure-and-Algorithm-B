from collections import deque


def main():
    n = int(input())
    teams = [0]*n  # 用于存储小队中处于队列的人数
    teams_index = dict()  # 用于存储小队队员属于哪个队列
    for i in range(n):
        for j in [int(x) for x in input().split()]:
            teams_index[j] = i
    q = deque()
    while 1:
        os = input().split()
        if os[0] == 'STOP':
            break
        elif os[0] == 'ENQUEUE':
            identifier = int(os[1])
            if identifier in teams_index.keys():
                index = teams_index[identifier]
                if teams[index] == 0:
                    q.append([index, deque([identifier])])
                else:
                    for i in q:
                        if i[0] == index:
                            i[1].append(identifier)
                teams[index] += 1
            else:
                q.append([None, deque([identifier])])
        else:
            print(q[0][1].popleft())
            if q[0][0] is not None:
                teams[q[0][0]] -= 1
            if not q[0][1]:
                q.popleft()


if __name__ == '__main__':
    main()
