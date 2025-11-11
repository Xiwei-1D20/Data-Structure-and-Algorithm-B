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
    n = int(input())
    dp = [[1 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            elif i == j:
                dp[i][j] = dp[i][j-1] + 1
            elif i > j:
                dp[i][j] = dp[i-j][j] + dp[i][j-1]
            elif i < j:
                dp[i][j] = dp[i][i]

    #ans = [1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604, 6842, 8349, 10143, 12310, 14883, 17977, 21637, 26015, 31185, 37338, 44583, 53174, 63261, 75175, 89134, 105558, 124754, 147273, 173525, 204226]
    print(dp[n][n])
    #if dfs(n, n) == ans[n - 1]:
        #print(1)

if __name__ == '__main__':
    main()