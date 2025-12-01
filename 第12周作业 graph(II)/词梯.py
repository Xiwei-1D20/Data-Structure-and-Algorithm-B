from collections import defaultdict, deque


def build_graph(n: int, words: list, g: dict):
    patterns = defaultdict(set)
    for i in range(n):
        temp_word = words[i]
        for j in range(4):
            pattern = temp_word[:j] + '_' + temp_word[j+1:]
            patterns[pattern].add(temp_word)

    for pattern in patterns.keys():
        for i in patterns[pattern]:
            g[i] = g[i] | patterns[pattern] - {i}

    return g


def bfs(start: str, end: str, graph: dict):
    q = deque([[start]])
    visited = {start}
    while q:
        temp_trace = q.popleft()
        for i in graph[temp_trace[-1]]:
            if i == end:
                temp_trace.append(i)
                return temp_trace
            if i not in visited:
                visited.add(i)
                temp_trace.append(i)
                q.append(temp_trace[:])
                temp_trace.pop()
    return False


def main():
    n = int(input())
    words = []
    g = dict()
    for i in range(n):
        temp_word = input()
        words.append(temp_word)
        g[temp_word] = set()

    g = build_graph(n, words, g)
    start, end = input().split()
    result = bfs(start, end, g)
    if not result:
        print('NO')
    else:
        print(' '.join(result))


if __name__ == '__main__':
    main()

