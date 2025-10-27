def main():
    n = int(input())
    result = []
    def backtrack(n):
        temp = 0
        if n > 1:
            backtrack(n - 1)
        else:
            result.append(1)
        for i in range(n):
            temp += result[i]*result[n-i-1]
        result.append(temp)
    backtrack(n)
    print(result[-1])

if __name__ == '__main__':
    main()