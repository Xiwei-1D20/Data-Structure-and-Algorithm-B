def dfs(m, n):
    if n == 1 or m == 1:
        return 1
    elif n == m:
        return dfs(n-1, n) + 1
    elif n > m:
        return dfs(m, n-m) + dfs(m-1, n)
    elif n < m:
        return dfs(n, n)

def main():
    while 1:
        try:
            n = int(input())
            dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i == 1 or j == 1:
                        dp[i][j] = 1
                    elif i == j:
                        dp[i][j] = dp[i][j - 1] + 1
                    elif i > j:
                        dp[i][j] = dp[i - j][j] + dp[i][j - 1]
                    elif i < j:
                        dp[i][j] = dp[i][i]
            print(dp[n][n])
        except EOFError:
            break


if __name__ == '__main__':
    main()